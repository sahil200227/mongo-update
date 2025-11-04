from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
import os, datetime

app = Flask(__name__)

@app.route("/api/update", methods=["POST"])
def update_record():
    try:
        client = MongoClient(os.environ["MONGO_URI"])
        db = client["jobcrm"]
        col = db["campaign_recipients"]

        data = request.get_json()
        record_id = ObjectId(data.get("_id"))

        col.update_one(
            {"_id": record_id},
            {"$set": {"status": "sent", "last_sent_at": datetime.datetime.utcnow()}}
        )

        return jsonify({"message": "✅ Record updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
