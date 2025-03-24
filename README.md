# VivaSpot API  

VivaSpot API is an open-source RESTful API for managing restaurant orders, menus, and operations. It provides endpoints for order tracking, menu management, and user authentication, making it easy for restaurants to integrate with web or mobile applications.  

## 🚀 Features  
- 📌 **Order Management** – Create, update, and track customer orders.  
- 📋 **Menu Management** – Manage menu items dynamically via API.  
- 👤 **User Authentication** – Secure authentication with role-based access.  
- 📊 **Order Status Updates** – Real-time order tracking for staff and customers.  
- 🔗 **WebSocket Support** – (Planned) Real-time notifications for new orders.  

## 🛠️ Tech Stack  
- **Framework**: Nexios  
- **Database**: PostgreSQL 
- **Authentication**: JWT 
- **Real-time**: WebSockets (Planned)  

## 🔧 Installation  

```bash
# Clone the repository
git clone https://github.com/techwithdunamix/viva-spot.git  
cd viva-spot 

# Install dependencies  
pip install -r requirements.txt  

  

# Start the development server  
uvicorn main:app --reload
