from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Excel file path on server
EXCEL_FILE = "attendance.xlsx"

@app.route('/attendance')
def attendance():
    try:
        df = pd.read_excel(EXCEL_FILE, sheet_name="july")
        data = df.to_dict(orient='records')
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
