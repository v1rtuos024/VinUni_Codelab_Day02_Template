# 01-problem-scan.md

# 🔍 Phase 1 — SCAN

Dưới đây là danh sách 5 bài toán thực tế được quét qua các hoạt động vận hành của các công ty thành viên Vingroup, tập trung vào những điểm nghẽn và cơ hội nâng cấp bằng AI:

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | VinFast | AI có thể tốt hơn | **Trợ lý hướng dẫn trạm sạc thông minh:** Tự động đề xuất lịch trình sạc tối ưu và trạm sạc trống phù hợp với loại cổng sạc (CCS2/GBT) của từng dòng xe điện (VF5, VF8, VF9). |
| 2 | Xanh SM | Tốn thời gian | **Điều vận thông minh (Smart Dispatching):** Tối ưu hóa điểm đón taxi điện Xanh SM dựa trên phân tích ngôn ngữ tự nhiên từ tin nhắn tài xế và tọa độ GPS thực tế. |
| 3 | VinFast | Lặp lại | **Đối chiếu hóa đơn sạc điện đối tác:** So khớp dữ liệu sạc điện hằng tuần từ hàng nghìn trụ sạc liên kết ngoài với hóa đơn thực tế gửi về hệ thống tài chính. |
| 4 | Vinhomes | Lặp lại | **Phân loại & Điều hướng phản ánh cư dân:** Phân loại tự động các khiếu nại (ví dụ: mất nước, hỏng đèn, ồn ào) gửi qua App Vinhomes Resident đến đúng ban quản lý từng tòa nhà. |
| 5 | Vinmec | Tốn thời gian | **Soạn thảo tóm tắt hồ sơ xuất viện (Discharge Summary):** Trích xuất thông tin lâm sàng từ bệnh án điện tử, xét nghiệm và ghi chú của bác sĩ để soạn thảo bản tóm tắt xuất viện bằng ngôn ngữ dễ hiểu cho bệnh nhân. |

---

# 🃏 Phase 2 — QUICK-ASSESS

Dưới đây là 3 Quick Problem Cards chi tiết cho các bài toán tiềm năng nhất, trong đó Card #1 là bài toán trọng tâm sẽ được nhóm lựa chọn để Deep-Dive:

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1 (Bài toán trọng tâm được chọn)        │
│                                                             │
│ Bài toán (1 câu): Tự động đề xuất lịch trình sạc tối ưu và  │
│ trạm sạc trống phù hợp với loại cổng sạc (CCS2/GBT) của từng│
│ dòng xe điện (VF5, VF8, VF9).                               │
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Khách hàng lái xe VinFast, Nhân viên   │
│ tổng đài hỗ trợ CSKH.                                       │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Xe báo pin thấp, tài xế mở app/bản đồ để tra cứu trạm  │
│      hoặc gọi tổng đài CSKH xin hỗ trợ.                     │
│   ──> 2. Lọc thủ công tìm trạm sạc gần nhất có loại cổng    │
│          tương thích (CCS2 hoặc GBT).                       │
│   ──> 3. Nhấp vào từng trạm để xem số lượng trụ còn trống   │
│          thực tế.                                           │
│   ──> 4. Tài xế quyết định lộ trình, thiết lập map và lái   │
│          xe đến trạm sạc.                                   │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 5-10 phút/   │
│ lượt, dễ xảy ra lỗi định hướng đến trạm hỏng hoặc full xe). │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3 (Hệ thống  │
│ AI tự động check mức pin, loại xe, tình trạng API trạm sạc  │
│ và draft đề xuất lộ trình duy nhất tốt nhất cho xe).        │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? Giảm thời gian tìm và │
│ chọn trạm sạc từ 10 phút ──> dưới 30 giây; Đảm bảo 99% đề   │
│ xuất đúng loại cổng sạc và trụ đang có sẵn.                 │
│                                                             │
│ Quick Architecture: [ ] No AI  [x] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Tối ưu hóa điểm đón taxi điện Xanh SM dựa │
│ trên phân tích ngôn ngữ tự nhiên từ tin nhắn tài xế và tọa  │
│ độ GPS thực tế.                                             │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Tài xế Xanh SM, Khách hàng gọi xe,     │
│ Điều phối viên trung tâm.                                   │
│                                                             │
│ Workflow thủ công hiện tại (3 bước):                        │
│   1. Khách nhắn tin/ghi chú điểm đón cụ thể (VD: "Mình ở    │
│      sảnh B tòa nhà, không phải sảnh A").                   │
│   ──> 2. Tài xế vừa lái xe vừa đọc tin nhắn để tự mường     │
│          tượng/ tra cứu lại điểm đón thực tế trên bản đồ.   │
│   ──> 3. Tài xế phải gọi điện xác nhận lại nếu GPS bị lệch. │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 3-5 phút/    │
│ lượt, gây mất an toàn khi lái xe).                          │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 (Trích xuất từ │
│ khóa địa điểm từ tin nhắn và tự động mapping cập nhật lại   │
│ GPS trên màn hình điều hướng của tài xế).                   │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? Giảm thời gian xác    │
│ nhận lại điểm đón xuống < 1 phút, tỷ lệ đón đúng sảnh/điểm  │
│ đạt trên 95%.                                               │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Trích xuất thông tin lâm sàng từ bệnh án  │
│ điện tử, xét nghiệm và ghi chú của bác sĩ để soạn thảo bản  │
│ tóm tắt xuất viện bằng ngôn ngữ dễ hiểu.                    │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [x] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Bác sĩ (quá tải hành chính), Bệnh nhân │
│ (chờ đợi thủ tục lâu).                                      │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Bác sĩ mở hồ sơ bệnh án của bệnh nhân chuẩn bị xuất    │
│      viện.                                                  │
│   ──> 2. Rà soát lại toàn bộ ghi chú lâm sàng, lịch sử điều │
│          trị, kết quả xét nghiệm trong nhiều ngày.          │
│   ──> 3. Tổng hợp và gõ lại thủ công báo cáo tóm tắt xuất   │
│          viện.                                              │
│   ──> 4. In ấn và giải thích cho bệnh nhân.                 │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 20-30 phút/ │
│ bệnh nhân, phàn nàn vì quá tải)[cite: 3].                   │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3 (Đọc toàn  │
│ bộ dữ liệu thô và tự động draft bản tóm tắt thân thiện).    │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? Giảm thời gian soạn   │
│ thảo từ 30 phút ──> dưới 5 phút (bác sĩ chỉ cần duyệt lại). │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘