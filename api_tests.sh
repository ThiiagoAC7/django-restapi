get_token() {
    curl -X POST http://127.0.0.1:8000/api/token/ \
    -H "Content-Type: application/json" \
    -d '{
      "username": "admin",
      "password": "admin"
    }' 
}

# POST /tasks - Cria uma nova tarefa.
create_task() {
    local token=$1
    curl -X POST http://127.0.0.1:8000/api/tasks/ \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $token" \
    -d '{
      "title": "Tarefa 5",
      "description": "Descrição da tarefa 5",
      "due_date": "2025-03-03"
    }' | jq
}

# GET /tasks - Retorna a lista de todas as tarefas.
get_tasks() {
    local token=$1
    curl -X GET http://127.0.0.1:8000/api/tasks/ \
        -H "Authorization: Bearer $token" | jq
}

filter_tasks() {
    local token=$1
    curl -X GET http://127.0.0.1:8000/api/tasks/?title=Tarefa%205 \
        -H "Authorization: Bearer $token" | jq
}

# PUT /tasks/{id} - Atualiza uma tarefa existente pelo ID.
update_task() { local token=$1
    curl -X PUT http://127.0.0.1:8000/api/tasks/5/ \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $token" \
    -d '{
      "title": "Tarefa 5 update",
      "description": "Descrição da tarefa 4 update",
      "due_date": "2025-03-03"
    }' | jq
}

# DELETE /tasks/{id} - Remove uma tarefa pelo ID.
delete_task() {
    curl -X DELETE http://127.0.0.1:8000/api/tasks/4/ | jq
}

ACESS_TOKEN=$(get_token | jq -r '.access')
# get_tasks "$ACESS_TOKEN"
# create_task "$ACESS_TOKEN" 
# update_task "$ACESS_TOKEN"
# filter_tasks "$ACESS_TOKEN"
