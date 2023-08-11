# -*- coding: utf-8 -*-
import os
from context import functions
from context import interface

path = '../dist/note.csv'

# Проверяем, пустой ли файл. Если да, то создаем заголовки
if os.stat("../dist/note.csv").st_size == 0:
    functions.createHeader(path)

userOptionChoice = 0
while userOptionChoice != 5:
    userOptionChoice = interface.showOptions()
    match userOptionChoice:
        case 1:
            userInput = str(input("Write new note here: "))
            functions.addNewNote(path, userInput)
        case 2:
            functions.showAll(path)
        case 3:
            functions.editNote(path)
        case 4:
            functions.removeNote(path)