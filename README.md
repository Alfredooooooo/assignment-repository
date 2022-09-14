## Mengapa kita menggunakan Virtual Environment? 
Virtual Environment memberikan kita pilihan untuk mempunyai development environment yang berbeda dengan global development environment. Sejatinya, jika kita menjalankan semuanya dengan Python yang ada pada sistem komputer kita beserta dengan library-nya, maka project yang akan kita buat akan terbatas hanya pada Python versi tersebut. Ditambah lagi, mencoba untuk menjalankan segala aplikasi Python akan membuat hal tersebut rentan terhadap version conflict. Maka dari itu fungsi Virtual Environment cukup penting dalam hal ini yaitu:
<br>
- Kita dapat menggunakan segala versi Python yang kita mau untuk development environment yang spesifik tanpa harus mempedulikan konflik-konflik yang mungkin akan terjadi
- Main Python Package sistem tidak akan tertumpuk dengan package-package yang kurang relevan (Package yang hanya relevan terhadap satu project)
- Kita dapat mengatur pacakage kita dengan lebih mudah dan orang lain yang bekerja dengan kita juga tahu package-package yang kita gunakan dan mereka dapat menggunakan package tersebut tanpa harus men-download/men-overwrite package-package tersebut kedalam kemputer orang tersebut
<br>
TL;DR: Virtual Environment dibutuhkan agar kita dapat membuat project dengan development environment sendiri beserta package-package yang dibutuhkan pada project tersebut tanpa berhubungan dengan project-project lainnya

### Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Tentu saja jika project Django kita tidak "package dependent" (tidak memerlukan package), kita tidak perlu repot-repot untuk menyalakan virtual environment. Tetapi seperti yang kita tahu, Django merupakan package sehingga disarankan untuk membuat Virtual Environment agar kita atau rekan kerja kita tidak akan kerepotan dengan konflik konflik yang akan terjadi. Kembali ke pertanyaan, jawabannya adalah ya, kita masih bisa membuat dan membuka aplikasi web berbasis Django tanpa virtual environment. Namun, jika kita melakukan command:

   ```shell
   python -m venv env
   ```
Hal ini akan melakukan install package-package yang dibutuhkan project kita secara global walaupun pada kasus normalnya, kita tidak perlu untuk melakukan instalasi secara global karena bisa saja terjadi version conflict pada package-package tersebut.


TL;DR: Kita bisa membuat aplikasi web berbasis Django tanpa virtual environment walaupun tidak "practical"
## Cara membuat aplikasi Django dan menjalankannya

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Sebelum implementasi:

1. Menjalankan perintah berikut untuk menyalakan _virtual environment_:

   ```shell
   python -m venv env
   ```

2. Menyelakan environment dengan perintah berikut:

   ```shell
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```

3. Install dependencies yang dibutuhkan untuk menjalankan aplikasi dengan perintah berikut:

   ```shell
   pip install -r requirements.txt
   ```

## Cara mengimpementasi:

1. Membuka file views.py yang ada pada direktori katalog dan menambahkan sebuah function yaitu render_view:

   ```shell
   def render_view(request):
    return render(request, "katalog.html", rendered_fields)
   ```

2. Buka terminal (cmd) dan jalankan perintah berikut untuk melakukan migrasi skema model ke database Django lokal:

   ```shell
   python manage.py makemigrations
   ```

3. Jalankan perintah berikut untuk menerapkan skema model diatas:

   ```shell
   python manage.py migrate
   ```

4. Jalankan perintah berikut untuk memasukkan data pada initial_catalog_data.json pada database Django lokal:

   ```shell
   python manage.py loaddata initial_catalog_data.json
   ```

5. Membuka kembali views.py yang ada pada direktori katalog dan edit function yang telah dibuat yaitu render_view:

   ```shell
   def render_view(request):
    list_katalog = CatalogItem.objects.all()
    rendered_fields = {
        "list_field": list_katalog,
        "name": "Alfredo Austin",
        "student_id": "2106705865",
    }
    return render(request, "katalog.html", rendered_fields)
   ```

6. Membuka urls.py pada project_django dan tambahkan kode berikut ini:

   ```shell
   ...
   path('katalog/', include('katalog.urls')),
   ```

7. Membuka urls.py pada direktori katalog dan tambahkan kode berikut ini:

   ```shell
   from django.urls import path
   from katalog.views import render_view

   app_name = "katalog"

   urlpatterns = [
      path("", render_view, name="render_view"),
   ]
   ```

8. Membuka katalog.html pada direktori templates dan tambahkan kode berikut ini:

   ```shell
   ...
   <h5>Name: </h5>
   <p>{{name}}</p>

   <h5>Student ID: </h5>
   <p>{{student_id}}</p>

   ...
      {% for data in list_field %}
      <tr>
         <td>{{data.item_name}}</td>
         <td>{{data.item_price}}</td>
         <td>{{data.item_stock}}</td>
         <td>{{data.rating}}</td>
         <td>{{data.description}}</td>
         <td>{{data.item_url}}</td>
      </tr>
      {% endfor %}
   ...
   ```

9. Masuk ke directory assignment-repository dan push ke GitHub pada dengan menjalankan perintah berikut:

   ```shell
   git add -A
   git commit -m "Your Commit"
   git push origin main
   ```

10. Masuk ke heroku.com dan buat aplikasi bernama pbpassignment dan melakukan copy API Key pada Account settings

11. Membuka repository pada GitHub dan mengisi secret key pada Settings -> Secrets -> Actions bar

   ```shell
   HEROKU_APP_NAME: pbpassignment
   HEROKU_API_KEY: (my_secret_API_key)
   ```
## Credits

Project ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage).
