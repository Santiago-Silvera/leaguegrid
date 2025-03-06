from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route("/")
def serve_html():
    grid_data = [[f"" for col in range(3)] for row in range(3)]
    return render_template('index.html', grid=grid_data)

if __name__ == "__main__":
    app.run(debug=True)
