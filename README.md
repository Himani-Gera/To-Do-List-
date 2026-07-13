🌸 To-Do List Web App

This project is a full-stack To-Do List web application built using Python, Flask, MySQL, HTML, and CSS. It allows users to log in, manage daily tasks, track their completion status, and delete completed tasks through a simple and user-friendly interface.

The application follows a smooth workflow: users enter the application through a welcome page, log in with a username, and access an options page where they can either add new tasks or view the current task list. The task list displays a serial number, task name, completion checkbox, and a delete option. Navigation buttons and a logout feature make the application easy to use.

To make the project accessible from any device, it is deployed on Render and uses a cloud-hosted MySQL database on Aiven instead of a local database. Since the free database service becomes inactive after periods of inactivity, an automated monitoring bot periodically accesses the database to keep it active, ensuring the application remains available without requiring manual intervention.

The project also includes Progressive Web App (PWA) functionality using a manifest.json file and a service worker, allowing users to install the application on their phones for a more app-like experience.

 Screenshots
 <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/220ca997-ab2a-4e75-9a76-dfe7a4a01fbc" />
 <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/f768faff-8279-4c9c-83d6-979d68a9becc" />
 <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/ee8468fb-2b50-4a12-babe-c09a0202384d" />
 <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/22cf1fd7-2e32-4198-b2d2-f730e1b80568" />
 <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/70df19ec-e23c-4a9e-8cd4-10da587ffc33" />





 Features

- Welcome page with a custom aesthetic design
- Username-based login
- Add new tasks
- View all tasks in a table
- Mark tasks as completed using checkboxes
- Delete tasks
- Navigation with Back and Logout options
- Cloud-hosted MySQL database
- Deployable on Render
- Installable as a Progressive Web App (PWA)
- Responsive pastel-themed user interface

 Technologies Used

- Python
- Flask
- MySQL
- HTML5
- CSS3
- Render (Deployment)
- Aiven Cloud MySQL
- Progressive Web App (PWA)
- Service Worker
- Manifest JSON
- claude (for pwa flies- manifest.json service-worker.js procfile)
