# SmartStore AI: Enterprise Agentic AI Copilot untuk Otomasi Layanan Pelanggan dan Pengaduan Retur E-Commerce Berbasis RAG

Proyek ini dikembangkan untuk memenuhi **Tugas 1 (Milestone 1 - W02)** Mata Kuliah *Artificial Intelligence* (1053001), Program Studi Sarjana Sistem Informasi, Institut Teknologi Del.

## 👥 Anggota Kelompok & Pembagian Peran
* **Fredrick Laurensius Aritonang** (NIM:12S24001) - *AI Architect & Model Lead* & *QA, Evaluation & Ethics Lead*
* **Dea Anggreany Hutapea** (NIM:12S24053) - *Data & Knowledge Engineer*
* **Rospika Sarah Yosefin Siregar** (NIM:12S24008) - *Integration & Interface Engineer*

---

## 📌 Deskripsi Ringkas Proyek
SmartStore AI adalah solusi *Enterprise AI Assistant/Copilot* yang merotomasi penanganan kueri pelanggan, pelacakan pesanan, dan verifikasi syarat pengembalian barang (*refund*). Sistem ini memadukan penelusuran alur eskalasi optimal (*Uniform Cost Search* / UCS), pencarian semantik korpus kebijakan toko (ChromaDB RAG), dan eksekusi aksi otomatis via Model Context Protocol (FastMCP).

---

## ⚙️ Spesifikasi Formal PEAS & Sifat Lingkungan

### Formulasi PEAS
* **Performance Measure**: Waktu respon penyelesaian tiket (< 2 menit), akurasi jawaban SOP (> 85%), dan efisiensi biaya/waktu rute eskalasi.
* **Environment**: Basis data transaksi pelanggan, dokumen SOP Kebijakan Retur & Garansi (PDF/TXT), serta graf alur keputusan eskalasi.
* **Actuators**: Antarmuka Gradio Web UI (*chat & thought trace*), pemanggilan fungsi FastMCP (`cek_resi`, `proses_refund`), dan pembaruan status tiket.
* **Sensors**: Teks pesan masukan dari pelanggan, ID Pesanan/Nomor Resi, dan respons data JSON dari API pihak ketiga.

### Klasifikasi Lingkungan Operasional
* **Partially Observable** | **Deterministic** | **Sequential** | **Static** | **Discrete** | **Single-Agent**

---

## 🛠️ Cara Menjalankan Kode (Astral uv)

### Prasyarat
- Python >= 3.10
- Astral `uv` package manager

### Langkah Eksekusi
1. **Clone Repositori**:
   ```bash
   git clone [https://github.com/FredrickAritonang/smartstore-ai-copilot.git](https://github.com/FredrickAritonang/smartstore-ai-copilot.git)
   cd smartstore-ai-copilot