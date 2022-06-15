from kivy.core.window import Window
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        #### aplication configs ####
        self.icon = "calculator.png"
        self.title = "Calculator"
        #### aplication configs ####

        #### varialbles ####
        self.operators = ["+","-","*","/"]
        self.last_was_operator = None
        self.last_button = None
        #### variables ####

        #### layout ####
        main_layout = BoxLayout(orientation = "vertical")
        #where the math is displayed
        self.solution = TextInput(background_color = "blue", foreground_color = "white")


        main_layout.add_widget(self.solution)
        buttons = [
            ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","+"],
            [".","0","c","-"]
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text = label, font_size = 30, background_color = "grey",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press = self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        
        equal_button = Button(
            text ="=", font_size = 30, background_color = "grey",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        equal_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_button)

        return main_layout
        #### layout ####
        

if __name__ == "__main__":
    app = MainApp()
    app.run()
    
#MainApp().run()