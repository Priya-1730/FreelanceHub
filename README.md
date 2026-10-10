# FreelanceHub — Freelance Marketplace

FreelanceHub is a Django-based web application that connects clients with freelancers. Clients can post projects and review proposals, while freelancers can find opportunities, submit proposals, and deliver their work through a centralized platform.

## 🚀 Features

### 👤 User Authentication
- User registration and login
- Role-based accounts for clients and freelancers
- Profile management

### 📋 Project Management
- Clients can create and manage projects
- Freelancers can browse available projects
- Project details and project listings

### 🤝 Proposal Management
- Freelancers can submit proposals
- Clients can review proposals
- Clients can accept or reject proposals

### 💻 Work Submission
- Freelancers can submit completed work
- Delivery messages and optional GitHub or live-project links
- Clients can review submitted work
- Project completion status management

### ⭐ Additional Features
- Freelancer profiles and skills
- Client and freelancer dashboards
- Review and feedback functionality
- Responsive interface using Bootstrap and custom CSS

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| MySQL | Database |
| HTML5 | Page structure |
| CSS3 | Styling |
| Bootstrap 5 | Responsive user interface |
| JavaScript | Frontend interactions |
| Git & GitHub | Version control and source code hosting |

## 📁 Project Structure

```text
FreelanceHub/
├── Django/                 # Django project configuration
├── accounts/               # Authentication and user profiles
├── projects/               # Project and proposal management
├── templates/              # HTML templates
│   ├── accounts/
│   └── projects/
├── static/
│   ├── css/
│   └── images/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### Prerequisites

- Python
- MySQL Server
- Git
- pip

### 1. Clone the repository

```bash
git clone https://github.com/Priya-1730/FreelanceHub.git
cd FreelanceHub
```

### 2. Create and activate a virtual environment

**Windows:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database

Create a MySQL database named `freelancehub`.

Configure your database credentials and Django secret key using environment variables in a local `.env` file. Refer to your Django settings for the required variable names.

**Never commit your `.env` file or private credentials to GitHub.**

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser:

http://127.0.0.1:8000/

## 🎯 Project Objective

The goal of FreelanceHub is to simplify collaboration between clients and freelancers by providing a structured workflow for project posting, proposal management, work delivery, and project completion.

## 🔮 Future Enhancements

- Online payment integration
- Real-time notifications and messaging
- Advanced project search and filtering
- Automated testing and deployment
- Enhanced security and production deployment

## 👩‍💻 Developer

**Priya Varshini G**

GitHub: [Priya-1730](https://github.com/Priya-1730)

Project Repository: [FreelanceHub](https://github.com/Priya-1730/FreelanceHub)

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.