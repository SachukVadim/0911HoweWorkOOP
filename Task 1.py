class Editor:
    def view_document(self):
        print("Перегляд документа.")

    def edit_document(self):
        print("Редагування документів недоступне для безкоштовної версії.")


class ProEditor(Editor):
    def edit_document(self):
        print("Редагування документа доступне.")


license_key = input("Введіть ліцензійний ключ: ")

editor = ProEditor() if license_key == "PRO123" else Editor()

editor.view_document()
editor.edit_document()
