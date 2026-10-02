BSL Employee Portal – Digital Electric Meter Reading System
A Django-based web application designed to digitize the process of employee electric meter reading submission. The system provides secure employee authentication, personalized dashboards, meter-reading submission with image proof, and digital storage of submitted readings.
📌 Project Overview
The BSL Employee Portal is a web-based application developed using Python and Django to provide employees with a centralized platform for submitting and managing their electric meter readings.
Instead of relying on manual/paper-based meter reading submissions, employees can:
- Create an employee account
- Log in securely
- Access a personalized dashboard
- Enter their electric meter reading
- Provide serial and quarter information
- Upload an image of the electric meter
- Select a submission option
- View previously submitted readings
- Track submission dates
- Access the Django administration panel for management
The application uses SQLite for persistent data storage and Django's built-in authentication framework for user management.
✨ Key Features
👤 Employee Authentication
The application provides a complete authentication workflow:
- Employee registration
- Employee login
- Logout functionality
- Password validation
- Session-based authentication
- Login protection for the dashboard
- Django authentication system
Users who are not authenticated cannot directly access the dashboard.
📝 Employee Registration
During registration, users provide:
- Username
- Email address
- BSL Staff Number
- Password
- Password confirmation
The application validates the staff number to ensure that it contains exactly 6 digits.
📊 Personalized Employee Dashboard
After authentication, employees are redirected to their personal dashboard.
The dashboard provides:
- Employee username
- Total number of meter readings
- Latest meter reading
- Account status
- Complete meter-reading history
- Meter images
- Submission dates
- New meter-reading submission form
Each employee sees readings associated with their own account.
⚡ Electric Meter Reading Submission
Employees can submit:
- Serial Number
- Quarter Number
- Meter Reading
- Meter Image
- Submission Option
The meter image is uploaded through Django's file-upload mechanism and stored in the configured media directory.
🖼️ Meter Image Proof
Each meter reading can contain an image of the physical electric meter.
The dashboard displays the uploaded image alongside the corresponding reading.
This provides visual evidence associated with the submitted meter reading.
🗃️ Digital Record Management
Every meter-reading record contains:
User
Serial Number
Quarter Number
Meter Reading
Meter Image
Submission Option
Created Date/Time

This creates a digital history of employee submissions.
🛡️ Admin Panel
The project uses Django's built-in administration framework.
The application provides an /admin/ route that can be used for administrative management after creating a Django superuser.
🏗️ System Architecture
                 ┌─────────────────────┐
                 │      Employee       │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    Web Interface    │
                 │  HTML + CSS + JS    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Django Backend    │
                 │      Python         │
                 └──────────┬──────────┘
                            │
              ┌─────────────┼─────────────┐
              │             │             │
              ▼             ▼             ▼
        Authentication   Meter Data    File Upload
              │             │             │
              └─────────────┼─────────────┘
                            ▼
                 ┌─────────────────────┐
                 │   SQLite Database   │
                 └─────────────────────┘

🛠️ Technology Stack
Backend
- Python
- Django 5.0.6
- Django Authentication
- Django ORM
- Django Forms
- Django Signals
Frontend
- HTML5
- CSS3
- JavaScript
- Django Templates
Database
- SQLite
File Storage
- Django Media Files
- Image uploads
Development Tools
- Python
- Django Development Server
- SQLite
- Git / GitHub
📂 Project Structure
BSL_project/
│
├── manage.py
│
├── db.sqlite3
│
├── BSL_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── electricmeter_reading/
│   │
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── 0002_profile.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   │
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   └── dashboard.html
│   │   │
│   │   └── home/
│   │       └── home.html
│   │
│   ├── static/
│   │   └── css/
│   │       ├── base.css
│   │       ├── home.css
│   │       ├── login.css
│   │       ├── signup.css
│   │       └── style.css
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── signals.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
└── media/
    └── meter_images/

🗄️ Database Models
MeterReading
The MeterReading model stores employee meter submissions.
class MeterReading(models.Model):    user = models.ForeignKey(User, on_delete=models.CASCADE)    slno = models.CharField(max_length=50)    quarterno = models.CharField(max_length=50)    meterreading = models.FloatField()    meterimage = models.ImageField(upload_to='meter_images/')    submit_option = models.CharField(max_length=50)    created_at = models.DateTimeField(auto_now_add=True)


Fields
Field	Description
user	Employee associated with the reading
slno	Meter serial number
quarterno	Quarter number
meterreading	Electric meter reading
meterimage	Uploaded meter image
submit_option	Selected submission option
created_at	Automatic submission timestamp


Profile
The project also defines a profile model associated with Django's User model.
class Profile(models.Model):    user = models.OneToOneField(User, on_delete=models.CASCADE)    staffno = models.CharField(max_length=100)


Django signals are used to automatically create and save a profile when a new user is created.
🔐 Authentication Flow
The authentication workflow is:
Employee
   │
   ▼
Registration
   │
   ├── Username
   ├── Email
   ├── Staff Number
   └── Password
   │
   ▼
Django User Account
   │
   ▼
Login
   │
   ▼
Authenticated Session
   │
   ▼
Employee Dashboard

The dashboard is protected using:
@login_requireddef dashboard_view(request):


Therefore, authentication is required before accessing the employee dashboard.
🔄 Meter Reading Workflow
Login
  │
  ▼
Dashboard
  │
  ▼
Enter Meter Details
  │
  ├── Serial Number
  ├── Quarter Number
  ├── Meter Reading
  ├── Meter Image
  └── Submission Option
  │
  ▼
Django Form Validation
  │
  ▼
Save MeterReading
  │
  ▼
Associate Reading With User
  │
  ▼
Store in SQLite
  │
  ▼
Display in Dashboard

🌐 URL Structure
The project contains the following major routes:
URL	Purpose
/	Home page
/admin/	Django administration
/auth/register/	Employee registration
/auth/login/	Employee login
/auth/logout/	Logout
/auth/dashboard/	Employee dashboard


🎨 Frontend
The project uses Django's template system together with HTML, CSS and JavaScript.
The frontend includes:
- Responsive navigation
- Employee dashboard
- Login page
- Registration page
- Meter submission form
- Reading history table
- Statistics cards
- Image preview
- Mobile navigation
- Alert messages
- Interactive UI elements
The templates use Django's template inheritance system.
For example:
{% extends 'base.html' %}

This allows common components such as the navigation bar and footer to be reused across pages.
📊 Dashboard
The dashboard displays three primary statistics:
Total Readings
Displays the total number of meter readings submitted by the logged-in employee.
Latest Reading
Displays the most recent meter reading available to the user.
Account Status
Displays the current account status.
The dashboard also provides a table containing:
Serial Number
Quarter Number
Meter Reading
Meter Image
Submission Option
Submission Date

🖼️ Image Upload System
The application uses Django's ImageField:
meterimage = models.ImageField(upload_to='meter_images/')


Uploaded images are stored under:
media/meter_images/

The project configures:
MEDIA_URL = '/media/'MEDIA_ROOT = BASE_DIR / 'media'


⚙️ Installation
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/BSL_project.git

cd BSL_project

2. Create a Virtual Environment
Windows
python -m venv venv

Activate it:
venv\Scripts\activate

Linux / macOS
python3 -m venv venv

source venv/bin/activate

3. Install Django
pip install django

If image handling requires Pillow:
pip install pillow

4. Apply Migrations
python manage.py makemigrations

python manage.py migrate

5. Create an Admin Account
python manage.py createsuperuser

Follow the prompts to create the administrator account.
6. Start the Development Server
python manage.py runserver

Open:
http://127.0.0.1:8000/

👨‍💼 Admin Access
Open:
http://127.0.0.1:8000/admin/

Log in using the superuser credentials.
The Django admin interface can be used to manage application data.
🔒 Security Considerations
For a production deployment, the following settings should be changed:
DEBUG = False


A production environment should also:
- Store SECRET_KEY in environment variables
- Configure ALLOWED_HOSTS
- Use HTTPS
- Configure secure cookies
- Configure CSRF protection
- Use a production database
- Restrict uploaded file types and sizes
- Configure production media/static storage
- Remove development credentials and sensitive files from GitHub
🚀 Future Enhancements
Possible improvements include:
🔍 OCR-Based Meter Reading
Automatically extract the meter reading from the uploaded meter image using OCR.
Meter Image
     ↓
OCR
     ↓
Detected Reading
     ↓
Validation
     ↓
Database

📱 Mobile Application
Develop an Android application for employees to submit meter readings directly from their smartphones.
📈 Analytics Dashboard
Add:
- Monthly consumption trends
- Employee submission statistics
- Quarter-wise analysis
- Reading comparisons
- Graphs and charts
🔔 Notifications
Add:
- Submission confirmation
- Reminder notifications
- Admin alerts
- Email notifications
🗄️ Production Database
Replace SQLite with:
- PostgreSQL
- MySQL
for production-scale deployment.
☁️ Cloud Deployment
The application could be deployed using platforms such as:
- AWS
- Azure
- Google Cloud
- Render
- Railway
🧪 Testing
The project contains a Django test module:
electricmeter_reading/tests.py

Additional automated tests can be implemented for:
- User registration
- Login/logout
- Staff number validation
- Meter reading submission
- Image uploads
- Dashboard access
- Unauthorized access
- Database operations
📌 Project Highlights
- Built a Django-based employee portal for digitizing electric meter-reading submissions.
- Implemented user authentication and authorization using Django's authentication framework.
- Developed a personalized dashboard for viewing and managing meter-reading records.
- Implemented image upload functionality for meter-reading verification.
- Used Django ORM and SQLite for persistent data management.
- Created reusable templates using Django Template Inheritance.
- Implemented responsive frontend interfaces using HTML, CSS and JavaScript.
- Used Django signals to automatically create employee profile records.
💻 Technologies
Python
Django 5.0.6
HTML5
CSS3
JavaScript
SQLite
Django ORM
Django Authentication
Django Forms
Django Signals
Git
GitHub

📷 Screenshots
Create a section like this after uploading screenshots to your repository:
## 📷 Screenshots

### Home Page
![Home Page](media/screenshots/home.png)

### Login Page
![Login Page](media/screenshots/login.png)

### Registration Page
![Registration Page](media/screenshots/register.png)

### Employee Dashboard
![Dashboard](media/screenshots/dashboard.png)

### Meter Reading Submission
![Meter Submission](media/screenshots/meter-submission.png)

👨‍💻 Developer
KUMAR ARYAN
B.Tech Computer Science & Engineering
AI & Machine Learning
Areas of Interest
- Artificial Intelligence
- Machine Learning
- Deep Learning
- Python
- Django
- Computer Vision
- Web Development
