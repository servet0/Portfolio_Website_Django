# Portfolio Website


## Kurulum

Projeyi çalıştırmak için aşağıdaki adımları takip edin:

1. **Gereksinimleri İndirin:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Veritabanını Migrate Edin:**
    ```bash
    python manage.py migrate
    ```

3. **Yönetici Hesabı Oluşturun:**
    ```bash
    python manage.py createsuperuser
    ```

4. **Sunucuyu Başlatın:**
    ```bash
    python manage.py runserver
    ```

Proje artık `http://localhost:8000` adresinde çalışır durumda olmalıdır. Yönetici paneline `http://localhost:8000/admin` adresinden erişebilirsiniz.


