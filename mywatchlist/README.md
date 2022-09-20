## Heroku Current Assignment Link

[Heroku MyWatchList HTML](https://pbpassignment.herokuapp.com/mywatchlist/html/)
<br>
[Heroku MyWatchList JSON](https://pbpassignment.herokuapp.com/mywatchlist/json/)
<br>
[Heroku MyWatchList XML](https://pbpassignment.herokuapp.com/mywatchlist/xml/)
<br>

## Perbedaan antara JSON, XML, dan HTML

HTML sendiri merupakan markup language untuk dokumen yang di desain untuk ditampilkan pada browser. Markup language merupakan sistem yang terdiri dari beberapa simbol/"tag" yang dipasangkan pada dokumen untuk mengontrol struktur, format, dan hubungan antara bagian-bagiannya. Dahulu kala, tiga fungsi ini menjadi isu penting namun terselesaikan dengan cara menyelimuti konten-konten dengan "tag" (sistem ini disebut GML (General Markup Language)). "Tag" ini juga mempunyai fitur untuk melakukan nesting agar konten dan strukturnya dapat lebih terkontrol. Maka dari itu, HTML muncul sebagai salah satu penerapan dari GML yang menjadi salah satu pengontrol struktur dalam dokumen agar dapat ditampilkan kedalam website dengan baik yang bahkan masih dipakai sampai sekarang.
<br>
<br>
Namun HTML sendiri berfungsi untuk menampilkan data dan mendeskripsikan struktur dari sebuah website tetapi tidak berfokus pada penyimpanan dan perpindahan data, maka hadir XML yang dapat melakukan fungsi tersebut, begitu juga JSON setelahnya. XML sendiri tidak dapat menggantikan HTML karena XML ketat dalam syntaxnya (XML tidak mentolerir error) jadi XML lahir guna membantu HTML lebih "extensible" dan fleksibel untuk bekerja dengan data. Sehingga XML memperbolehkan kita untuk menyisipkan data.
<br>
<br>
Maka dari itu, jika kita berbicara tentang data, istilah XML dan JSON tidak dapat disepelekan. Persamaan antara keduanya adalah:

- JSON dan XML sama-sama mendeskripsikan data (self describing) yang disimpan/dipindahkan (transfer)
- JSON dan XML sama-sama mempunyai hierarki
- JSON dan XML sama-sama dapat di parse dan digunakan di berbagai bahasa pemrograman
- JSON dan XML sama-sama dapat di fetch menggunakan XMLHttpRequest
  <br>
  <br>
  Selain persamaan, perbedaan antara keduanya adalah:
- JSON tidak menggunakan "end tag" (seperti <employees></employees>, <employee></employee>, <firstName><firstName/>)
- JSON lebih pendek
- JSON lebih cepat d baca dan ditulis
- JSON dapat menggunakan array
- JSON berbasis JavaScript namun XML berbasis SGML (Standard General Markup Language (dengan tag))
- XML lebih aman dibandingkan JSON
- Komen dapat diterapkan pada XML namun tidak pada JSON
- XML support berbagai encoding, JSON hanya support UTF-8 Encoding
- JSON biasa digunakan untuk merepresentasikan objek, sedangkan XML digunakan untuk merepresentasikan data-data didalamnya (dengan menggunakan struktur "tag")

Referensi:
<br>
[Data Delivery](https://scele.cs.ui.ac.id/pluginfile.php/161284/mod_resource/content/1/04%20-%20Data%20Delivery.pdf)
<br>
[HTML vs JSON vs XML](https://medium.com/@oazzat19/what-is-the-difference-between-html-vs-xml-vs-json-254864972bbb)
<br>
[XML vs JSON W3S](https://www.w3schools.com/js/js_json_xml.asp)
<br>
[XML vs JSON GFG](https://www.geeksforgeeks.org/difference-between-json-and-xml/)
<br>

## Mengapa kita membutuhkan data delivery dalam pengimplementasian sebuah platform

Kita membutuhkan data delivery karena tidak semua hal disimpan (dalam hal ini file yang berisi data-data) dalam server tetapi digenerate oleh kode program. Maka dari itu ketika browser melakukan request data, server akan mengembalikan data yang diinginkan melalui data delivery agar data dapat ditampilkan dalam platform-platform tersebut.

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

4. Membuat aplikasi baru dengan menjalankan command berikut:

   ```shell
   django-admin startapp mywatchlist
   ```

## Cara mengimpementasi:

1. Menambahkan path mywatchlist di direktori project_django pada file settings.py dan pada file urls.py

```shell
INSTALLED_APPS = [
    ...
    'katalog',
    'mywatchlist',
]
```

```shell
urlpatterns = [
    ...
    path('katalog/', include('katalog.urls')),
    path('mywatchlist/', include('mywatchlist.urls')),
]

```

2. Membuka file models.py yang ada pada direktori mywatchlist dan menambahkan sebuah class MyWatchList dengan parameter models.Model yaitu:

```shell
class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=120)
    rating = models.FloatField()
    release_date = models.CharField(max_length=120)
    review = models.TextField()
```

3. Membuat file bernama "initial_mywatchlist_data.json" dan menambahkan data sebagai objek dari model MyWatchList

4. Buka terminal (cmd) dan jalankan perintah berikut untuk melakukan migrasi skema model ke database Django lokal:

   ```shell
   python manage.py makemigrations
   ```

5. Jalankan perintah berikut untuk menerapkan skema model diatas:

   ```shell
   python manage.py migrate
   ```

6. Jalankan perintah berikut untuk memasukkan data pada initial_mywatchlist_data.json pada database Django lokal:

   ```shell
   python manage.py loaddata initial_mywatchlist_data.json
   ```

7. Membuka file views.py yang ada pada direktori mywatchlist dan menambahkan function-function berikut:

   ```shell
    def render_mywatchlist(request):
        data = MyWatchList.objects.all()
        true = 0
        for i in data:
            if (i.watched == True):
                true += 1

        context = {
            "list_watch_list": data,
            "name": "Alfredo Austin",
            "student_id": "2106705865",
            "true_number": true
        }
        return render(request, "mywatchlist.html", context)


    def show_json(request):
        data = MyWatchList.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")


    def show_json_by_id(request, id):
        data = MyWatchList.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")


    def show_xml(request):
        data = MyWatchList.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


    def show_xml_by_id(request, id):
        data = MyWatchList.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
   ```

8. Membuka urls.py pada direktori mywatchlist dan tambahkan kode berikut ini:

   ```shell
    from django.urls import path
    from mywatchlist.views import render_mywatchlist, show_json, show_json_by_id, show_xml, show_xml_by_id

    app_name = "mywatchlist"

    urlpatterns = [
        path("html/", render_mywatchlist, name="render_mywatchlist"),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
        path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    ]
   ```

9. Menambahkan script Bootstrap pada base.html agar bisa menggunakan fitur-fitur mereka:

   ```shell
   ...
   <head>
   ...
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
   </head>

   <body>
   ...

   <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js" integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3" crossorigin="anonymous"></script>
   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.min.js" integrity="sha384-7VPbUDkoPSGFnVtYi0QogXtr74QeVeeIs99Qfg5YCF+TidwNdjvaKZX19NZ/e6oz" crossorigin="anonymous"></script>
   </body>

   </html>
   ```

10. Membuka mywatchlist.html pada direktori templates dan tambahkan kode berikut ini:

    ```shell
    {% extends 'base.html' %}

    {% block content %}
        <div class="container mt-2">
            <div class="row">
                <div class="col-sm-3">
                    <div class="card" style="width: 18rem;">
                        <div class="card-body">
                        <h5 class="card-title">{{name}}</h5>
                        <p class="card-text">Mahasiswa Ilmu Komputer 2021 yang sedang menjalani mata kuliah PBP</p>
                        <p class="card-text">NPM: {{student_id}}</p>
                        </div>
                    </div>
                </div>
                <div class="col-sm-9">
                    <div class="card text-center">
                        <div class="card-header">
                        Kesimpulan
                        </div>
                        <div class="card-body">
                        <h5 class="card-title">Kesimpulan</h5>
                        {% if true_number >= 5 %}
                        <p class="card-text">Selamat, kamu sudah banyak menonton!</p>
                        {% else %}
                      <p class="card-text">Wah, kamu masih sedikit menonton!</p>
                      {% endif %}
                      <a href="https://www.imdb.com/" target="_blank" class="btn btn-primary btn-sm">Taken From</a>
                      </div>
                  </div>
              </div>
          </div>

          <table class="table table-success table-striped table-hover table-active table-bordered border-light mt-4">
              <thead>
                  <tr>
                      <th class="text-center" colspan="6">My Watch List</th></tr>
                  <tr>
                  <th scope="col">#</th>
                  <th scope="col">Title</th>
                  <th scope="col">Release Date</th>
                  <th scope="col">Rating</th>
                  <th scope="col">Watched</th>
                  <th class="text-center" scope="col">Review</th>
                  </tr>
              </thead>
              <tbody>
                  {% for watchlist in list_watch_list %}
                  <tr>
                  <th scope="row">{{watchlist.pk}}</th>
                  <td>{{watchlist.title}}</td>
                  <td>{{watchlist.release_date}}</td>
                  <td>{{watchlist.rating}}</td>
                  {% if watchlist.watched == True %}
                      <td>Watched Already</td>
                  {% else %}
                      <td>On My Watch Queue</td>
                  {% endif %}
                  <td>{{watchlist.review}}</td>
                  </tr>
                  {% endfor %}
              </tbody>
          </table>
      </div>
    {% endblock content %}
    ```

11. Membuat unit test pada tests.py untuk menguji bahwa ketiga URL diatas dapat mengembalikan respons HTTP 200 OK serta menambahkan file style.css pada static/css/:

```shell
    from django.test import TestCase, Client
    from django.urls import reverse


    # Create your tests here.
    class TestUrls(TestCase):
        def setUp(self):
            self.client = Client()
            self.html_url = ("/mywatchlist/html/")
            self.json_url = ("/mywatchlist/json/")
            self.xml_url = ("/mywatchlist/xml/")

        def test_html_url(self):
            response = self.client.get((self.html_url))
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, "mywatchlist.html")

        def test_json_url(self):
            response = self.client.get((self.json_url))
            self.assertEquals(response.status_code, 200)

        def test_xml_url(self):
            response = self.client.get((self.xml_url))
            self.assertEquals(response.status_code, 200)
```

12. Masuk ke directory assignment-repository dan push ke GitHub pada dengan menjalankan perintah berikut:

    ```shell
    git add -A
    git commit -m "Your Commit"
    git push origin main
    ```

13. Masuk ke heroku.com dan buat aplikasi bernama pbpassignment dan melakukan copy API Key pada Account settings

14. Membuka repository pada GitHub dan mengisi secret key pada Settings -> Secrets -> Actions bar

```shell
HEROKU_APP_NAME: pbpassignment
HEROKU_API_KEY: (my_secret_API_key)
```

## Penangkapan Screenshot Postman
#### HTML
![image](https://user-images.githubusercontent.com/88032017/191315536-58590161-3543-420b-817e-088d24dbdc1e.png)
![image](https://user-images.githubusercontent.com/88032017/191315621-9ae25ed0-69d3-4f18-aa61-970cdb7ab419.png)
#### JSON
![image](https://user-images.githubusercontent.com/88032017/191315744-89eeaa80-51a7-4cc4-aaa8-4525a3f2921d.png)
![image](https://user-images.githubusercontent.com/88032017/191315843-129eef0f-d51a-4eed-b545-ddb0a3597de5.png)
#### XML
  ![image](https://user-images.githubusercontent.com/88032017/191315946-f7fdd300-cc82-4365-ab1c-f5b09c6dddb5.png)
![image](https://user-images.githubusercontent.com/88032017/191316056-8b9bb786-3092-4fd3-a41e-2e0c7e3532f7.png)

