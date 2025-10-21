from flask import Flask, render_template, jsonify, url_for

app = Flask(__name__)

@app.route('/oshri')
def index():
    return jsonify({
        "available_endpoints": {
            "/": "List all available endpoints",
            "/student/<name>": "Render a page showing student name",
            "/healthz": "Health check endpoint"
        }
    })

@app.route('/student/<name>')
def student(name):
    return render_template('student.html', student_name=name)

@app.route('/healthz')
def healthz():
    return jsonify({
        "status": "healthy",
        "message": "Application is running",
        "version": "1.0.0",
        "timestamp": __import__('datetime').datetime.now().isoformat()
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
