# Banking Case Manager

A simple **Flask-based web application** for managing banking cases with **full CRUD functionality** (Create, Read, Update, Delete).  

This application is designed to run in a **DevPod workspace** or any containerized Python environment and supports **in-memory storage** for initial testing. The browser interface provides a **friendly table view** with real-time updates.

---

## Features

- **Create new cases**: Add cases with customer name, case type, and description.  
- **Read/list cases**: View all cases in a **browser-friendly table** or as JSON via API.  
- **Update existing cases**: Modify fields and status (OPEN/CLOSED).  
- **Delete cases**: Remove cases entirely from memory.  
- **Color-coded statuses**: OPEN (green) / CLOSED (red).  
- Fully compatible with **DevPod + Docker Desktop**.  

---

### Flow Explanation:

# Browser sends HTTP requests to Flask:
# GET /cases → fetch all cases
# POST /cases → create new case
# PUT /cases/<id> → update case
# DELETE /cases/<id> → delete case
# Flask processes requests and updates in-memory storage.
# Browser table updates dynamically using JavaScript fetch API.
# Status colors: OPEN (green) / CLOSED (red).

# API Endpoints
# Endpoint	Method	Description
# /cases	GET	List all cases
# /cases	POST	Create a new case
# /cases/<id>	GET	Get a specific case
# /cases/<id>	PUT	Update a specific case
# /cases/<id>	DELETE	Delete a specific case
