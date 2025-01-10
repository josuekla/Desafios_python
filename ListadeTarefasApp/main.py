from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class TodoApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.task_input = TextInput(hint_text="Digite uma nova tarefa", size_hint=(1, 0.1))
        self.add_widget(self.task_input)

        add_button = Button(text="Adicionar Tarefa", size_hint=(1, 0.1))
        add_button.bind(on_press=self.add_task)
        self.add_widget(add_button)

        self.task_list = BoxLayout(orientation="vertical", size_hint_y=None)
        self.task_list.bind(minimum_height=self.task_list.setter('height'))

        scroll_view = ScrollView(size_hint=(1, 0.8))
        scroll_view.add_widget(self.task_list)
        self.add_widget(scroll_view)

    def add_task(self, instance):
        task_text = self.task_input.text.strip()
        if task_text:
            task_label = Label(text=task_text, size_hint_y=None, height=40)
            self.task_list.add_widget(task_label)
            self.task_input.text = ""

class TodoAppMain(App):
    def build(self):
        return TodoApp()
    
if __name__ == "__main__":
    TodoAppMain().run()