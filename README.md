# College Management System

A Django-based College Management System that allows for managing students, staff, courses, attendance, and more.

## Setup Instructions

1. Create and activate virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate  # For Windows
source venv/bin/activate  # For Linux/Mac
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Run the development server:
```bash
python manage.py runserver
```

## Access Instructions

### Local Access
- Access the system at: http://127.0.0.1:8000

### Network Access (Multiple Devices)
To access from other devices on the network:
1. Run the server with:
```bash
python manage.py runserver 0.0.0.0:8000
```
2. Access using your computer's IP address: http://YOUR_IP:8000

## User Types and Registration

1. HOD (Head of Department):
- Register with email format: username.hod@college.com
- Example: abdul.hod@college.com

2. Staff:
- Register with email format: username.staff@college.com
- Example: john.staff@college.com

3. Student:
- Register with email format: username.student@college.com
- Example: john.student@college.com

## Features

1. HOD Features:
- Manage courses
- Manage staff
- Manage students
- View and respond to feedback
- Manage leave requests
- View attendance reports

2. Staff Features:
- Take attendance
- Manage leave requests
- Submit feedback
- Add results

3. Student Features:
- View attendance
- Submit leave requests
- Submit feedback
- View results

## Password Reset

If you forget your password:
1. Click on "Forgot Password?" on the login page
2. Enter your registered email address
3. Check your email for password reset instructions
4. Follow the link to set a new password

## Important Notes

1. The system can be accessed simultaneously from multiple browsers and devices
2. For production deployment:
   - Configure proper email settings in settings.py
   - Use a production-grade database
   - Set DEBUG=False
   - Update SECRET_KEY
   - Configure proper security settings

## Requirements

- Django==3.2.6
- django-widget-tweaks==1.4.8
- Pillow==10.2.0

## Security Considerations

1. Default email backend is set to console for development
2. Configure proper email settings for production use
3. Update ALLOWED_HOSTS in settings.py for production
4. Never expose SECRET_KEY in production

## Troubleshooting

1. If student features don't work after registration:
   - Ensure a course exists in the system
   - Ensure a session year exists
   - HOD needs to assign the student to a course

2. If you can't access from other devices:
   - Check if the server is running with 0.0.0.0:8000
   - Verify ALLOWED_HOSTS in settings.py includes your IP
   - Check network firewall settings

# Project Summary
This is a Simple College Management System Developed for Educational Purpose using Python (Django).
# Features of this Website
# A. Admin Users Can
1. See Overall Summary Charts of Students Performance, Staffs Performance, Add/Remove Courses, Add/Remove Subjects, Check/Reply Leave application of staffs/students, Check/reply on feedback bt staffs/students etc.

2. Manage Staffs (Add, Update and Delete)

3. Manage Students (Add, Update and Delete)

4. Manage Course (Add, Update and Delete)

5. Manage Subjects (Add, Update and Delete)

6. Manage Sessions (Add, Update and Delete)

7. View Student Attendance

8. Review and Reply Student/Staff Feedback

9. Review (Approve/Reject) Student/Staff Leave

10. Update Profile

11. Login/Logout

# B. Staff/Teachers Can

1. See the Overall Summary Charts related to their students, their subjects, leave status, etc.

2. Take/Update Students Attendance

3. Add/Update Result

4. Apply for Leave

5. Send Feedback to HOD

6. Update Profile

7. Login/Logout

# C. Students Can

1. See the Overall Summary Charts related to their attendance, their subjects, leave status, etc.

2. View Attendance

3. View Result

4. Apply for Leave

5. Send Feedback to HOD

6. Update Profile

7. Login/Logout

# Tech Stacks

Django, Ajax, Jquery, Bootstrap, Javascript, Python, Owl Carousel, HTML, CSS

# Project Screenshots
Home Page


![image](https://user-images.githubusercontent.com/52338664/131291661-a6723396-4679-41bc-8b86-d8162c78850a.png)

![image](https://user-images.githubusercontent.com/52338664/131291702-3ad64f71-0b52-44fc-8808-92dc7c86e990.png)
![image](https://user-images.githubusercontent.com/52338664/131291718-216869ea-7d8a-45c7-9495-177c23a768a1.png)

User Registration

![image](https://user-images.githubusercontent.com/52338664/131291749-86cdca54-99a4-41f7-b732-38e8bcb22a93.png)

User Login

![image](https://user-images.githubusercontent.com/52338664/131291767-6b732816-e8d9-4a5d-95ec-3719a16cf7c2.png)

Contact Page

![image](https://user-images.githubusercontent.com/52338664/131291786-ae5c6523-b6da-43e2-b5a5-83e08788fc1d.png)

Admin Home Page

![image](https://user-images.githubusercontent.com/52338664/131291810-dd32e8c5-726f-49dc-9d26-cd28d4e2320c.png)

Staff Home Page
![image](https://user-images.githubusercontent.com/52338664/131294155-9654581f-c879-4da1-923f-c03f409eac96.png)

Student Home Page
![image](https://user-images.githubusercontent.com/52338664/131294191-900cfa69-ad58-4756-a5e5-5f3d1b252e20.png)

Add Course Page
![image](https://user-images.githubusercontent.com/52338664/131294244-9d75108b-a615-4cc0-b58a-2267b5115956.png)

Add Student Page
![image](https://user-images.githubusercontent.com/52338664/131294274-cb8f1f74-d5f1-4948-841c-a847f1b538b0.png)

Add Staff Page
![image](https://user-images.githubusercontent.com/52338664/131294312-105abce5-4a97-455a-9b45-6cb9911e63a9.png)

Add Subject Page
![image](https://user-images.githubusercontent.com/52338664/131294324-1efb9010-664d-44db-adb1-aee1e45f7be7.png)

Manage Subject Page
![image](https://user-images.githubusercontent.com/52338664/131294347-00850bc6-0db0-454e-8b6a-07d8bee95306.png)

Manage Course Page
![image](https://user-images.githubusercontent.com/52338664/131294372-95b49964-8e04-4487-882c-4162ccae6d9b.png)

Manage Staff Page
![image](https://user-images.githubusercontent.com/52338664/131294424-434395f3-26ae-4b6b-92ee-c641a1d442d8.png)

Manage Student Page
![image](https://user-images.githubusercontent.com/52338664/131294452-a9dad2ad-4f72-421c-b0ff-06e1fdcf35ab.png)

Staff Take Attendance Page
![image](https://user-images.githubusercontent.com/52338664/131294485-d8fb5c40-4dcc-4adf-b99d-20f0826f9334.png)

Staff View and Update Attendance Page
![image](https://user-images.githubusercontent.com/52338664/131294520-f3b3facb-dc9f-4ec9-b1d8-a3830641b5e2.png)

Session Year Manage
![image](https://user-images.githubusercontent.com/52338664/131294561-82ee4e38-9090-4e24-9d8e-793062fd9312.png)

Staff Apply for Leave
![image](https://user-images.githubusercontent.com/52338664/131294585-adb4b6f7-54cf-47ce-968a-7b046d908c34.png)

Staff Feedback Message
![image](https://user-images.githubusercontent.com/52338664/131294610-f557aa67-4d17-4b7c-a70f-343d9dd1a3ad.png)

Student View Attendance Form
![image](https://user-images.githubusercontent.com/52338664/131294641-d1b947b7-5090-4501-a819-53813cd05fa6.png)

Student View Attendance Data
![image](https://user-images.githubusercontent.com/52338664/131294669-9cc6a910-b8c9-4674-a5e7-cab7208e80b2.png)

Student Apply for Leave
![image](https://user-images.githubusercontent.com/52338664/131294701-3745ff15-b412-480c-9436-3d3a7cfdb223.png)

Student Send Feedback Message
![image](https://user-images.githubusercontent.com/52338664/131294726-36b70a48-ee11-4d4f-a8e6-ef25ae5e1f6f.png)

HOD Reply Student Feedback
![image](https://user-images.githubusercontent.com/52338664/131294748-73a18c2c-d310-4e3e-aa3e-0e8388887a5b.png)

HOD Reply Staff Feedback
![image](https://user-images.githubusercontent.com/52338664/131294760-7895e621-fc6a-45b8-bc3d-6d7d16eca39f.png)

HOD Approve and Disapprove Student Leave
![image](https://user-images.githubusercontent.com/52338664/131294989-d06e948c-8685-4e10-82fc-7a2f1ff80a52.png)

HOD Approve and Disapprove Student Leave
![image](https://user-images.githubusercontent.com/52338664/131295032-3e7a8eda-b372-4c65-be4d-2061c72675bd.png)

HOD Approve and Disapprove Staff Leave
![image](https://user-images.githubusercontent.com/52338664/131295007-ab8995f3-4e8a-4ea0-a2e3-a13d44415865.png)

HOD View Attendance Data
![image](https://user-images.githubusercontent.com/52338664/131296228-c04922dc-243d-4201-b230-f405c7d4902c.png)

Add Student Results From Staff Panel
![image](https://user-images.githubusercontent.com/52338664/131296269-0066e46d-7581-4a81-8d72-40ac8c5a2bf3.png)


