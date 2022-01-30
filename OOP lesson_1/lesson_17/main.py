

todo_items = []


class TodoItem:
    def __init__(self, stroka):
        self.is_done = True
        self.stroka = stroka
    def check(self):
        self.is_done = True
    def uncheck(self):
        self.is_done = False


class Todo(TodoItem):
    def add_todo(self, exemplar):
        for i in exemplar:
            lst = todo_items.append(i)
            todo_items.append(lst)
        return f'{ todo_items }'

    def list_items(self):
        return f'{todo_items}'

    def find(self, word):
        self.word = word
        return 
    
# todoitem = TodoItem("sdfs")
# print(todo.stroka)
todo_items = TodoItem("s")
# todo1 = Todo(stroka= "Todo1")

# 
print(todo_items.check())
# print(todo.uncheck())
# print(todo1.list_items())
# print(todo1.find("sdds"))


