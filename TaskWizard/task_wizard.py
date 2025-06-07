import kivy  # also has Pyjnius installed
import speech_recognition as sr
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from random import choice
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import threading
class StartScreen(Screen):
    # There should also be a button that allows the user to switch between Voice Recognition and Enter Text Mode
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=50)
        logo = Image(source='project-management-strategic-plan-to-manage-resources-for-development-working-process-and-schedule-task-completion-concept-smart-businessman-project-manager-manage-multiple-project-dashboards-vector.jpg', size_hint=(1, 0.3))
        title = Label(text='Welcome to [font=Roboto-Bold] TaskWizard [/font]',
                      size_hint=(1, 0.2),
                      markup=True)
        button = Button(text='Let us continue!', font_size=25, background_color=choice(['#FFA07A', '#98FB98', '#ADD8E6']), border=(1, 1, 1, 1))
        button.bind(on_press=self.switch_screen)
        layout.add_widget(title)
        layout.add_widget(logo)
        layout.add_widget(button)
        self.add_widget(layout)

    def switch_screen(self, *args):
        screen_manager.current = 'main'
        """
        voice_recog = Popup(title='Voice Recognition Option', content=BoxLayout(orientation='vertical', spacing=10),
                            size_hint=(0.8, 0.4))
        # two buttons for voice recognition
        voice_on_button = Button(text="Yes")
        voice_off_button = Button(text="No")
        # determine which voice button is selected

        def voice_button_yes(instance):
            voice_recog.dismiss()
            MainScreen.voice_recognition_enabled = True
            MainScreen.label.text = "Please start speaking:"

        def voice_button_no(instance):
            voice_recog.dismiss()
            MainScreen.voice_recognition_enabled = False

        # if the button is yes, then... if no, then, just let them manually choose
        # code here to do the above description
        voice_on_button.bind(on_press=voice_button_yes)
        voice_off_button.bind(on_press=voice_button_no)

        voice_recog.content.add_widget(Label(text="Would you like to start use voice recognition?"))
        voice_recog.content.add_widget(voice_on_button)
        voice_recog.content.add_widget(voice_off_button)

        voice_recog.open()
        """
class MainScreen(Screen):
    """
    label = None
    def prev_voice_opt(self):
        if self.voice_recognition_enabled:
            def update_label(self, text):
                self.label.text = text
            voice_input = voice_recognition(self)
        if voice_input is not None and voice_input.lower() == 'make a plan of what to do':
            screen_manager.current = 'second'
            # Add a button to go back to the home screen
            back_button = Button(text="Back to Home Screen", size_hint=(None, None), size=(200, 50))
            back_button.bind(on_press=lambda x: setattr(screen_manager, 'current', 'start'))
            self.add_widget(back_button)
            # voice_recognition() # still need to complete it and while listening, show the options they can select
    # There should also be a button that allows the user to switch between Voice Recognition and Enter Text Mode
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=50)
        # add the title here and the all the actions we can take
        title = Label(text='Please select what would you like to do', size_hint=(1, 0.3))
        layout.add_widget(title)

        grid = GridLayout(cols=3, spacing=20, size_hint=(1, 0.7))
        buttons = [Button(text='Make a Plan of What To Do', font_size=25,
                          background_color='#FFA07A', border=(1, 1, 1, 1)),
                   Button(text='Check my Progress', font_size=25,
                          background_color='#98FB98', border=(1, 1, 1, 1)),
                   Button(text='Delete Tasks in my Plan', font_size=25,
                          background_color='#ADD8E6', border=(1, 1, 1, 1)),
                   ]
        for button in buttons:
            grid.add_widget(button)
            button.bind(on_press=self.switch_screen)

        layout.add_widget(grid)
        self.add_widget(layout)

    def switch_screen(self, instance):
        if instance.text == 'Make a Plan of What To Do':
            screen_manager.current = 'second'
        if instance.text == 'Check my Progress':
            screen_manager.current = 'third'



class SecondScreen(Screen):
    voice_recognition_enabled = False
    text_input = ""
    dropdown = None
    selected_category = None
    def prev_voice_opt(self):
        if self.voice_recognition_enabled:
            # voice_recognition() # still need to complete it and while listening, show the options they can select
            pass
    # There should also be a button that allows the user to switch between Voice Recognition and Enter Text Mode

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=50)
        title = Label(text='Please choose an option', size_hint=(1, 0.2), markup=True)

        # it might be better if the task category related functions are in the third screen
        dropdown_button = Button(text="Task Categories", size_hint=(0.2, 0.1), size=(200, 50))

        # create a drop down list
        self.dropdown = DropDown()
        task_categories = ['Work', 'School', 'Household Chores', 'Leisure Activities', 'Healthcare', "Social Events",
                           "Financial Tasks", "Personal Development", "Others"]  # need at least 5-6 categories
        # think of a way to use voice recognition to select an option instead of manually choosing (unless the user chooses to do so)


        for category in task_categories:
            btn = Button(text=category, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)
            # add voice recognition somewhere here
        self.dropdown.bind(on_select=lambda instance, x: setattr(dropdown_button, 'text', x))

        dropdown_button.bind(on_release=self.dropdown.open)
        # all the above are the main codes related to the dropdown list of task categories
        # add a TextInput widget
        self.selected_category = dropdown_button.text
        self.text_input = TextInput(hint_text='Enter your task details here...', size_hint=(0.6, 0.4), multiline=False)
        self.save_button = Button(text='Save', font_size=25, background_color=choice(['#FFA07A', '#98FB98', '#ADD8E6']), border=(1, 1, 1, 1))
        self.save_button.bind(on_press=self.on_save)

        button = Button(text='Go back to the main menu', font_size=25, background_color=choice(['#FFA07A', '#98FB98', '#ADD8E6']), border=(1, 1, 1, 1))
        button.bind(on_press=self.switch_screen)
        layout.add_widget(title)
        layout.add_widget(dropdown_button)
        layout.add_widget(self.text_input)
        layout.add_widget(self.save_button)
        layout.add_widget(button)


        self.add_widget(layout)

    def show_dropdown(self, widget):
        dropdown = self.dropdown

    def on_task_input(self, instance, value):
        self.task_input = value

    def on_select_category(self, instance, x):
        self.selected_category = x

    def on_save(self, instance):
        # save the task_input to a file or database or perform any other action to store the task
        self.save_button.text = "The task is saved!"
        task_text = self.text_input.text # get the task input
        print(task_text)
        category = self.selected_category #
        saved_task = {'task': task_text, 'category': category}
        print(saved_task)# create a dictionary with the task and category
        data_set = MainApp.data
        for i, saved_dict in enumerate(saved_task):
            key = f"task{i + 1}"
            data_set[f"task{len(data_set) + 1}"] = saved_task
        print("length of the dataset:", len(data_set))
    def switch_screen(self, *args):
        screen_manager.current = 'main'

class ThirdScreen(Screen):
    # add tasks there
    def on_pre_enter(self, *args):
        # get the task data from the app's data dictionary
        task_data = MainApp.data
        print(len(task_data))
        # check if there is task data
        if task_data:
            # set the task text in the label
            for key, task in task_data.items():
                task_text = task_data[key].get('text')
                task_category = task_data[key].get('category')
                task_label = Label(text=f'Task: {task_text}\nCategory: {task_category}',
                                   size_hint=(1, None), height=100, font_size=30,
                                   halign='center', valign='middle')
                self.ids.task_layout.add_widget(task_label)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=50)
        ThirdScreen.on_pre_enter(self)
        title = Label(text='Here are all the tasks', size_hint=(1, 0.2), markup=True)
        # create a layout for the task labels
        task_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        task_layout.bind(minimum_height=task_layout.setter('height'))
        button = Button(text='Go back to the main menu', font_size=25,
                        background_color=choice(['#FFA07A', '#98FB98', '#ADD8E6']), border=(1, 1, 1, 1))
        button.bind(on_press=self.switch_screen)
        layout.add_widget(title)
        layout.add_widget(task_layout)
        layout.add_widget(button)
        self.add_widget(layout)

        # save a reference to the task layout for later use
        self.ids.task_layout = task_layout
    def switch_screen(self, *args):
        screen_manager.current = 'main'
# above is a sample example
    """
    def log_into_database ():
        # this function could be optional because the app can be only local for simplicity
    """

    """
    def main ():
        # run other functions and manipulate them to make the app run efficiently
    """


class MainApp(App):
    data = {}
    print(data)
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        start_screen = StartScreen(name='start')
        main_screen = MainScreen(name='main')
        second_screen = SecondScreen(name='second')
        third_screen = ThirdScreen(name='third')
        screen_manager.add_widget(start_screen)
        screen_manager.add_widget(main_screen)
        screen_manager.add_widget(second_screen)
        screen_manager.add_widget(third_screen)
        return screen_manager


if __name__ == '__main__':
    app = MainApp()
    app.run()



def voice_recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please start speaking:")
        audio = r.listen(source)

        try:
            voice_input = r.recognize_google(audio)
            print(f"Voice Recognizer think you said: {voice_input}")
            return voice_input
        except sr.UnknownValueError:
            print("Could not understand the audio. Please try again later")
            raise SpeechRecognitionError("Could not understand the audio. Please try again later")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition Service; {e} ")
            return SpeechRecognitionError(f"Could not request results from Google Speech Recognition Service; {e} ")

class SpeechRecognitionError(Exception):
    pass

