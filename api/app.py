from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    try:
        # Récupérer les données du formulaire
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "No JSON data provided"}), 400
            
        username = data.get("username")
        password = data.get("password")
        
        # Validation des entrées
        if not username or not password:
            return jsonify({"status": "error", "message": "Username and password are required"}), 400
        
        # Connexion à la base de données
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        
        # Corriger la vulnérabilité SQL Injection en utilisant des paramètres
        query = "SELECT * FROM users WHERE username=? AND password=?"
        cursor.execute(query, (username, password))
        
        result = cursor.fetchone()
        
        if result:
            return jsonify({"status": "success", "user": username})
        else:
            return jsonify({"status": "error", "message": "Invalid credentials"}), 401
            
    except Exception as e:
        return jsonify({"status": "error", "message": "Internal server error"}), 500
        
    finally:
        # S'assurer que la connexion est fermée
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    app.run(debug=False)  # Désactiver le mode debug en production