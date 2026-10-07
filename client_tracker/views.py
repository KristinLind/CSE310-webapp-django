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

def client_detail(request, client_id):
    """Display one client/project from Firestore."""

    doc_ref = db.collection("clients").document(client_id)
    doc = doc_ref.get()

    if doc.exists:
        data = doc.to_dict()

        client = {
            "id": doc.id,
            "name": data.get("client_name"),
            "project": data.get("project_name"),
            "status": data.get("status"),
        }

        return render(
            request,
            "client_tracker/client_detail.html",
            {"client": client}
        )

    return redirect("dashboard")

def update_client(request, client_id):
    """Update the status of an existing client/project."""

    doc_ref = db.collection("clients").document(client_id)
    doc = doc_ref.get()

    if not doc.exists:
        return redirect("dashboard")

    if request.method == "POST":
        new_status = request.POST.get("status")

        doc_ref.update({
            "status": new_status
        })

        return redirect("client_detail", client_id=client_id)

    data = doc.to_dict()

    client = {
        "id": doc.id,
        "name": data.get("client_name"),
        "project": data.get("project_name"),
        "status": data.get("status"),
    }

    return render(
        request,
        "client_tracker/update_client.html",
        {"client": client}
    )

def delete_client(request, client_id):
    """Delete an existing client/project from Firestore."""

    doc_ref = db.collection("clients").document(client_id)
    doc = doc_ref.get()

    if not doc.exists:
        return redirect("dashboard")

    if request.method == "POST":
        doc_ref.delete()
        return redirect("dashboard")

    data = doc.to_dict()

    client = {
        "id": doc.id,
        "name": data.get("client_name"),
        "project": data.get("project_name"),
        "status": data.get("status"),
    }

    return render(
        request,
        "client_tracker/delete_client.html",
        {"client": client}
    )    