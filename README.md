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
![Home Page1](![image](https://github.com/user-attachments/assets/ef79193b-1eb6-47ca-a0cd-c1f2c4ec83e3)
)  
 ![Home Page2](https://media.discordapp.net/attachments/1064562719975542874/1352513167137439744/Screenshot_2025-03-21_104823.png?ex=67de498b&is=67dcf80b&hm=f72c7219232409f71eba1d5f455de85a37ff2960c43bd275470bc4430f8c0ed8&=&format=webp&quality=lossless&width=1730&height=846)

 
### 2️⃣ **Job Details Page** – `/job/<job_id>`  
🔹 Displays **job title, responsibilities, requirements, salary, and location**.  
🔹 Clicking **"Apply Now"** redirects to the application form.  

📌 **Screenshot:**  
![Job Details Page]([insert-image-here](https://media.discordapp.net/attachments/1064562719975542874/1352513167539834931/Screenshot_2025-03-21_104855.png?ex=67de498b&is=67dcf80b&hm=f185b8b3863d46ea36dfa8bf8fea4b9a337c739be3e64bfd05888ebfadd00d97&=&format=webp&quality=lossless&width=1730&height=796))  

### 3️⃣ **Application Form** – `/job/<job_id>/application`  
🔹 Users fill in required details (Name, Email, LinkedIn, Experience, etc.).  
🔹 After submission, users are redirected to confirmation.  

📌 **Screenshot:**  
![Application Form]([![image](https://github.com/user-attachments/assets/543f799e-e2c7-42e2-bd54-5f8b920bda03](https://media.discordapp.net/attachments/1064562719975542874/1352513124128788521/Screenshot_2025-03-21_104943.png?ex=67de4981&is=67dcf801&hm=d19256b3d1529d9c8436ad22ba8fc18355f14d317abba11514b7e9c7f10bfd9d&=&format=webp&quality=lossless&width=1744&height=859))
)  

### 4️⃣ **Application Submission Confirmation** – `/job/<job_id>/submit_application`  
🔹 Displays a message confirming the application submission.  

📌 **Screenshot:**  
![Application Submitted]([insert-image-here](https://media.discordapp.net/attachments/1064562719975542874/1352514470957551708/Screenshot_2025-03-21_105914.png?ex=67de4ac2&is=67dcf942&hm=eca39ee3914fcd9d3172e7e40dae96b38ee4597670c9d70401587f7ef1814ab7&=&format=webp&quality=lossless&width=1860&height=853))  

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
