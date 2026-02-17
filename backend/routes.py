# backend/routes.py
import pandas as pd                # ✅ add this
from flask import jsonify, request
from .utils import load_csv

def register_routes(app):
    @app.route("/")
    def home():
        return jsonify({"message": "Brent Oil Dashboard API is running!"})

    @app.route("/api/prices")
    def prices():
        df = load_csv("brent_prices.csv", parse_dates=["Date"])
        start = request.args.get("start")
        end = request.args.get("end")
        if start:
            df = df[df["Date"] >= pd.to_datetime(start)]
        if end:
            df = df[df["Date"] <= pd.to_datetime(end)]
        return df.to_json(orient="records", date_format="iso")

    @app.route("/api/change_points")
    def change_points():
        df = load_csv("change_points.csv", parse_dates=["Date"])
        start = request.args.get("start")
        end = request.args.get("end")
        if start:
            df = df[df["Date"] >= pd.to_datetime(start)]
        if end:
            df = df[df["Date"] <= pd.to_datetime(end)]
        return df.to_json(orient="records", date_format="iso")

    @app.route("/api/events")
    def events():
        df = load_csv("key_oil_market_events.csv", parse_dates=["Date"])
        return df.to_json(orient="records", date_format="iso")
