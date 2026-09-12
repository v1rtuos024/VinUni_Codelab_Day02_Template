# 🏗️ Phase 3 — DEEP-DIVE

## 3.1. Current-State Workflow Mapping
Quy trình tìm kiếm trạm sạc hiện tại của tài xế xe điện VinFast khi có cảnh báo pin thấp:

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Xe báo pin   │     │ Mở bản đồ/   │     │ Kiểm tra thủ │     │ Lựa chọn &   │
│ thấp (<20%)  │ ──→ │ Tìm kiếm trạm│ ──→ │ công loại cổng│ ──→│ Bắt đầu      │
│              │     │ sạc gần nhất │     │ và trụ trống │     │ điều hướng   │
│ Ai: Tài xế   │     │ Ai: Tài xế   │     │ Ai: Tài xế   │     │ Ai: Tài xế   │
│ ⏱ 1 phút    │     │ ⏱ 2 phút     │     │ ⏱ 5 phút 🔴 │    │ ⏱ 1 phút    │
│ In: Cảnh báo │     │ In: GPS      │     │ In: App info │     │ Out: Lộ trình│
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
🔴 = Bottlenecks (Bước 3 tốn nhiều thời gian nhất, gây phân tâm khi lái xe và dễ chọn nhầm trạm hỏng/kín chỗ).
⏱ Tổng thời gian thao tác: ~9-10 phút.
```

## 3.2. Problem Statement (6-field) & Metrics

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Khách hàng lái xe điện VinFast (Tài xế). |
| **2. Current Workflow** | Khi xe báo pin thấp, tài xế phải thao tác thủ công trên màn hình xe hoặc app điện thoại để tìm trạm, tự nhấp vào từng trạm để xem số lượng trụ còn trống và tự đánh giá xem loại cổng sạc (CCS2/GBT) ở trạm đó có phù hợp với xe mình không trước khi khởi hành. |
| **3. Bottleneck** | Bước rà soát thủ công để đối chiếu 3 yếu tố: "Trạm gần nhất" + "Có trụ trống thực tế" + "Đúng chuẩn cổng sạc của xe" mất rất nhiều thời gian và gây mất an toàn khi tài xế đang thao tác lúc lái xe. |
| **4. Business Impact** | Gây ra "Range Anxiety" (nỗi lo hết pin) và trải nghiệm người dùng kém. Tăng nguy cơ xe sập nguồn giữa đường nếu tài xế điều hướng đến trạm không phù hợp hoặc đã full xe, dẫn đến phàn nàn trên các cộng đồng người dùng VinFast. |
| **5. Success Metric** | 1. Giảm thời gian tìm và chốt trạm sạc từ 10 phút xuống < 30 giây.<br>2. Tỷ lệ đề xuất đúng trạm sạc có cổng tương thích đạt 100%.<br>3. Tỷ lệ điều hướng đến trạm còn ít nhất 1 trụ trống lúc xe đến nơi đạt >90%. |
| **6. Operational Boundary** | AI **được phép** truy cập dữ liệu % pin hiện tại, tọa độ GPS của xe, loại xe, và API trạng thái trạm sạc V-Green. <br>**TUYỆT ĐỐI KHÔNG ĐƯỢC:** Tự động lái xe đổi hướng mà không có sự đồng ý của tài xế; Không được đề xuất trạm vượt quá quãng đường khả dụng của % pin hiện tại (Nếu pin <5%, phải bắt buộc đề xuất gọi Dịch vụ sạc pin lưu động 24/7). |

## 3.3. Future-State Flow & AI Fit
* **Xác định mức AI Fit:** Giải pháp thuộc nhóm **LLM Feature kết hợp Rule-based** (Rule để lọc cứng loại cổng sạc và khoảng cách; LLM để giao tiếp giọng nói tự nhiên, phân tích ngữ cảnh người dùng như: "Tìm trạm sạc nhanh nào có quán cafe gần đây").
* **Vẽ Future-State Flow:**

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Kích hoạt ra │     │ 🔵 AI Step:  │     │ 🟢 HITL:     │     │ Xe tự động   │
│ lệnh tìm trạm│ ──→ │ Auto-lọc trạm│ ──→ │ Tài xế xác   │ ──→ │ thiết lập lộ │
│ sạc bằng     │     │ & Draft đề   │     │ nhận 1 trong │     │ trình tối ưu │
│ giọng nói    │     │ xuất qua TTS │     │ 2 option     │     │              │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                               ↩️ Fallback:
                                                               Nếu API trạm sạc
                                                               offline, AI báo lỗi
                                                               và hiển thị danh 
                                                               sách trạm cơ bản 
                                                               như hệ thống cũ.
```

---

# 🏁 Phase 5 — EVALUATE

### AI Readiness Checklist:
1. [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test? *(Hệ thống VinFast có sẵn API trạng thái trạm sạc V-Green real-time và thông số telemetry của xe).*
2. [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)? *(Có, tài xế là người ra quyết định bấm/nói "Đồng ý" để chốt lộ trình).*
3. [x] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ? *(Hoàn toàn sẵn sàng vì nâng cấp trợ lý ảo ViVi là mục tiêu trọng tâm tăng tính cạnh tranh cho xe VinFast).*

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
[x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp (Test trước trên dòng xe VF8 tại khu vực Hà Nội).
[ ] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline):** Trì hoãn để chuẩn bị thêm.
[ ] **NO-GO (Không khả thi / Rule-based tốt hơn):** Hủy bỏ dự án AI này.

**Justification (Lý giải quyết định):**
Dự án được đánh giá đạt mức độ **GO** vì tính khả thi về mặt dữ liệu rất cao (dữ liệu phần cứng và API trạm sạc đều thuộc hệ sinh thái khép kín của Vingroup). Việc tích hợp LLM Feature giúp trợ lý ảo trên xe giải quyết triệt để nỗi lo lớn nhất của người dùng xe điện là "Tìm trạm sạc", tiết kiệm đáng kể thời gian thao tác thủ công, đảm bảo an toàn giao thông và nâng tầm trải nghiệm lái xe thông minh đúng với định hướng của Vin Smart Future.