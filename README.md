# Job Portal Application

A Django-based platform for managing job postings, featuring user accounts, company profiles, and job listings.

---

## Main Features
- **User Accounts**: Sign up, log in, and log out functionality.  
- **Company Profiles**: Create, update, and manage company information.  
- **Job Listings**: Add, edit, and remove job postings.  
- **Pagination**: Easy navigation through job listings with paginated views.

---

## Quick Start Guide

### Step 1: Clone the Project
```bash
git clone https://github.com/kashishGadhiya-aub/Job_Portal
cd job_portal
```

### Step 2: Set Up a Virtual Environment (Optional)
```bash
# Create a virtual environment
python -m venv .venv

# Activate the environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### Step 3: Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### Step 4: Set Up the Database
The project uses SQLite by default. To configure a custom database, update the settings in `job_portal/settings.py`.

Run the following commands to set up the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create an Admin User
Set up a superuser account for admin access:
```bash
python manage.py createsuperuser
```

### Step 6: Run the Application
Start the development server:
```bash
python manage.py runserver
```

Open your browser and visit: `http://127.0.0.1:8000/`.

---

