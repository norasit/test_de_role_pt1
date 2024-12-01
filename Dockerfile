# ใช้ Official Python image ที่เหมาะสม
FROM python:3.9-slim

# ตั้งค่า Working Directory ใน Container
WORKDIR /app

# คัดลอก requirements.txt ไปยัง Container
COPY requirements.txt .

# อัปเกรด pip และติดตั้ง dependencies พร้อมตัวเลือกปิดคำเตือน root user action
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt --root-user-action=ignore

# เปิดพอร์ต 8888 สำหรับ Jupyter Notebook
EXPOSE 8888

# ตั้งค่า Default Command สำหรับรัน Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]
