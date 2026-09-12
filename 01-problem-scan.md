# 01 — Problem Scan

## Lab 02: AI Product Scoping — Vin Smart Future

### Chủ đề được chọn
**VinFast Vehicle Issue Triage Assistant**

Hệ thống AI hỗ trợ nhân viên VinFast đọc mô tả lỗi xe bằng tiếng Việt tự nhiên, tóm tắt triệu chứng, phân loại nhóm vấn đề ban đầu và đề xuất nhóm kỹ thuật phù hợp để tiếp tục xử lý.

---

# Phase 1 — SCAN

Sử dụng 4 lenses: **Repetitive**, **Time-consuming**, **AI-upgrade**, **Stakeholder Pain**.

| # | Subsidiary | Lens | Mô tả bài toán |
|---|---|---|---|
| 1 | VinFast | AI-upgrade | Phân loại lỗi xe ban đầu từ mô tả tiếng Việt tự nhiên của khách hàng. |
| 2 | VinFast | Repetitive | Đối chiếu dữ liệu sạc điện với hóa đơn của các đối tác. |
| 3 | Xanh SM | Time-consuming | Điều phối xử lý tài xế gặp sự cố pin hoặc cần tìm trạm sạc. |
| 4 | Vinhomes | Repetitive | Phân loại và điều hướng phản ánh của cư dân đến đúng bộ phận. |
| 5 | Vinpearl | Stakeholder Pain | Tổng hợp và phân loại các review tiêu cực của khách hàng. |

---

# Phase 2 — QUICK-ASSESS

## Quick Problem Card #1 — VinFast Vehicle Issue Triage

**Bài toán:**  
Khách hàng mô tả tình trạng xe bằng ngôn ngữ tự nhiên, nhân viên phải đọc và xác định vấn đề thuộc nhóm kỹ thuật nào.

**Công ty thành viên:** VinFast

**Actor:**  
Nhân viên chăm sóc khách hàng và cố vấn dịch vụ VinFast.

### Workflow thủ công hiện tại

1. Khách hàng gọi hoặc nhắn mô tả tình trạng xe.
2. Nhân viên đọc/nghe mô tả.
3. Nhân viên hỏi thêm một số thông tin.
4. Nhân viên phân loại vấn đề.
5. Chuyển yêu cầu cho bộ phận kỹ thuật phù hợp.

### Bottleneck

Mô tả của khách hàng thường không sử dụng thuật ngữ kỹ thuật.

Ví dụ:

> "Xe đi qua ổ gà thì bánh trước bên trái kêu cụp cụp."

Nhân viên phải tự suy luận xem vấn đề có thể liên quan đến hệ thống treo, bánh xe hay nhóm kiểm tra khác.

**Baseline giả định:** khoảng 5 phút/yêu cầu.

### AI có thể hỗ trợ ở đâu?

LLM có thể:

- Tóm tắt triệu chứng.
- Chuẩn hóa mô tả.
- Phân loại vấn đề vào nhóm kỹ thuật.
- Đề xuất các câu hỏi cần hỏi thêm.

AI không được tự kết luận chính xác xe đang hỏng bộ phận nào.

### Success Metric

- Tối thiểu 90% yêu cầu được route đúng nhóm kỹ thuật.
- Giảm thời gian phân loại ban đầu từ khoảng 5 phút xuống dưới 1 phút.
- 100% trường hợp liên quan đến an toàn phải được con người review.

> Các số liệu trên là target giả định cho prototype, cần được kiểm chứng bằng dữ liệu thực tế.

### Quick Architecture

**LLM Feature + Rule + Human-in-the-loop**

---

## Quick Problem Card #2 — Vinhomes Complaint Routing

**Bài toán:**  
Phân loại phản ánh của cư dân và chuyển đến đúng bộ phận vận hành.

**Công ty thành viên:** Vinhomes

**Actor:**  
Nhân viên CSKH Vinhomes.

### Workflow thủ công hiện tại

1. Cư dân gửi phản ánh.
2. Nhân viên đọc nội dung.
3. Xác định category.
4. Xác định tòa nhà/bộ phận.
5. Chuyển yêu cầu.

### Bottleneck

Nhân viên phải đọc nhiều nội dung tự do như:

- Mất nước.
- Tiếng ồn.
- Vệ sinh.
- Thang máy.
- An ninh.

### AI có thể hỗ trợ ở đâu?

LLM đọc nội dung, tóm tắt và đề xuất category.

### Success Metric

- Tối thiểu 95% phản ánh được route đúng category.
- Thời gian phân loại dưới 30 giây.

### Quick Architecture

**LLM Feature**

---

## Quick Problem Card #3 — Vinpearl Review Analyzer

**Bài toán:**  
Tổng hợp review khách hàng và phát hiện các phản ánh tiêu cực cần xử lý.

**Công ty thành viên:** Vinpearl

**Actor:**  
Manager và bộ phận Customer Experience.

### Workflow thủ công hiện tại

1. Review được đăng trên các nền tảng.
2. Nhân viên đọc review.
3. Phân loại sentiment.
4. Xác định vấn đề.
5. Tổng hợp báo cáo.
6. Gửi manager.

### Bottleneck

Khối lượng review lớn và nội dung không có cấu trúc.

### AI có thể hỗ trợ ở đâu?

LLM có thể:

- Tóm tắt review.
- Phân loại sentiment.
- Trích xuất complaint.
- Nhóm các vấn đề tương tự.

### Success Metric

- Giảm thời gian tổng hợp review.
- Tối thiểu 90% review nghiêm trọng được phát hiện.

### Quick Architecture

**LLM Feature**

---

# Quyết định lựa chọn

Nhóm chọn:

## VinFast Vehicle Issue Triage Assistant

### Lý do lựa chọn

Bài toán có:

- Input ngôn ngữ tự nhiên rõ ràng.
- Tác vụ lặp lại.
- LLM có lợi thế trong việc hiểu các cách diễn đạt đa dạng.
- Workflow có thể giới hạn rõ ràng.
- Có thể kiểm soát rủi ro bằng Human-in-the-loop.

Tuy nhiên đây là lĩnh vực liên quan đến an toàn xe nên AI chỉ được đóng vai trò **triage assistant**, không phải hệ thống chẩn đoán cuối cùng.
