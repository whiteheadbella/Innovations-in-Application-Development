# Innovations-in-Application-Development
End-to-End Application Development

Whitehead, Bella P.
USN 22016652210
ITE6200 - Application Development and Emerging Technologies

#Employee Management System

#Full Documentation
📌 Project Overview
Employee Management System is a Django-based web application that enables organizations to manage employee records with ease. The system provides essential CRUD operations, user authentication, and integrates a conversational chatbot assistant using Google Dialogflow.
🚀 Features
#Employee Registration: Add new employees with name, email, and password.
#Update Employee Details: Modify existing employee information.
#Delete Employee: Remove employee records when necessary.
#View Employee List: Display all employees in a structured, tabular format.
#User Authentication: Secure login and logout for authorized access.
#Modern UI: Built with Bootstrap for responsive design.
#Integrated Chatbot: Virtual assistant powered by Dialogflow for quick help.

#Tech Stack
#Layer	Technology
#Backend	Django (Python)
#Frontend	HTML, CSS, Bootstrap
#Database	MySQL (via XAMPP's phpMyAdmin)
#Chatbot	Dialogflow ES + Dialogflow Messenger

#EmployeeAssistantBot — Chatbot Integration Documentation
#Overview
#EmployeeAssistantBot is a Dialogflow-based chatbot integrated into a Django web application using the #Dialogflow Messenger widget. It enables users to interact with a virtual assistant via a web page hosted #at http://127.0.0.1:8000/chatbot/chatbot/.

#Technologies Used
#Dialogflow ES (Google Cloud-based conversational AI)
#Dialogflow Messenger (Web widget)
#Django (Python web framework)
#HTML/CSS (Basic front-end styling)

Project Structure
📁 File Structure

EmployeeSystem/
│
├── EmployApp/                   # Main app for employeesystem
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   └── app1/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── update.html
│   │       ├── about.html
│   │       ├── services.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│
├── chatbot/                # Chatbot integration app
│   ├── templates/
│   │   └── chatbot/
│   │       └── chatbot.html
│   ├── views.py
│   ├── urls.py
│
├── EmployeeSystem /
│   ├── settings.py
│   ├── urls.py
├── database.py
├── manage.py
├── README.md
├── requirements.txt


#Task	URL
#Homepage	http://127.0.0.1:8000/
#Admin Panel	http://127.0.0.1:8000/admin
#Chatbot	http://127.0.0.1:8000/chatbot/chatbot/




