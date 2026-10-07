import os

import firebase_admin
from firebase_admin import credentials, firestore
from django.shortcuts import render, redirect


# Connect Django to Firebase
if not firebase_admin._apps:
    credential_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "clouddatabasetracker-firebase-adminsdk-fbsvc-6a0cee1181.json"
    )

    cred = credentials.Certificate(credential_path)
    firebase_admin.initialize_app(cred)

db = firestore.client()


def dashboard(request):
    """Display all clients and projects stored in Firestore."""

    clients = []

    docs = db.collection("clients").stream()

    for doc in docs:
        data = doc.to_dict()

        clients.append({
            "id": doc.id,
            "name": data.get("client_name"),
            "project": data.get("project_name"),
            "status": data.get("status"),
        })

    return render(
        request,
        "client_tracker/dashboard.html",
        {"clients": clients}
    )


def add_client(request):
    """Add a new client/project to Firestore."""

    if request.method == "POST":
        name = request.POST.get("name")
        project = request.POST.get("project")
        status = request.POST.get("status")

        db.collection("clients").add({
            "client_name": name,
            "project_name": project,
            "status": status
        })

        return redirect("dashboard")

    return render(request, "client_tracker/add_client.html")

