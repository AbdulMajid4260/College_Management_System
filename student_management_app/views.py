from django.shortcuts import render,HttpResponse, redirect,HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from .models import CustomUser, Staffs, Students, AdminHOD
from django.contrib import messages
from django.core.exceptions import ValidationError

def home(request):
	return render(request, 'home.html')


def contact(request):
	return render(request, 'contact.html')


def loginUser(request):
	if request.user.is_authenticated:
		if request.user.user_type == CustomUser.STUDENT:
			return redirect('student_home/')
		elif request.user.user_type == CustomUser.STAFF:
			return redirect('staff_home/')
		elif request.user.user_type == CustomUser.HOD:
			return redirect('admin_home/')
	return render(request, 'login.html')

def doLogin(request):
	if request.method != 'POST':
		messages.error(request, "Invalid method")
		return redirect('loginUser')
	
	try:
		email_id = request.POST.get('email', '')
		password = request.POST.get('password', '')

		if not email_id or not password:
			messages.error(request, "Please provide both email and password")
			return render(request, 'login.html')

		# Check if user exists
		try:
			user = CustomUser.objects.get(email=email_id)
		except CustomUser.DoesNotExist:
			messages.error(request, "No account found with this email. Please register first.")
			return render(request, 'login.html')

		# Verify password
		if user.password != password:  # In production, use proper password hashing
			messages.error(request, "Invalid password. Please try again.")
			return render(request, 'login.html')

		login(request, user)

		if user.user_type == CustomUser.STUDENT:
			return redirect('student_home/')
		elif user.user_type == CustomUser.STAFF:
			return redirect('staff_home/')
		elif user.user_type == CustomUser.HOD:
			return redirect('admin_home/')

	except Exception as e:
		messages.error(request, f"An error occurred while logging in. Please try again.")
		return render(request, 'login.html')

	return render(request, 'login.html')

	
def registration(request):
	if request.user.is_authenticated:
		if request.user.user_type == CustomUser.STUDENT:
			return redirect('student_home/')
		elif request.user.user_type == CustomUser.STAFF:
			return redirect('staff_home/')
		elif request.user.user_type == CustomUser.HOD:
			return redirect('admin_home/')
	return render(request, 'registration.html')

def doRegistration(request):
	if request.method != 'POST':
		messages.error(request, "Invalid method")
		return redirect('registration')
	
	try:
		first_name = request.POST.get('first_name', '')
		last_name = request.POST.get('last_name', '')
		email_id = request.POST.get('email', '')
		password = request.POST.get('password', '')
		confirm_password = request.POST.get('confirmPassword', '')

		# Validate required fields
		if not all([first_name, last_name, email_id, password, confirm_password]):
			messages.error(request, "Please fill in all fields")
			return render(request, 'registration.html')
		
		# Validate password match
		if password != confirm_password:
			messages.error(request, "Passwords do not match")
			return render(request, 'registration.html')

		# Validate password length
		if len(password) < 6:
			messages.error(request, "Password must be at least 6 characters long")
			return render(request, 'registration.html')

		# Check if user already exists
		if CustomUser.objects.filter(email=email_id).exists():
			messages.error(request, "An account with this email already exists")
			return render(request, 'registration.html')

		# Validate email format and get user type
		user_type = get_user_type_from_email(email_id)
		if user_type is None:
			messages.error(request, "Please use valid email format: 'name.student@college.com' or 'name.staff@college.com'")
			return render(request, 'registration.html')

		# Create username from email
		username = email_id.split('@')[0].split('.')[0]
		if CustomUser.objects.filter(username=username).exists():
			messages.error(request, "Username already exists. Please use a different email")
			return render(request, 'registration.html')

		# Create user
		user = CustomUser()
		user.username = username
		user.email = email_id
		user.password = password  # In production, use proper password hashing
		user.user_type = user_type
		user.first_name = first_name
		user.last_name = last_name
		user.save()

		# Create specific user type object
		if user_type == CustomUser.STAFF:
			Staffs.objects.create(admin=user)
		elif user_type == CustomUser.STUDENT:
			Students.objects.create(admin=user)
		elif user_type == CustomUser.HOD:
			AdminHOD.objects.create(admin=user)

		messages.success(request, "Account created successfully! Please login.")
		return redirect('loginUser')

	except Exception as e:
		messages.error(request, f"An error occurred while creating your account. Please try again.")
		return render(request, 'registration.html')

	
def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')


def get_user_type_from_email(email_id):
	"""
	Returns CustomUser.user_type corresponding to the given email address
	email_id should be in following format:
	'<username>.<staff|student|hod>@<college_domain>'
	eg.: 'abhishek.staff@jecrc.com'
	"""

	try:
		email_id = email_id.split('@')[0]
		email_user_type = email_id.split('.')[1]
		return CustomUser.EMAIL_TO_USER_TYPE_MAP[email_user_type]
	except:
		return None
