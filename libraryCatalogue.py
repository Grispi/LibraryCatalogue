from libraryBook import Book


class LibraryCatalogue():
    def __init__(self, dic):
        self.currentDay = 0
        self.lengthOfCheckoutPeriod = 7
        self.initialLateFee = 0.50
        self.feePerLateDay = 1.00
        self.dic = dic

    def libraryCatalogue(self, lengthOfCheckoutPeriod, initialLateFee, feePerLateDay):
        self.lengthOfCheckoutPeriod = lengthOfCheckoutPeriod
        self.initialLateFee = initialLateFee
        self.feePerLateDay = feePerLateDay

    def getCurrentDay(self):
        return self.currentDay

    def getBook(self, title):
        return self.dic[title]

    def getLengthOfCheckoutPeriod(self):
        return self.lengthOfCheckoutPeriod

    def getInitialLateFee(self):
        return self.initialLateFee

    def getFeePerLateDay(self):
        return self.feePerLateDay

    def nextDay(self):
        self.currentDay += 1

    def setDay(self, day):
        self.currentDay = day

    def checkoutBook(self, title):
        book = self.getBook(title)
        # print(book.getTitle())
        # print(self.dic[title].getISBN())
        if(book.getIsCheckedOut()):
            self.sorryBookAlreadyCheckedOut()
        else:
            book.setIsCheckedOut(True, self.currentDay)
            print("You just checked out ",
                  book.getTitle(), ". It is due on day ",
                  (self.currentDay + self.getLengthOfCheckoutPeriod()), ".")

    def returnBook(self, title):
        book = self.getBook(title)
        daysLate = self.currentDay - \
            (book.getDayCheckedOut() + self.getLengthOfCheckoutPeriod())
        if daysLate > 0:
            print("You owe the library $",  (self.getInitialLateFee() + daysLate *
                                             self.getFeePerLateDay()), "Because your book is ", daysLate, " days overdue")
        else:
            print("Book returned. Thank you")
        book.setIsCheckedOut(False, -1)

    def sorryBookAlreadyCheckedOut(self):
        print("Sorry Book Already CheckedOut")


p1 = Book("Harry Potter", 3456, 111111)
dic = {}
dic["Harry Potter"] = p1
lib = LibraryCatalogue(dic)
lib.checkoutBook("Harry Potter")

lib.nextDay()
lib.nextDay()
lib.checkoutBook("Harry Potter")
lib.setDay(17)
lib.returnBook("Harry Potter")
lib.checkoutBook("Harry Potter")
