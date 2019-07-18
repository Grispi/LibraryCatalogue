class Book:
    def __init__(self, titleBook, bookPageCount, bookISBN):
        self.title = titleBook
        self.pageCount = bookPageCount
        self.ISBN = bookISBN
        self.isCheckedOut = False
        self.dayCheckedOut = -1

    def getTitle(self):
        return self.title

    def getCountPage(self):
        return self.pageCount

    def getISBN(self):
        return self.ISBN

    def getIsCheckedOut(self):
        return self.isCheckedOut

    def getDayCheckedOut(self):
        return self.dayCheckedOut

    def setIsCheckedOut(self, newIsCheckedOut, currentDayCheckedOut):
        self.isCheckedOut = newIsCheckedOut
        self.setDayCheckedOut(currentDayCheckedOut)

    def setDayCheckedOut(self, day):
        self.dayCheckedOut = day


# p1 = Book("Harry Poter", 3456, 111111)

# print(p1.title, p1.bookISBN, p1.bookPageCount)
# print(p1.getTitle(), p1.getCountPage())
