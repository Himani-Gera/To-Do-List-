🌸 To-Do List Web App

This project is a full-stack To-Do List web application built using Python, Flask, MySQL, HTML, and CSS. It allows users to log in, manage daily tasks, track their completion status, and delete completed tasks through a simple and user-friendly interface.

The application follows a smooth workflow: users enter the application through a welcome page, log in with a username, and access an options page where they can either add new tasks or view the current task list. The task list displays a serial number, task name, completion checkbox, and a delete option. Navigation buttons and a logout feature make the application easy to use.

To make the project accessible from any device, it is deployed on Render and uses a cloud-hosted MySQL database on Aiven instead of a local database. Since the free database service becomes inactive after periods of inactivity, an automated monitoring bot periodically accesses the database to keep it active, ensuring the application remains available without requiring manual intervention.

The project also includes Progressive Web App (PWA) functionality using a manifest.json file and a service worker, allowing users to install the application on their phones for a more app-like experience.

✨ Features

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

🛠️ Technologies Used

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
