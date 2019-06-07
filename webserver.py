import os
from flask import Flask, render_template_string

app = Flask(__name__)


html = """
<html>
<body>
    {% for f in files %}

    <div>{{f}}</div>

    {% endfor %}
</body>
</html>
"""

@app.route("/")
def list_files_in_this_folder():
    dir_listed = os.listdir(os.getcwd())
    return render_template_string(html, files=dir_listed)

if __name__ == "__main__":
    app.run(debug=True)