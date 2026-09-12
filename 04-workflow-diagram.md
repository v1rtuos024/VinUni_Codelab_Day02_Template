> **Mô tả:** Dưới đây là sơ đồ trực quan hóa quy trình vận hành hiện tại (Current-State) của việc tìm kiếm trạm sạc trên xe điện VinFast, làm nổi bật các điểm chuyển giao (Handoff) và điểm nghẽn cổ chai (Bottleneck).

## 1. Sơ đồ quy trình (Text-based ASCII)

```text
  [Hệ thống Xe VinFast]             [Tài xế]                    [App Bản Đồ / V-Green]
           │                           │                                  │
           │ Bước 1: Pin thấp (<20%)   │                                  │
           │ Cảnh báo trên màn hình    │                                  │
           ├──────────────────────────>│                                  │
           │        🔄 Handoff         │ Bước 2: Thao tác mở bản đồ       │
           │        (⏱ 1 phút)         │ Tìm kiếm từ khóa "Trạm sạc"      │
           │                           ├─────────────────────────────────>│
           │                           │            🔄 Handoff            │
           │                           │            (⏱ 2 phút)            │
           │                           │                                  │
           │                           │ Bước 3: Rà soát thông tin        │
           │                           │ 🔴 BOTTLENECK                    │
           │                           │<─────────────────────────────────┤
           │                           │ - Nhấp vào từng trạm gần nhất.   │
           │                           │ - Rà soát xem loại cổng sạc có   │
           │                           │   phù hợp không (CCS2 hay GBT).  │
           │                           │ - Kiểm tra số lượng trụ trống.   │
           │                           │   (⏱ 5 phút - Gây mất an toàn)   │
           │                           │                                  │
           │ Bước 4: Chốt lộ trình     │                                  │
           │ Bắt đầu điều hướng        │                                  │
           │<──────────────────────────┤                                  │
           │        🔄 Handoff         │                                  │
           │        (⏱ 1 phút)         │                                  │
           ▼                           ▼                                  ▼

⏳ TỔNG THỜI GIAN: ~9 - 10 phút / lượt tìm kiếm trạm sạc.