from flask import Flask, jsonify, request, render_template
from .tasks import list_tasks, create_task, get_task, update_task, delete_task
from pathlib import Path

def create_app():
    app = Flask(__name__, template_folder=str(Path(__file__).resolve().parents[1] / 'templates'))
    @app.route('/api/tasks', methods=['GET'])
    def api_list():
        tasks = [t.__dict__ for t in list_tasks()]
        return jsonify(tasks)

    @app.route('/api/tasks', methods=['POST'])
    def api_create():
        data = request.get_json() or {}
        title = data.get('title')
        description = data.get('description','')
        if not title:
            return jsonify({'error':'title required'}), 400
        t = create_task(title, description)
        return jsonify(t.__dict__), 201

    @app.route('/api/tasks/<int:task_id>', methods=['GET','PUT','DELETE'])
    def api_task(task_id):
        if request.method == 'GET':
            t = get_task(task_id)
            if not t: return jsonify({'error':'not found'}), 404
            return jsonify(t.__dict__)
        if request.method == 'PUT':
            data = request.get_json() or {}
            t = update_task(task_id, title=data.get('title'), description=data.get('description'), completed=data.get('completed'), priority=data.get('priority'))
            if not t: return jsonify({'error':'not found'}), 404
            return jsonify(t.__dict__)
        if request.method == 'DELETE':
            ok = delete_task(task_id)
            if not ok: return jsonify({'error':'not found'}), 404
            return jsonify({}), 204

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

if __name__ == '__main__':
    create_app().run(debug=True)