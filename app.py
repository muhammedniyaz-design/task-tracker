from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database for demonstration
tasks = [
    {"id": 1, "title": "Submit Cloud Computing Assignment", "priority": "High", "done": False},
    {"id": 2, "title": "Prepare for Viva Assessment", "priority": "Medium", "done": False}
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    priority = request.form.get('priority', 'Medium')
    if title:
        new_task = {
            "id": len(tasks) + 1,
            "title": title,
            "priority": priority,
            "done": False
        }
        tasks.append(new_task)
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)