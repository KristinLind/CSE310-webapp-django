# Overview

As a software engineer, I wanted to take the Client & Project Tracker I've been building over the last two modules and turn it into something a person could actually use in a web browser. I first wrote it as a Kotlin console program, then rebuilt it in Python and connected it to Firebase Firestore so the data would persist. For this module I put a Django web app on top of that same Firestore database. I've worked with React before, but this is my first time using Django, so I wanted to learn how a server-side framework takes a request from the browser, runs Python code, and builds a page to send back.

The web app lets you see all of your clients and projects on a dashboard, add a new client and project, open a client to view its details, update a project's status, and delete a client you no longer need. Every page is built from live data in Firestore, so anything you add or change is still there the next time you open the app.

To run it on your own computer:

1. Create and activate a virtual environment: `python3 -m venv venv` then `source venv/bin/activate`
2. Install the packages: `pip install -r requirements.txt`
3. Add a Firebase Service Account key (`.json` file) to the top-level project folder and update the credential filename in `client_tracker/views.py` if necessary. The service account key is excluded from the public repository through `.gitignore` because it grants access to the database.
4. Start the test server: `python manage.py runserver`
5. Open a browser and go to `http://127.0.0.1:8000/` to see the dashboard.

I wanted to build this to see how Django organizes a web app into URLs, views, and templates, and to bring my last two modules together into one working app that feels like a real tool instead of a menu in the terminal.

[Software Demo Video](https://us06web.zoom.us/rec/play/wdCACAZjA5H8iXnvypI-gfi_rKQMJDQrqA8ChIHjhhwXbF4qTQh4vUbKXGxZwW3OpDbUmcKEWM8ucWSC.s3a89hkoCeW21OFR?accessLevel=meeting&canPlayFromShare=true&from=share_recording_detail&continueMode=true&oldStyle=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fus06web.zoom.us%2Frec%2Fshare%2FWJ2pWR2An5lsu5VPmnLKtTLLj1Q9j4WvDgv9RhjSIN-j2bsKuHWPLKvA6hsmkUat.6vXsR6EYMYNfhHAB)

# Web Pages

- **Dashboard** (`/`) — The home page. The view reads every document in my Firestore "clients" collection and lists each client's name, project, and status. Each client name is a link to its detail page, and the "+ Add Client & Project" button opens the Add page. If nothing has been added yet, it shows a message instead.

- **Add Client & Project** (`/add/`) — A form where you enter the client name and project name and pick a starting status. When you submit, the new document is saved to Firestore and you're sent back to the Dashboard, where it now shows up.

- **Client Details** (`/client/<id>/`) — Built from the one Firestore document you clicked on. It shows the client's name, project, and status, with links to update the status, delete the client, or go back to the Dashboard. In my Module 2 console version, you had to copy a long document ID to pick a record. Now you just click the name.

- **Update Project Status** (`/client/<id>/update/`) — Shows the current information and a drop-down to choose a new status. After you submit, the status is updated in Firestore and you're taken back to the Client Details page showing the change.

- **Delete Client & Project** (`/client/<id>/delete/`) — Asks you to confirm before anything is removed. Clicking "Yes, Delete" removes the document from Firestore and returns you to the Dashboard, or you can cancel and go back to the client.

# Development Environment

I used Visual Studio Code as my code editor and the VS Code terminal to run the Django test server. I used Git and GitHub for version control and the Firebase console to check my data.

I wrote the software in Python using the Django web framework, with HTML templates and a CSS stylesheet for the pages. I used the firebase-admin library to connect Django to my Firestore database.

# Useful Websites

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial: Writing your first Django app](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [YouTube Django Tutorial: Build a Full Python Web App from Scratch](https://www.youtube.com/watch?v=l0QEGvAX8rU)
- [firebase-admin Python SDK Documentation](https://firebase.google.com/docs/reference/admin/python)
- [Firebase Firestore Documentation](https://firebase.google.com/docs/firestore)

# Future Work

- Let you edit the client name and project name, not only the status
- Restructure the data so multiple projects can be grouped under a single client instead of each project being its own unlinked document
- Add a search or filter on the dashboard to show only projects with a certain status
- Add user login so each person only sees their own clients