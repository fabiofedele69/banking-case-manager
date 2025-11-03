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

## Technical Architecture

```mermaid
flowchart TD
    A[Browser (Client)] -->|HTTP Requests: GET / POST / PUT / DELETE| B[Flask App (app.py)]
    B --> C[In-Memory Storage (Python List)]
    B -->|Render Table & Forms| A

    subgraph Browser_View
        A1[Create Case Form]
        A2[Editable Table Rows]
        A3[Update / Close / Delete Buttons]
    end

    A --> Browser_View
    Browser_View --> B
    C --> B
# banking-case-manager
