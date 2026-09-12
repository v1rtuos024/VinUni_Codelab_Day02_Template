# 01 — Problem Scan & Quick Problem Cards

## Bối cảnh và giả định

Tôi đóng vai AI Product Engineer tại Vin Smart Future. Các con số dưới đây là baseline giả định để scoping trong lab; khi triển khai cần lấy log thật từ hệ thống vận hành và phỏng vấn điều phối viên.

## Phase 1 — SCAN

| # | Công ty | Lens | Bài toán và dấu hiệu đau |
|---:|---|---|---|
| 1 | Xanh SM | Tốn thời gian | Điều phối viên đọc cuộc gọi/ghi chú sự cố pin, hỏi lại vị trí rồi tạo phiếu cứu hộ; mất khoảng 15–20 phút mỗi lượt. |
| 2 | Xanh SM | Lặp lại | Gom và phân loại lý do khách hủy chuyến từ ghi chú tài xế để tìm 10 nguyên nhân chính; mỗi tuần mất 6–8 giờ. |
| 3 | VinFast | Lặp lại | Đối chiếu hóa đơn điện và dữ liệu phiên sạc từ nhiều trạm đối tác; khoảng 2.000 dòng/tuần cần kiểm tra thủ công. |
| 4 | Vinhomes | AI-upgrade | Phân loại phản ánh cư dân (mất nước, thang máy, tiếng ồn) và chuyển đúng ban quản lý; ticket bị route sai khoảng 12% theo baseline giả định. |
| 5 | Vinmec | Tốn thời gian | Bác sĩ trích xuất thông tin từ bệnh án, xét nghiệm để soạn tóm tắt xuất viện; mất 20–30 phút/bệnh nhân. Bản nháp luôn phải do bác sĩ duyệt. |
| 6 | Vinpearl | Pain từ người khác | Tổng hợp review đa kênh, phát hiện phàn nàn khẩn cấp về vệ sinh/an toàn và chuyển quản lý ca trực; hiện xử lý theo ca thủ công. |

## Phase 2 — QUICK-ASSESS

### Card #1 — Xanh SM: hỗ trợ sự cố pin trên đường

- **Bài toán:** Điều phối viên mất 15–20 phút để hiểu sự cố và tạo hướng xử lý từ cuộc gọi/ghi chú không có cấu trúc.
- **Actor:** Điều phối viên trung tâm; tài xế là người cung cấp thông tin.
- **Workflow hiện tại:** (1) nhận cuộc gọi → (2) ghi chú thủ công và hỏi vị trí/pin → (3) tra bản đồ/trạm → (4) gọi lại, tạo phiếu cứu hộ.
- **Bottleneck:** Bước 2–3, đặc biệt khi pin dưới 5% hoặc dữ liệu thiếu; nhiều handoff giữa tài xế, điều phối viên và đội cứu hộ (15–20 phút/lượt).
- **AI hỗ trợ:** LLM trích xuất ý định, pin, vị trí, mức khẩn cấp và tạo bản nháp phiếu; rule engine kiểm tra ngưỡng pin/khoảng cách.
- **Metric:** thời gian tạo phiếu trung vị 18 → dưới 5 phút; ≥95% phiếu đủ trường; 0 đề xuất trạm >5 km khi pin <5%; tỷ lệ điều phối viên chấp nhận bản nháp ≥85%.
- **Quick architecture:** Rule + LLM feature, có HITL; chưa cần agent tự hành.

### Card #2 — Vinhomes: phân loại và điều hướng phản ánh cư dân

- **Bài toán:** Ticket tiếng Việt tự do bị chuyển nhầm ban, kéo dài thời gian xử lý.
- **Actor:** Nhân viên CSKH và ban quản lý tòa nhà.
- **Workflow hiện tại:** (1) nhận ticket App → (2) đọc và gắn nhãn → (3) chuyển ban xử lý → (4) gọi lại cư dân nếu thiếu thông tin.
- **Bottleneck:** Đọc và phân loại thủ công 3–5 phút/ticket; mô tả tiếng lóng/ảnh đính kèm dễ gây route sai.
- **AI hỗ trợ:** LLM phân loại chủ đề, tóm tắt và nêu trường còn thiếu; rule kiểm tra tòa/ban phụ trách. Nhân viên duyệt trước khi chuyển.
- **Metric:** thời gian route 5 → dưới 1 phút; route đúng ≥90%; tỷ lệ ticket phải hỏi lại giảm 20%; không tự cam kết bồi thường.
- **Quick architecture:** LLM feature + Rule + HITL.

### Card #3 — Vinmec: bản nháp tóm tắt xuất viện

- **Bài toán:** Bác sĩ phải tổng hợp nhiều nguồn dữ liệu để viết tóm tắt dễ hiểu cho bệnh nhân.
- **Actor:** Bác sĩ điều trị; điều dưỡng hỗ trợ kiểm tra hành chính.
- **Workflow hiện tại:** (1) mở bệnh án/xét nghiệm → (2) đọc và sao chép dữ liệu → (3) viết tóm tắt → (4) rà soát, ký duyệt.
- **Bottleneck:** Sao chép và diễn đạt lặp lại 20–30 phút/bệnh nhân; rủi ro bỏ sót dị ứng/thuốc.
- **AI hỗ trợ:** LLM chỉ tạo bản nháp có trích dẫn nguồn; rule kiểm tra trường bắt buộc; bác sĩ duyệt và ký điện tử.
- **Metric:** thời gian soạn 25 → dưới 10 phút; ≥98% trường bắt buộc có nguồn; 100% bản phát hành có chữ ký bác sĩ; 0 chẩn đoán mới do AI tự đưa ra.
- **Quick architecture:** LLM feature + Rule + HITL, fallback về mẫu thủ công.

## Lựa chọn cho Deep-Dive

Chọn **Card #1 — Xanh SM hỗ trợ sự cố pin** vì có workflow quan sát được, metric định lượng rõ và ranh giới an toàn có thể kiểm thử bằng prototype. Card #2 phù hợp giai đoạn sau; Card #3 có giá trị cao nhưng yêu cầu quản trị dữ liệu y tế và thẩm định lâm sàng rộng hơn.
