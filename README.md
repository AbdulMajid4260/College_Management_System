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


![Home-page](assets/Home-page1.png)

![image](assets/Home_page2.png)

User Registration

![image](assets/Register_page.png)

User Login

![image](assets/Login_page.png)

Contact Page

![image](assets/Contactus_page.png)

Admin Home Page

![image](assets/Admin_Homepage1.png)
![image](assets/Admin_Homepage2.png)


Staff Home Page
![image](assets/Staff_Homepage1.png)

Student Home Page
![image](assets/Student_Homepage.png)

Add Course Page
![image](assets/Add_Coursepage.png)

Add Student Page
![image](assets/Add_Studentpage.png)

Add Staff Page
![image](assets/Add_Staffpage.png)

Add Subject Page
![image](assets/Add_Subjectpage.png)

Staff Take Attendance Page
![image](assets/Staff_Take_attendancepage.png)

Staff View and Update Attendance Page
![image](assets/Staff_View_attendancepage.png)

Staff Apply for Leave
![image](assets/Staff_ApplyLeavepage.png)

Student View Attendance Form
![image](assets/Student_ViewAttendacepage.png)

Student Apply for Leave
![image](assets/Student_ApplyLeavepage.png)

Student Send Feedback Message
![image](assets/Student_Feedbackpage.png)

Add Student Results From Staff Panel
![image](https://user-images.githubusercontent.com/52338664/131296269-0066e46d-7581-4a81-8d72-40ac8c5a2bf3.png)


