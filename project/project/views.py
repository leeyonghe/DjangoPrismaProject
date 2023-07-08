from django.shortcuts import render
from prisma import Prisma
import asyncio


async def Init(name, email):
    db = Prisma(auto_register=False)
    await db.connect()
    await db.user.create(data = { 'name' : name, 'email' : email })
    await db.disconnect()

async def getUser(email):
    db = Prisma(auto_register=False)
    await db.connect()    
    user = await db.user.find_unique(where={ 'email' : email })
    await db.disconnect()
    return user

def main(request):

    email = "test@gmail.com"
    name = "test"

    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # loop.run_until_complete(Init(name, email))
    # loop.close()
    # return render(request, 'main.html', {})

    loop = asyncio.new_event_loop()
    task = loop.create_task(getUser(email))
    loop.run_until_complete(task)
    print("{}".format(task.result()))
    
    return render(request, 'main.html', { 'user' : task.result()})