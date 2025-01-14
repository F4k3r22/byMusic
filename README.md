<h1 align="center">byMusic</h1>

<div align="center">
  <img src="Image/bymusiclogo.png" alt="byMusic Logo" width="200"/>
</div>

<h2 align="center">byMusic - Spotify Clone with Python</h2>

In this project we will build a Spotify clone step by step using Python. You will learn how to create a music streaming application from scratch, including:

- Functional music player

- Spotify-like user interface

- Music library system

- User management

### 🏠 Personal Use and Self-Hosting:
The code will be available for personal and educational use.

### 💼 Commercial License:
If you want to implement it commercially, contact me at: riveraaai200678@gmail.com

## 🛢️ DB
In the future I will add a sql file with the database schema but for now I have only created the 'users' table like this:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(10) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    pno VARCHAR(20) NOT NULL,
    password VARCHAR(255) NOT NULL,
    gender VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```