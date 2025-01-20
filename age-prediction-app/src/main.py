import cv2
from deepface import DeepFace

# Hàm nhận diện gương mặt và dự đoán tuổi từ camera
def detect_and_predict_age_from_camera():
    # Mở camera
    cap = cv2.VideoCapture(0)
    
    # Load mô hình nhận diện gương mặt của OpenCV
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    while True:
        # Đọc frame từ camera
        ret, frame = cap.read()
        if not ret:
            print("Không thể đọc dữ liệu từ camera.")
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Nhận diện gương mặt
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        # Vẽ khung quanh các gương mặt và dự đoán tuổi
        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            
            # Dự đoán tuổi bằng DeepFace
            try:
                analysis = DeepFace.analyze(face, actions=['age'], enforce_detection=False)
                age = analysis[0]['age']  # Truy cập đúng phần tử của kết quả phân tích
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cv2.putText(frame, f"Age: {int(age)}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
            except Exception as e:
                print(f"Lỗi khi dự đoán: {e}")
        
        # Hiển thị kết quả
        cv2.imshow("Camera", frame)
        
        # Nhấn 'q' để thoát
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Giải phóng camera và đóng cửa sổ
    cap.release()
    cv2.destroyAllWindows()

# Chạy hàm nhận diện và dự đoán tuổi từ camera
detect_and_predict_age_from_camera()