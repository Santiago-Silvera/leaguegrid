from flask import Flask, send_from_directory, render_template, jsonify
import random
import string

app = Flask(__name__)

@app.route("/")
def serve_html():
    num_rows = 3
    num_col = 3
    grid_data = [[f"" for col in range(num_col)] for row in range(num_rows)]
    top_questions = [random_string() for _ in range(num_col)]  # 3 random top questions
    left_questions = [random_string() for _ in range(num_rows)]  # 3 random left questions
    return render_template('index.html', grid=grid_data, top_questions=top_questions, left_questions=left_questions, zip=zip)

def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

if __name__ == "__main__":
    app.run(debug=True)
