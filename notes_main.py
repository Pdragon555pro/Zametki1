from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import json

notes = {
    "Добро пожаловать!": {
    'текст' : "Это самое лучшее приложение для заметок во всей вселенной!",
    "теги" : ["Добро", "инструкция"]}}

# with open("notes_data.json", "w", encoding='utf-8') as file:
#     json.dump(notes, file, ensure_ascii=False, indent=4)

app = QApplication([])
ui = uic.loadUi('zametki2.html')
ui.show()

#Функции
def show_note():
    key = ui.list_notes.selectedItems() [0].text()
    print(key)
    ui.field_text.setText(notes[key]['текст'])
    ui.list_tags.clear()
    ui.list_tags.addItems(notes[key]['теги'])
def add_note():
    note_name, ok = QInputDialog.getText(ui, 'Добавить заметку', 'Название заметки:')
    if ok and note_name != '':
        notes[note_name] = {'текст': '', 'теги': []}
        ui.list_notes.addItem(note_name)
        ui.list_tags.addItems(notes[note_name]['теги'])
def save_note():
    if ui.list_notes.selectedItems():
        key = ui.list_notes.selectedItems()[0].text()
        notes[key]['текст'] = ui.field_text.toPlainText()
        with open('notes_data.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
        print(notes)
    else:
        print('Заметка для сохранения не выбрана!')

def del_note():
    if ui.list_notes.selectedItems():
        key = ui.list_notes.selectedItems()[0].text()
        del notes[key]
        ui.list_notes.clear()
        ui.list_tags.clear()
        ui.field_text.clear()
        ui.list_notes.addItems(notes)
        with open('notes_data.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
        print(notes)
    else:
        print('Заметка для удаления не выбрана!')

def add_tag():
    if ui.list_notes.selectedItems():
        key = ui.list_notes.selectedItems()[0].text()
        tag = ui.field_tag.text()
        if not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            ui.list_tags.addItem(tag)
            ui.field_tag.clear()
        with open('notes_data.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False, indent=4)
        print(notes)
    else:
        print('Заметка для добавления тега не выбрана!')

def del_tag():
    if ui.list_notes.selectedItems():
        key = ui.list_notes.selectedItems()[0].text()
        tag = ui.list_tags.selectedItems()[0].text()
        notes[key]['теги'].remove(tag)
        ui.list_tags.clear()
        ui.list_tags.addItems(notes[key]['теги'])
        with open('notes_data.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False, indent=4)
    else:
        print('Тег для удаления не выбран!')

def search_tag():
    print(ui.button_tag_search.text())
    tag = ui.field_tag.text()
    if ui.button_tag_search.text() == 'Искать' and tag:
        print(tag)
        notes_filtered = {} #Заметки с выделенным тегом
        for note in notes:
            if tag in notes[note]['теги']:
                notes_filtered[note]=notes[note]
        ui.button_tag_search.setText('Сбросить поиск')
        ui.list_notes.clear()
        ui.list_tags.clear()
        ui.list_notes.addItems(notes_filtered)
        print(ui.button_tag_search.text())
    elif ui.button_tag_search.text() == 'Сбросить поиск':
        ui.field_tag.clear()
        ui.list_notes.clear()
        ui.list_tags.clear()
        ui.list_notes.addItems(notes)
        ui.button_tag_search.setText('Искать')
        print(ui.button_tag_search.text())
    else:
        pass

#Кнопки
ui.button_note_create.clicked.connect(add_note)
ui.button_note_save.clicked.connect(save_note)
ui.button_note_del.clicked.connect(del_note)
ui.list_notes.itemClicked.connect(show_note)
ui.button_tag_add.clicked.connect(add_tag)
ui.button_tag_del.clicked.connect(del_tag)
ui.button_tag_search.clicked.connect(search_tag)

file = open('notes_data.json', 'r', encoding='utf-8')
notes = json.load(file)
    
ui.list_notes.addItems(notes)

app.exec_()
