from flask import Flask, request, jsonify
import subprocess

app = Flask(__bombitup__)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    target_number = request.json.get('number')
    count = request.json.get('count')

    try:
        # Adjust the command according to the actual script and arguments used in BOMBitUP
        command = ["python", "bombitup.py", "-m", target_number, "-s", str(count)]
        subprocess.run(command, check=True)
        return jsonify({"status": "success", "message": f"Sent {count} messages to {target_number}"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
