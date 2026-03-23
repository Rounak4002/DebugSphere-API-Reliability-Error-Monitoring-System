# DebugSphere – API Reliability & Error Monitoring System

## Overview
DebugSphere is a lightweight API monitoring and error tracking system designed to help understand backend system behavior in real-world scenarios. It logs API request details such as endpoints, methods, status codes, and timestamps, and displays them through a simple dashboard for easy debugging and analysis.

---

## Features
- Tracks API requests (GET/POST)
- Logs endpoint, request method, status code, and timestamp
- Stores logs in a structured SQLite database
- Simple dashboard to view and analyze logs
- Helps identify failure patterns and debugging points

---

## Tech Stack
- Backend: Python (Flask)
- Database: SQLite
- Frontend: HTML (Jinja Templates)
- Tools: REST APIs

---

## Project Structure
debugsphere/
│── app.py
│── logger.py
│── requirements.txt
│── database.db
│
├── templates/
│ └── dashboard.html
│
├── static/
│ └── style.css

-----
## ⚙️ How It Works
1. API requests are made to the system  
2. Each request is logged with:
   - Endpoint  
   - HTTP method  
   - Status code  
   - Timestamp  
3. Logs are stored in SQLite database  
4. Dashboard displays logs for monitoring and debugging  

---

## How to Run

### 1. Clone the repository
git clone <your-repo-link>
cd debugsphere

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the application
python app.py


---

## Use Case
- Debugging API failures  
- Monitoring backend request flow  
- Understanding system behavior  
- Identifying error patterns  

---

## Future Improvements
- Add authentication system  
- Integrate real-time alerts for failures  
- Enhance dashboard with graphs and analytics  
- Support for multiple services  

---

## Contribution
Contributions are welcome. Feel free to fork and improve the project.

---

## License
This project is open-source and intended for learning purposes.
