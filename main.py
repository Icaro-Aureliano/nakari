from app import create_app
from flask import Flask, render_template_string

app = create_app()

@app.route('/')
def list_routes():
    output = []
    for rule in app.url_map.iter_rules():
        if f"{rule}"[-1] == "/" and f"{rule}" not in output and f"{rule}" != "/static/" and f"{rule}" != "/":     
            line = f"<a href='{rule}'>{rule}</a>"
            output.append(line)
    
    return render_template_string('<pre>' + '\n'.join(output) + '</pre>')

if __name__ == "__main__":
    app.run(debug=True)
