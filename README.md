# rental-management-system

to run the repo run command python run.py

RentalManagementSystem/
│
├── app/
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css          # Custom styles
│   │   │
│   │   └── js/
│   │       └── script.js          # Optional JS
│   │
│   ├── templates/
│   │   ├── base.html              # Header + Footer (fixed bottom)
│   │   ├── home.html              # Shows available rentals
│   │   ├── rentals.html           # All rentals list
│   │   ├── add_rental.html        # Add rental form
│   │   ├── edit_rental.html       # Edit rental form
│   │   └── billing.html           # Billing details page
│   │
│   ├── __init__.py                # App & DB initialization
│   ├── models.py                  # Database models (SQLite)
│   └── routes.py                  # Routes (HTML + JSON APIs)
│
├── run.py                         # Start Flask server
├── rental.db                      # SQLite database (auto-created)
└── requirements.txt               # Flask dependencies





✔ Working CRUD with SQLite

✔ Responsive UI with header & footer

✔ Home page shows available rentals only

✔ Billing module

✔ Footer fixed at bottom

✔ Backend now returns JSON (REST API)

✔ JSON verified in browser


-------------------------------------------------------------------
style.css

/* -------- GLOBAL -------- */
body {
    background-color: #f5fbff; /* very light pastel blue */
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

/* -------- NAVBAR -------- */
.navbar {
    background: linear-gradient(90deg, #b8e7e1, #cfe9ff); /* pastel green → blue */
}

.navbar-brand,
.navbar .nav-link {
    color: #033d3d !important;
    font-weight: 600;
}

.navbar .nav-link:hover {
    color: #0a6b6b !important;
}

/* -------- CONTAINER -------- */
.container {
    flex: 1;
}

/* -------- HEADINGS -------- */
h1, h2, h3 {
    color: #055160;
    font-weight: 600;
}

/* -------- CARDS / TABLE -------- */
.card {
    border-radius: 12px;
    background-color: #ffffff;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

/* -------- TABLE -------- */
.table {
    background-color: #ffffff;
    border-radius: 10px;
    overflow: hidden;
}

.table thead {
    background-color: #dff5f2; /* pastel green */
}

.table th {
    color: #055160;
}

.table tbody tr:hover {
    background-color: #f1fbff;
}

/* -------- BUTTONS -------- */
.btn-primary {
    background-color: #9ad0ec;
    border: none;
    color: #033d3d;
}

.btn-primary:hover {
    background-color: #7bbfe0;
}

.btn-success {
    background-color: #9fe0b5;
    border: none;
    color: #034d2c;
}

.btn-success:hover {
    background-color: #7fd3a0;
}

.btn-danger {
    background-color: #f4a7a7;
    border: none;
}

/* -------- FORMS -------- */
.form-control {
    border-radius: 8px;
    border: 1px solid #cfe9ff;
}

.form-control:focus {
    box-shadow: 0 0 0 0.2rem rgba(154, 208, 236, 0.4);
    border-color: #9ad0ec;
}

/* -------- FOOTER -------- */
footer {
    background: linear-gradient(90deg, #cfe9ff, #b8e7e1);
    color: #033d3d;
    text-align: center;
    padding: 15px;
    margin-top: auto;
    font-weight: 500;
}



add_rental.html

{% extends 'base.html' %}
{% block content %}
<h2>Add Rental</h2>
<form method="post">
<input class="form-control mb-2" name="title" placeholder="Title" required>
<input class="form-control mb-2" name="description" placeholder="Description">
<input class="form-control mb-2" name="price" placeholder="Rent Price" required>
<input class="form-control mb-2" name="billing_date" placeholder="Billing Date">
<button class="btn btn-primary">Save</button>
</form>
{% endblock %}

base.html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Rental Management System</title>

  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">

  <style>
    html, body {
      height: 100%;
    }

    body {
      display: flex;
      flex-direction: column;
    }

    .page-content {
      flex: 1;
    }
  </style>
</head>

<body>

<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container">
    <a class="navbar-brand" href="/">Rental Management System</a>
    <button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#nav">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div id="nav" class="collapse navbar-collapse">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item"><a class="nav-link" href="/">Home</a></li>
        <li class="nav-item"><a class="nav-link" href="/rentals">Rentals</a></li>
        <li class="nav-item"><a class="nav-link" href="/add">Add Rental</a></li>
        <li class="nav-item"><a class="nav-link" href="/billing">Billing</a></li>
      </ul>
    </div>
  </div>
</nav>

<!-- MAIN CONTENT -->
<div class="container mt-4 page-content">
  {% block content %}{% endblock %}
</div>

<!-- FOOTER -->
<footer class="bg-dark text-white text-center p-3">
  © 2026 Rental Management System | Developed by 💙 P Suman Patro
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

billing.html

{% extends 'base.html' %}
{% block content %}
<h2>Billing Details</h2>

<table class="table table-striped">
<tr>
    <th>Property</th>
    <th>Rent Amount</th>
    <th>Billing Date</th>
    <th>Status</th>
</tr>

{% for r in rentals %}
<tr>
    <td>{{ r.title }}</td>
    <td>₹ {{ r.rent_price }}</td>
    <td>{{ r.billing_date }}</td>
    <td>{{ r.status }}</td>
</tr>
{% endfor %}
</table>

{% endblock %}

edit_rental.html

{% extends 'base.html' %}
{% block content %}
<h2>Edit Rental</h2>
<form method="post">
<input class="form-control mb-2" name="title" value="{{ rental.title }}">
<input class="form-control mb-2" name="description" value="{{ rental.description }}">
<input class="form-control mb-2" name="price" value="{{ rental.rent_price }}">
<input class="form-control mb-2" name="billing_date" value="{{ rental.billing_date }}">
<select class="form-control mb-2" name="status">
<option>Available</option>
<option>Rented</option>
</select>
<button class="btn btn-success">Update</button>
</form>
{% endblock %}

home.html

{% extends 'base.html' %}
{% block content %}

<h2>Welcome to Rental Management System</h2>
<p>Manage rental properties easily with CRUD operations.</p>

<hr>

<h4>Available Rentals</h4>

{% if rentals %}
<div class="row">
    {% for r in rentals %}
    <div class="col-md-4">
        <div class="card mb-3 shadow-sm">
            <div class="card-body">
                <h5 class="card-title">{{ r.title }}</h5>
                <p class="card-text">{{ r.description }}</p>
                <p><strong>Price:</strong> ₹ {{ r.rent_price }}</p>
                <p><strong>Billing Date:</strong> {{ r.billing_date }}</p>
                <span class="badge bg-success">Available</span>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
{% else %}
<p class="text-muted">No rental items available right now.</p>
{% endif %}

{% endblock %}

rentals.html

{% extends 'base.html' %}
{% block content %}
<h2>Rental List</h2>
<table class="table table-bordered">
<tr>
<th>Title</th><th>Price</th><th>Billing Date</th><th>Status</th><th>Action</th>
</tr>
{% for r in rentals %}
<tr>
<td>{{ r.title }}</td>
<td>{{ r.rent_price }}</td>
<td>{{ r.billing_date }}</td>
<td>{{ r.status }}</td>
<td>
<a href="/edit/{{ r.id }}" class="btn btn-warning btn-sm">Edit</a>
<a href="/delete/{{ r.id }}" class="btn btn-danger btn-sm">Delete</a>
</td>
</tr>
{% endfor %}
</table>
{% endblock %}

script.js
console.log("Rental Management System Loaded");