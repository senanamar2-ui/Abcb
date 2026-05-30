import cv2
import requests
import numpy as np

# الرابط الأساسي لمشروعك (تأكد من استبدال المسار الصحيح)
base_url = 'https://raw.githubusercontent.com/senanamar2-ui/اسم_المشروع/main/'

# ترتيب الملفات من 1 إلى 20
file_names = [f"{i}.jpg" for i in range(1, 21)]

def show_images():
    for file_name in file_names:
        image_url = f'{base_url}{file_name}'
        
        response = requests.get(image_url)
        
        if response.status_code == 200:
            image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
            img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
            
            # عرض الصورة
            cv2.imshow('GitHub Image Viewer', img)
            print(f"يتم عرض: {file_name}")
            
            # انتظار ضغطة زر للانتقال للصورة التالية
            cv2.waitKey(0)
        else:
            print(f"خطأ في تحميل الصورة: {file_name}")

    cv2.destroyAllWindows()

if __name__ == "__main__":
    show_images()
