# Problem Framing — SmartStore AI
### Enterprise Agentic AI Copilot untuk Otomasi Layanan Pelanggan dan Pengaduan Retur E-Commerce Berbasis RAG

## 1. Profil Organisasi
SmartStore adalah platform e-commerce skala menengah dengan kurang lebih
1.500–2.000 transaksi per hari, menjual produk kebutuhan sehari-hari
(fashion, elektronik ringan, dan perlengkapan rumah tangga). Layanan
pelanggan ditangani lewat kanal chat, dengan alur eskalasi bertingkat:
pemeriksaan otomatis (bot) → verifikasi kebijakan SOP → keputusan
auto-approve atau eskalasi ke agen manusia (Level 1, lalu Level 2 untuk
kasus kompleks).

## 2. Pain Points (Masalah Bisnis)
1. **Volume tinggi keluhan retur/refund berulang** — sekitar 60-70% tiket
   keluhan yang masuk ke tim CS berisi pertanyaan berpola sama: status
   pesanan, syarat retur, estimasi waktu refund. Bila semua tiket ini
   diproses manual oleh agen manusia, waktu tunggu pelanggan membengkak
   dan biaya operasional CS naik signifikan.
2. **Eskalasi tidak konsisten & lambat** — tanpa panduan otomatis, kasus
   sederhana (mis. cek posisi kurir) kadang nyasar ke Human Agent Level 2
   yang seharusnya menangani kasus rumit, sehingga rata-rata waktu
   penyelesaian tiket (*resolution time*) memburuk dan agen senior
   kelebihan beban kerja.
3. **Verifikasi syarat refund manual & rawan human error** — agen harus
   mengecek manual apakah suatu keluhan memenuhi syarat SOP retur
   (batas waktu maksimal 14 hari, kondisi barang masih tersegel, dsb.),
   yang memakan waktu rata-rata 5-10 menit per tiket dan berisiko
   inkonsistensi keputusan antar-agen.
4. **Basis pengetahuan SOP tersebar** — dokumen kebijakan retur, garansi,
   dan FAQ tersimpan terpisah di beberapa file/folder internal sehingga
   agen manusia maupun sistem sulit mengambil jawaban yang akurat dan
   terkini secara cepat.

## 3. Mengapa AI (Enterprise AI Assistant) adalah Solusi yang Tepat
- **Optimasi alur eskalasi** — algoritma pencarian biaya minimum (UCS,
  lihat `src/search.py`) memetakan jalur penyelesaian tiket dengan waktu
  total tercepat, memastikan kasus sederhana selesai di jalur otomatis
  (Bot → Auto-Approve) dan hanya kasus yang memang perlu yang naik ke
  Human Agent.
- **Jawaban SOP yang konsisten & ter-grounded** — pencarian semantik pada
  korpus SOP retur/garansi (ChromaDB RAG, dibangun di Milestone 3)
  memastikan agen AI menjawab berdasarkan dokumen resmi, bukan
  karangan, dan konsisten untuk semua pelanggan.
- **Aksi otomatis, bukan cuma jawaban teks** — lewat Model Context
  Protocol (FastMCP, Milestone 4), agen bisa langsung memanggil fungsi
  bisnis nyata seperti `cek_resi` dan `proses_refund`, bukan sekadar
  memberi instruksi ke pelanggan.
- **Transparansi & keterlacakan** — jejak penalaran (Thought Trace) dan
  sitasi dokumen di dashboard (Milestone 5) memudahkan audit keputusan
  agen, penting untuk kepatuhan dan evaluasi kualitas.

## 4. Batasan Sistem (Scope)
- Domain yang dicakup: status pesanan, pelacakan kurir, verifikasi syarat
  retur/refund, dan eskalasi tiket. Di luar itu (mis. pertanyaan produk
  di luar katalog), agen menolak dengan santun (guardrail, dibangun di
  Milestone 3).
- Sistem adalah *purwarupa*, menggunakan data simulasi/sampel — bukan
  data transaksi pelanggan nyata.
- Lingkungan diasumsikan **deterministic** dan **single-agent** per sesi
  (satu pelanggan ditangani independen dari pelanggan lain), sesuai
  klasifikasi PEAS yang sudah dirumuskan di README.

## 5. Tujuan Proyek
Membangun purwarupa AI Copilot yang: (a) mengoptimalkan alur penyelesaian
tiket lewat baseline search, (b) menjawab pertanyaan SOP retur/garansi
secara ter-grounded dari dokumen resmi, dan (c) mengeksekusi aksi bisnis
nyata (cek resi, proses refund) lewat tool calling — disajikan lewat
dashboard web interaktif dengan jejak penalaran yang transparan.