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