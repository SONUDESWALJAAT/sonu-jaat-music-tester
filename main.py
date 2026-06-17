import os
import shutil
from mutagen.mp3 import MP3
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import MDTabsBase, MDTabs
from kivymd.uix.card import MDCard

class Tab(MDBoxLayout, MDTabsBase):
    pass

class AudioSorterApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Dark"
        
        screen = Screen()
        main_layout = MDBoxLayout(orientation='vertical', padding=10, spacing=10)
        
        main_layout.add_widget(
