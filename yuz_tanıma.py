import cv2
print("Kod başladı")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# 2. Kamerayı başlatıyoruz (0 genelde varsayılan kameradır)
cap = cv2.VideoCapture(0)

print("Kamera açılıyor... Kapatmak için 'q' tuşuna basın.")

while True:
    # Kameradan bir kare okuyoruz
    ret, frame = cap.read()
    
    # Görüntüyü gri tonlamaya çeviriyoruz (İşlemeyi hızlandırır)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Yüzleri tespit ediyoruz
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Tespit edilen her yüzün etrafına bir kare çiziyoruz
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(frame, "Insan", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Tespit edilen her yüzün etrafına bir kare çiziyoruz
    for (x, y, w, h) in faces:
        # Yüzün etrafına yeşil kare çiziyoruz
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "Insan", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        
        roi_gray = gray[y:y+h, x:x+w]    # Gri görüntüdeki yüz bölgesi
        roi_color = frame[y:y+h, x:x+w]  # Renkli görüntüdeki yüz bölgesi
        
        # Kırptığımız o yüz bölgesinin içinde gözleri arıyoruz
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        # Bulunan her gözün etrafına mavi bir kare çiziyoruz
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)

    # Sonucu ekranda gösteriyoruz
    cv2.imshow('Sudenaz Görüntü İşleme Projesi', frame)

    # 'q' tuşuna basılırsa döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Her şeyi serbest bırakıyoruz
cap.release()
cv2.destroyAllWindows()
