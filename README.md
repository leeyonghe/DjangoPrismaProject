# Django + Prisma(Postgres) + Docker 구축

## 프로젝트 설명

이 프로젝트는 Django를 백엔드 프레임워크로 사용하고, Prisma를 ORM으로 통합하여 Postgres 데이터베이스와 상호작용합니다. Docker를 사용하여 개발 환경을 컨테이너화하여 일관된 배포 및 실행 환경을 제공합니다.

### 주요 구성 요소
- **Django**: 강력한 웹 프레임워크로, 빠른 개발과 간단한 유지보수를 지원합니다.
- **Prisma**: 현대적인 ORM으로, 데이터베이스 스키마 관리 및 타입 안전한 쿼리를 제공합니다.
- **Postgres**: 안정적이고 확장 가능한 오픈 소스 관계형 데이터베이스.
- **Docker**: 컨테이너 기반의 가상화 기술로, 개발 환경을 표준화합니다.

### 주요 기능
1. Django와 Prisma의 통합을 통해 데이터베이스 작업을 간소화.
2. Docker를 사용하여 로컬 및 프로덕션 환경에서 동일한 설정으로 실행 가능.
3. Postgres 데이터베이스를 활용한 데이터 저장 및 관리.

### 시작하기

1. **Docker compose 설치**
```bash
# Docker Compose 설치 (Linux)
sudo curl -L "https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")')/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# 설치 확인
docker-compose --version
```

2. **Docker 컨테이너 실행**
   ```bash
   docker-compose up --build
   ```