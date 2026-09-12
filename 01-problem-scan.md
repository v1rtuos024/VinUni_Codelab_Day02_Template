# Quét cơ hội AI và ba Quick Problem Cards

Tác giả: chủ nhánh `buiquangvinh` — cần điền họ tên/mã sinh viên trước khi nộp.

## Phạm vi bằng chứng

Bài làm theo bối cảnh giả lập của worksheet. Chưa phỏng vấn nhân viên hay tiếp cận log nội bộ. Mọi thời gian, sản lượng và mục tiêu dưới đây là **giả định thiết kế cần kiểm chứng**, không phải thống kê doanh nghiệp. Tên đơn vị được dùng theo đề bài.

## Phase 1 — SCAN

| # | Đơn vị | Lens | Bài toán cụ thể | Cách xác minh |
|---|---|---|---|---|
| 1 | Xanh SM | Tốn thời gian | Đọc báo cáo pin yếu, kiểm tra thông tin và viết hướng xử lý | Đo thời gian từng bước trên ticket ẩn danh |
| 2 | Vinhomes | AI có thể tốt hơn | Phân loại phản ánh cư dân viết tự do để chuyển đúng đội | So nhãn AI với nhãn do hai nhân viên thống nhất |
| 3 | VinFast | Lặp lại | Đối chiếu mã giao dịch và số tiền hóa đơn sạc | Kiểm tra tỷ lệ khớp bằng rule trước khi xét AI |
| 4 | Vinpearl | Pain từ người khác | Lễ tân đọc nhiều tin nhắn để tổng hợp yêu cầu lưu trú | Phỏng vấn và đo thời gian tổng hợp |
| 5 | Xanh SM | Lặp lại; AI có thể tốt hơn | Gom nhóm lý do hủy chuyến từ ghi chú tự do | Lấy mẫu ẩn danh và kiểm tra độ đồng thuận nhãn |

## Phase 2 — QUICK-ASSESS

### Card 1 — Soạn nháp xử lý báo cáo pin yếu

- **Đơn vị / Actor:** Xanh SM; điều phối viên xử lý thông tin, tài xế chờ phản hồi.
- **Workflow:** nhận báo cáo → xác minh pin/vị trí → tra phương án → soạn và duyệt → liên hệ tài xế/đội hỗ trợ.
- **Bottleneck giả định:** tra cứu 5 phút và soạn/duyệt 4 phút; tổng 15 phút/lượt.
- **AI hỗ trợ:** diễn giải tin nhắn và soạn nháp; không xác nhận trạm trống, gửi tin hoặc điều xe.
- **Metric mục tiêu:** trung vị soạn/duyệt từ 4 xuống ≤2 phút; toàn quy trình từ 15 xuống ≤13 phút nếu các bước khác giữ nguyên; 100% nháp qua người duyệt.
- **Quick Architecture:** Rule + LLM Feature, không dùng Agent.
- **Điều kiện:** nguồn pin đáng tin cậy và người chịu trách nhiệm duyệt; lab mới có dữ liệu giả lập.

### Card 2 — Phân loại phản ánh cư dân

- **Đơn vị / Actor:** Vinhomes; nhân viên CSKH và đội kỹ thuật.
- **Workflow:** nhận tin → đọc nội dung → chọn nhóm → chuyển đội → theo dõi phản hồi.
- **Bottleneck giả định:** đọc/chọn nhóm 4 phút trong tổng 8 phút/lượt.
- **AI hỗ trợ:** gợi ý nhãn điện, nước, vệ sinh hoặc khác; nhân viên duyệt trước khi chuyển.
- **Metric mục tiêu:** trung vị phân loại ≤1 phút; macro-F1 ≥0,90 trên 100 phản ánh đã gán nhãn; không bỏ sót tình huống khẩn cấp trong tập kiểm tra riêng.
- **Quick Architecture:** Rule cho trường dữ liệu rõ ràng; LLM cho văn bản tự do.
- **Ranh giới:** không kết luận trách nhiệm, hứa bồi thường hay quyết định phí; chuyển thủ công khi thiếu dữ liệu.

### Card 3 — Đối chiếu hóa đơn sạc

- **Đơn vị / Actor:** VinFast; nhân viên kế toán đối soát.
- **Workflow:** nhập bảng → chuẩn hóa mã → so khớp tiền → kiểm tra lệch → người phụ trách duyệt.
- **Bottleneck giả định:** so khớp thủ công 3 phút trong tổng 5 phút/hóa đơn.
- **Giải pháp:** join theo mã giao dịch, tính tiền bằng số thập phân; gom ngoại lệ cho người xử lý.
- **Metric mục tiêu:** ≥95% dòng đủ mã khớp tự động; ≤30 giây tính toán cho 1.000 dòng; không tự ghi nhận chênh lệch vào sổ.
- **Quick Architecture:** Rule / No AI; LLM không có lợi thế ở phép đối chiếu xác định.
- **Điều kiện:** thống nhất khóa giao dịch và quy tắc làm tròn; chưa kiểm chứng chất lượng dữ liệu.

## Lựa chọn và phản biện

Chọn Card 1 vì khớp ranh giới pin/draft của starter code, có thể tạo phản ví dụ rõ ràng. Card 2 cần taxonomy thực tế; Card 3 nên giải bằng rule.

Phản biện chi phí: AI không thay thế bước tra trạm 5 phút nên không thể hứa giảm toàn quy trình còn 3 phút. Phản biện ranh giới: ngưỡng 5% là quy tắc **bài lab**, không phải kết luận kỹ thuật về khả năng di chuyển. Phản biện dữ liệu: test tổng hợp không chứng minh hiệu quả kinh doanh; cần baseline thực tế trước pilot.
