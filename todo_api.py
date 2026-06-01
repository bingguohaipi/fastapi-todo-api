from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List,Optional

app=FastAPI(title="待办事项API")

class Todo(BaseModel):
    id:Optional[int]=None
    title:str
    description:Optional[str]=None
    completed:bool=False

todos=[]
next_id=1

@app.get('/todos',response_model=List[Todo],summary="获取所有待办事项")
async def get_todos(todo_id:int):
    return todos

@app.get('/todos/{todo_id}',response_model=Todo,summary="获取单个待办事项")
async def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404,detail="待办事项不存在")


@app.post('/todos',response_model=Todo,summary="创建待办事项")
async def create_todo(todo:Todo):
    global next_id
    todo.id=next_id
    next_id+=1
    todos.append(todo)
    return todo

@app.put('/todos/{todo_id}',response_model=Todo,summary="更新待办事项")
async def update_todo(todo_id:int,update_todo:Todo):
    for i,todo in enumerate(todos):
        if todo.id==todo_id:
            updated_todo.id=todo_id
            todos[i]=updated_todo
            return updated_todo
    raise HTTPException(status_code=404,detail="待办事项不存在")

@app.delete('/todos/{todo_id}',summary="删除待办事项")
async def delete_todo(todo_id:int):
    global todos
    for i,todo in enumerate(todos):
        if todo.id==todo_id:
            del todos[i]
            return {"message":"待办事项删除成功"}
    raise HTTPException(status_code=404,detail="待办事项不存在")
            
            
    
