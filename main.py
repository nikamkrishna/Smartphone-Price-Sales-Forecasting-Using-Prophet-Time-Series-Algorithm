import kivy
kivy.require('1.11.1') # Replace with your Kivy version

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Enter your name:')
        text_input = TextInput()
        button = Button(text='Click me!', size_hint=(None, None), size=(200, 50))
        button.bind(on_press=lambda x: self.on_button_click(text_input.text)) # Pass the text input value to on_button_click
        layout.add_widget(label)
        layout.add_widget(text_input)
        layout.add_widget(button)
        return layout

    def on_button_click(self, value):
        # Display the input value in the label
        self.root.children[0].text = f'Hello, {value}!'
