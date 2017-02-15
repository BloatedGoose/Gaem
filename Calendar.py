import pygame
#c. ten real life minutes to a year in the game, maybe start faster and slow down as the game progresses
class Calendar(object):
    timeCurrent = (m, h, d, m, y)

    appointments = []

    def addApp(date, event):
        appointments.append((date, event))
        break;

    def dateMatch(checkedDate):
        if (checkedDate == timeCurrent)
            return true
        else
            return false
        break;

    def ageUpdate(listPeople):
        for person in listPeople:
            if (dateMatch(person.birthday)):
                person.age += 1
        break;
