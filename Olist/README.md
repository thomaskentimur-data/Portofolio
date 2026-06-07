E-commerce Business Intelligence / Data Analyst Project

Deskripsi Proyek

Proyek ini bertujuan untuk mengubah/memanfaatkan data transaksi mentah menjadi insight strategi bisnis dan menganalisa kinerja bisnis e-commerce secara menyeluruh dengan fokus pada aspek penjualan, logistik, segmentasi pelanggan, dan kinerja penjual.



Business Overview

Total Revenue: $19,613,564  merupakan total pendapatan dari seluruh transaksi
Total Orders: 95,103   merupakan total transaksi yang dibuat
Count of Customers: 92,045   merupakan total konsumen yang melakukan transaksi
Average Order Value: $206    merupakan rata rata nilai pendapatan pada setiap transaksi 
Average Freight Value: $20   merupakan rata rata nilai biaya pengiriman

Product Insight


bed_bath_table , health_beauty, computers_accesories, furniture_decor merupakan 4 kategori produk yang menyumbang pendapatan terbanyak ke perusahaan
health_beauty, watches_gifts, computers_accesories, furniture_decor, bed_bath_table merupakan 5 produk tertinggi yang memenuhi ekspektasi konsumen
Produk dengan berat lebih dari 1300 gram mendominasi kontribusi hampir setengah dari total pendapatan disusul dengan produk lebih dari 400 gram dan kurang dari 1300 gram dengan total kontribusi sebesar 28.91% dari total pendapatan dan terakhir dari produk dengan berat kurang dari sama dengan 400 gram dengan kontribusi sebesar 22.03% dari total pendapatan
Produk dengan volume lebih dari 12500 cm3 paling banyak diminati oleh konsumen , lalu disusul  dengan kurang dari sama dengan 12500 dan lebih dari 3780, dan terakhir kurang dari sama dengan 3780.

dari insight diatas dapat disimpulkan bahwa konsumer lebih suka transaksi pada jenis produk yang memiliki volume dan berat yang cukup besar dibanding produk yang berukuran kecil

Solusi Strategis

Optimalisasi Logistik untuk Produk Besar
Mengingat produk dengan berat >1300g dan volume >12500cm³ adalah penyumbang pendapatan terbesar, perusahaan harus memastikan efisiensi biaya pengiriman. Karena biaya rata-rata pengiriman adalah $20, negosiasi dengan vendor logistik untuk tarif pengiriman barang berukuran besar dapat meningkatkan margin keuntungan secara signifikan.  

Peningkatan Kualitas pada Kategori Penjualan Tinggi
Kategori bed_bath_table adalah penyumbang pendapatan terbesar , namun memiliki skor review terendah (3.91) di antara 5 kategori utama. Perusahaan perlu melakukan investigasi terhadap kualitas produk atau proses pengiriman pada kategori ini agar skor kepuasan meningkat, sehingga dapat mempertahankan pangsa pasar.  

Strategi Promosi Tersegmentasi
Produk dengan volume dan berat yang lebih besar terbukti memiliki revenue yang lebih dominan. Perusahaan dapat memfokuskan kampanye pemasaran atau bundling pada produk-produk di kategori health_beauty (yang memiliki skor kepuasan tinggi) untuk menarik lebih banyak pembeli loyal, mengingat kategori ini memiliki performa yang sangat seimbang antara pendapatan dan kepuasan konsumen.


Logistic & Delivery

Meskipun 92.08% pengiriman tepat waktu, terdapat 8% tingkat keterlambatan yang cukup signifikan. Analisis tren menunjukkan adanya lonjakan keterlambatan pada periode tertentu (awal 2018). Selain itu, terdapat variasi waktu transit yang tinggi antar wilayah (negara bagian).

Audit Vendor

Perusahaan perlu mengevaluasi kinerja kurir atau mitra logistik di wilayah dengan waktu transit tinggi (seperti AM atau wilayah luar SP).

Prediksi Keterlambatan

Implementasikan sistem early warning berdasarkan data historis untuk memprediksi pesanan mana yang berisiko terlambat, sehingga tim operasional bisa mengambil tindakan preventif sebelum pengiriman dilakukan.


Customers & Payment Behavior


Metode pembayaran kartu kredit (credit_card) merupakan penggerak utama bisnis dengan kontribusi $15.07 juta atau 76.83% dari total pendapatan.
Terdapat tren di mana pelanggan cenderung memilih skema cicilan untuk produk dengan harga lebih tinggi. Mayoritas transaksi (hampir 50% dari total transaksi) dilakukan dengan 1 kali cicilan, namun volume transaksi dengan 2 hingga 10 cicilan juga cukup signifikan untuk menjaga daya beli pelanggan pada produk mahal.
Negara bagian SP (São Paulo) adalah pusat ekonomi utama, dengan kontribusi pembayaran terbesar secara absolut. Ini menunjukkan bahwa kekuatan logistik dan pasar terkonsentrasi di wilayah tersebut.
Terdapat ketimpangan yang jauh antara wilayah SP dengan wilayah lain (seperti MG, RJ, SC, PR). Wilayah di luar SP memiliki volume pembayaran yang jauh lebih kecil, yang kemungkinan berkorelasi dengan biaya logistik yang lebih mahal atau waktu pengiriman yang lebih lama.

Solusi Strategis

Optimalisasi Payment Gateway
Tawarkan program promosi khusus (diskon atau cashback) bagi pengguna kartu kredit dari bank tertentu untuk menjaga Customer Lifetime Value (CLV).
Lakukan analisis cost-benefit. Jika biaya logistik ke wilayah seperti MG atau RJ bisa ditekan (misalnya dengan membuka micro-fulfillment center atau gudang kecil di sana), maka perusahaan bisa menawarkan harga pengiriman yang lebih kompetitif untuk menarik lebih banyak pembeli di wilayah tersebut.
Perusahaan dapat membuat fitur "Recommended Installment Plan" di halaman checkout secara otomatis berdasarkan kategori produk, untuk mengurangi hambatan bagi pelanggan dalam menyelesaikan pembelian barang bernilai tinggi (high-ticket items)

Seller Performance

Negara bagian SP (São Paulo) adalah penyumbang pendapatan terbesar yang sangat dominan. Jika dilihat dari data, sebagian besar nilai transaksi (pembayaran) terjadi di wilayah ini
Pada chart donut dapat dilihat beberapa negara bagian yang memiliki nilai review tertinggi. Hal ini menunjukan bahwa hal hal yang berkaitan dengan kepuasan konsumen seperti kualitas produk, tingkat keterlambatan dan lainya dari negara tersebut lebih baik dari pada rata rata negara bagian dengan kontribusi pendapatan paling besar.


Tools & Technologies

Data Processing : Python / Jupyter Notebook
Data visualization : Power BI
Analysis Areas: Sales Performance, Logistic Management, Customer Segmentation, Payment Analysis.