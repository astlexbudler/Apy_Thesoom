from django.apps import AppConfig


class AppCoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_core'

    # 앱이 실행될 때 실행되는 함수
    def ready(self):

        try:
            from django.contrib.auth import get_user_model

            # 이미 관리자 계정이 생성되었는지 확인
            if not get_user_model().objects.filter(username='admin').exists():
                admin = get_user_model().objects.create_superuser( # superuser 생성
                    username='admin',
                    first_name='더숨',
                    last_name='hanzo7@naver.com, 01089474292',
                    is_superuser=True,
                    is_staff=True,
                    is_active=True
                )
                admin.set_password('ejtna513')
                admin.save()

        except Exception as e: # 마이그레이션이 안되었거나, DB가 없을 때
            print(e)
            pass
