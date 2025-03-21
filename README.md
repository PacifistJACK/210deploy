# Career210 - A Modern Job Portal  

Career210 is a **dynamic job portal** that enables employers to list job openings and candidates to apply seamlessly. The platform is built with **Flask, MySQL (Aiven), HTML, Bootstrap**, and is **deployed on Render** for real-time accessibility.  

---

## 🌟 Features  

- **Live Job Listings** – Directly reflects jobs stored in **MySQL Workbench**.  
- **Detailed Job Pages** – Displays **role, responsibilities, requirements, salary, and location**.  
- **Seamless Application Process** – Users can apply for jobs through an **interactive form**.  
- **Real-Time Data Reflection** – Adding/removing jobs in the **MySQL database** updates instantly.  

---

## 📌 How It Works  

### 1️⃣ **Home Page** – [Career210 Home](https://career210.onrender.com/)  
🔹 Displays available jobs dynamically fetched from **MySQL**.  
🔹 Clicking the **"Apply"** button on any job redirects to the job details page.  

📌 **Screenshot:**  
![image](https://github.com/user-attachments/assets/3314283f-d9af-4eeb-940f-3620fb4447e5)


 ![Home Page2](https://media.discordapp.net/attachments/1064562719975542874/1352513167137439744/Screenshot_2025-03-21_104823.png?ex=67de498b&is=67dcf80b&hm=f72c7219232409f71eba1d5f455de85a37ff2960c43bd275470bc4430f8c0ed8&=&format=webp&quality=lossless&width=1730&height=846)

 
### 2️⃣ **Job Details Page** – `/job/<job_id>`  
🔹 Displays **job title, responsibilities, requirements, salary, and location**.  
🔹 Clicking **"Apply Now"** redirects to the application form.  

📌 **Screenshot:**  
![image](https://github.com/user-attachments/assets/e0d8cb11-eb4d-43fe-a2eb-13ca76ef217f)


### 3️⃣ **Application Form** – `/job/<job_id>/application`  
🔹 Users fill in required details (Name, Email, LinkedIn, Experience, etc.).  
🔹 After submission, users are redirected to confirmation.  

📌 **Screenshot:**  
![image](https://github.com/user-attachments/assets/d39ec374-9a75-414c-b21c-8e2388ae6df4)

### 4️⃣ **Application Submission Confirmation** – `/job/<job_id>/submit_application`  
🔹 Displays a message confirming the application submission.  

📌 **Screenshot:**  
![image](https://github.com/user-attachments/assets/f6ae31e0-4bcc-4d2e-afeb-af43a517ada5)
  

---

## 🛠️ Tech Stack  

- **Frontend** – HTML, Bootstrap  
- **Backend** – Flask  
- **Database** – MySQL (Aiven)  
- **Deployment** – Render  

---

## 🚀 Deployment  

Career210 is deployed on **Render**, making it accessible anywhere with real-time updates from **MySQL Workbench**.  

🔹 Live Demo: **[Career210](https://career210.onrender.com/)**  

---
