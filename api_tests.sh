get_token() {
    curl -X POST http://127.0.0.1:8000/api/token/ \
    -H "Content-Type: application/json" \
    -d '{
      "username": "admin",
      "password": "admin"
    }' | jq
}

# POST /tasks - Cria uma nova tarefa.
create_task() {
    curl -X POST http://127.0.0.1:8000/api/tasks/ \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzMjY2ODM2LCJpYXQiOjE3MjI2NjIwMzYsImp0aSI6IjY1ODVjNmJhZmM5MDRjZGNhZmNjZjUxM2RiMDQ1MDc0IiwidXNlcl9pZCI6Mn0.3pG63VzFzkDFIrKqsqMwEzrmMPGd_LXqQupRZADBgCQ" \
    -d '{
      "title": "Tarefa 4",
      "description": "Descrição da tarefa 4",
      "due_date": "2025-03-03"
    }' | jq
}

# GET /tasks - Retorna a lista de todas as tarefas.
get_tasks() {
    curl -X GET http://127.0.0.1:8000/api/tasks/ \
        -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzMjY2ODM2LCJpYXQiOjE3MjI2NjIwMzYsImp0aSI6IjY1ODVjNmJhZmM5MDRjZGNhZmNjZjUxM2RiMDQ1MDc0IiwidXNlcl9pZCI6Mn0.3pG63VzFzkDFIrKqsqMwEzrmMPGd_LXqQupRZADBgCQ" | jq
}


# PUT /tasks/{id} - Atualiza uma tarefa existente pelo ID.
update_task() {
    curl -X PUT http://127.0.0.1:8000/api/tasks/4/ \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzMjY2ODM2LCJpYXQiOjE3MjI2NjIwMzYsImp0aSI6IjY1ODVjNmJhZmM5MDRjZGNhZmNjZjUxM2RiMDQ1MDc0IiwidXNlcl9pZCI6Mn0.3pG63VzFzkDFIrKqsqMwEzrmMPGd_LXqQupRZADBgCQ" \
    -d '{
      "title": "Tarefa 4 update",
      "description": "Descrição da tarefa 4 update",
      "due_date": "2025-03-03"
    }' | jq
}

# DELETE /tasks/{id} - Remove uma tarefa pelo ID.
delete_task() {
    curl -X DELETE http://127.0.0.1:8000/api/tasks/4/ | jq
}
