import csv
import datetime
import random


def createHeader(path):
    header = ["Date of creation", "ID", "Note"]
    with open(path, 'a+', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)


def addNewNote(path, note):
    # Создаем генерацию ID. Он будет иметь вид: "буква-число"
    letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'z']  # Список букв
    letter = random.randint(0, len(letter_list))  # Генерируем букву
    data_log = datetime.date.today()  # Генерируем дату
    note_list = [str(data_log), str(letter_list[letter]) + "-" + str(random.randint(0, 9999)), note]  # Генерируем
    # массив для записи в файл
    with open(path, 'a+', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(note_list)
        file.close()


def showAll(path):
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
        file.close()

def editNote(path):
    myList = []
    print("Please enter the new details for each of the following: ")
    # Создаём пустой массив, записываем в него данные из файла
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            myList.append(row)
        file.close()

    # Показываем строки по нумерации, которые можно изменить
    print("Please see the details to editing: ")
    for i in range(len(myList)):
        print("Row" + str(i) + " :" + str(myList[i]))

    userInputToEdit = int(input("Which row would you like to change? Enter 1 - " + str(len(myList) - 1) + ": "))

    # Меняем данные на выбранной строке
    myList[userInputToEdit][0] = str(datetime.date.today())
    for i in range(1, len(myList[0])):
        newDetails = input("Enter new data for " + str(myList[0][i]) + ": ")
        myList[userInputToEdit][i] = newDetails

    # Показываем изменённый МАССИВ
    print("Please see the details of the new file below: ")
    for i in range(len(myList)):
        print("Row" + str(i) + " :" + str(myList[i]))

    # Если да, то записываем данные из массива в файл
    changeCSV = input("Would you like to make the changes to the csv file? Y/N: ").lower()
    if changeCSV == "y":
        with open(path, 'w+', newline='') as file:
            writer = csv.writer(file)
            for i in range(len(myList)):
                writer.writerow(myList[i])
            file.close()

def removeNote(path):
    # Создаём пустой массив и записываем туда данные с файла
    myList = []
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            myList.append(row)
        file.close()

    # Показываем по нумерации строки, которые можно изменить
    print("Please see the details to editing: ")
    for i in range(len(myList)):
        print("Row" + str(i) + " :" + str(myList[i]))

    userInputToRemove = int(input("Which row would you like to remove? Enter 1 - " + str(len(myList) - 1) + ": "))
    # Удаляем строку, по номеру, который ввёл пользователь
    myList.remove(myList[userInputToRemove])

    # Показываем изменённый МАССИВ
    print("Please see the details of the new file below: ")
    for i in range(len(myList)):
        print("Row" + str(i) + " :" + str(myList[i]))

    # Если да, то записываем в файл данные из изменённого массива
    changeCSV = input("Would you like to make the changes to the csv file? Y/N: ").lower()
    if changeCSV == "y":
        with open(path, 'w+', newline='') as file:
            writer = csv.writer(file)
            for i in range(len(myList)):
                writer.writerow(myList[i])
            file.close()