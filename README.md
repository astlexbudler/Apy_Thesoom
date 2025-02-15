# 이프유고

Django 이용하여 제작한 객실 정보 조회 및 예약 사이트.

---

## 개요

호텔의 정보와 객실 정보를 조회하고, 객실을 예약할 수 있는 예약 사이트. 관리자가 호텔과 객실 정보, 예약 정보를 업로드하면, 사용자가 객실과 날짜를 선택해서 예약을 진행. 결제 내역 확인 가능.

### 프로젝트 실행 방법

1. Django/{project_name} 디렉토리로 이동합니다.
2. 가상환경을 생성하고 실행합니다.
3. OS에 따라서 Win 기반 OS의 경우 init.ps1(PowerShell)을 실행합니다. Linux 기반 OS의 경우 init.sh를 실행합니다. requirements와 migration 및 초기 필요한 데이터가 자동으로 구성됩니다.
4. python manage.py runserver 또는 python3 manage.py runserver 명령어를 이용하여 Django 프로젝트를 실행할 수 있습니다.
5. 데이터베이스 초기화 시 다시 init 파일을 실행하여 초기 상태로 되돌릴 수 있습니다. 작성된 코드는 복구되지 않습니다.
6. .env등의 환경 변수 설정이 필요한 경우(또는 credentials.json 등등), Django 프로젝트의 루트 디렉토리에 환경 변수 파일을 저장합니다.

---

## 주의

⚠️ 시크릿 인증 키를 직접 하드코딩하지 마세요. credentials.json 파일에 인증키를 저장하고 따로 관리하여야합니다.

---

## 프로젝트 구조

프로젝트 명: ifyougo

- **app_core**:  
프로젝트의 기본 설정과 관련된 앱. 사전 설정 데이터 생성 및 스케줄러, 기본적인 설정과 관련된 테이블이 정의되어있습니다.
  - ACCOUNT (계정) Django 기본 user 모델을 상속받음
    - id: PK (기본 제공)
    - username: 아이디 (Unique)
    - password: 비밀번호
    - first_name: 닉네임
    - last_name: 파트너 업체명
    - email: 이메일
    - is_active: 활성 상태
    - is_staff: 스태프 여부
    - is_superuser: 최고 관리자 여부
    - date_joined: 가입 일자
    - last_login: 마지막 로그인
    - groups: M2M → Group
  - GROUP (그룹)
    - name 그룹 이름
  - PLACE (장소) // 호텔
    - id: PK
    - name: 장소 이름
    - intro: 짧은 소개
    - location: 장소
    - location_link: 구글 지도 링크
    - description: 소개(html)
  - PLACE_IMAGE (장소 이미지)
    - id: PK
    - place: PLACE
    - image: File
    - image_type: 이미지 타입
    - order: 이미지 표시 순서
  - PLACE_ITEM (장소 상품) // 객실, 룸서비스 등등
    - id: PK
    - place: PLACE
    - image: null=True
    - name: 상품 이름
    - description: 설명(html)
    - price: 가격
  - ITEM_DATE (상품 일자 정보) // 예약정보 또는 일자별 안내 정보
    - id: PK
    - item: ITEM
    - year: 연도
    - month: 월
    - date: 날짜
    - content: 표시할 내용
  - REVIEW (리뷰)
    - id: PK
    - place: PLACE
    - author: ACCOUNT
    - rate: 평점
    - content: 내용
    - images: Files
    - created_at: 작성일
  - PURCHASE (결제 기록)
    - id: PK
    - item: PLACE_ITEM
    - created_at: 결제 시작 일시
    - purchase_at: 결제 완료 일시
    - payment_agency: 결제사
    - payment_method: 결제 방법
    - payment_info: 결제 정보(json)
    - status: 결제 상태
- **app_api**:  
API 요청 주소와 해당 요청에 대한 처리가 정의되어있는 앱. 별도로 정의된 테이블은 없습니다.
- **app_user**:  
사용자 관련 처리를 담당하느 앱.
  - PATH:
    - / 메인 페이지
    - /login 로그인 페이지
    - /signup 회원가입 페이지
    - /find 계정 찾기 페이지
    - /reset 비밀번호 초기화 페이지
    - /profile 프로필 페이지
    - /terms 이용약관 페이지
    - /contact 연락처 페이지
- **app_place**:  
장소 관련 처리를 담당하는 앱.
  - PATH:
    - /place/detail 장소 정보 상세 페이지
    - /place/write 장소 등록 페이지
    - /place/edit 장소 수정 페이지
- **app_purchase**:  
결제 관련 처리를 담당하는 앱.
  - PATH:
    - /purchase/request 결제 요청 페이지
    - /purchase/complete 결제 요청 결과 페이지
    - /purchase/history 결제 기록
