class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
        self.user_books = {}
        self.more_book =[]
        self.books_prices = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print ("""{name}'s email has been updated to {email}""".format(name = self.name, email=self.email))
        

    def __repr__(self):
        return """ 
        The Users is: {user_name} and email is: {user_email} """.format(user_name = self.name, user_email = self.email)

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email
    
    def read_book(self, book, rating = None, price = None):
        self.book = book
        self.more_book += [self.book.title]
        self.books[self.book] = rating
        self.user_books[self.email] = self.more_book
        self.books_prices[self.book] = price

    def get_average_rating(self):
        self.total_ratings = 0
        rating_counter = 0
        self.results = 0.0
        for rating in self.books.values():
            if type(rating) is int:
                self.total_ratings += rating
                rating_counter += 1
        if rating_counter > 0:
            self.results = self.total_ratings/rating_counter
        return self.results

    def get_average_price(self):
        self.total_prices = 0
        price_counter = 0
        self.results = 0.0
        for price in self.books_prices.values():
            if type(price) is int or type(price) is float:
                self.total_prices += price
                price_counter += 1
        if price_counter > 0:
            self.results = self.total_prices/price_counter
        return self.results
		
class Book():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        self.prices = []
         
    def __hash__(self):
        return hash((self.title, self.isbn))
       
    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print ("""{title}'s ISBN has been updated to {isbn}""".format(title = self.title, isbn = self.isbn))

    def add_rating(self, rating):
        if type(rating) is int and abs(rating) <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def add_book_price(self, price):
        if type(price) is int or type(price) is float:
            self.prices.append(price)
        else:
            print("Invalid Book Prices")
            
    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def get_average_rating(self):
        self.total_ratings = 0
        rating_counter = 0
        self.results = 0.0
        for rating in self.ratings:
            if type(rating) is int:
                self.total_ratings += rating
                rating_counter += 1
        if rating_counter > 0:
            self.results = self.total_ratings/rating_counter
        return self.results
    
    def get_average_price(self):
        self.total_prices = 0
        price_counter = 0
        self.results = 0.0
        for price in self.prices:
            if type(price) is int or type(price) is float:
                self.total_prices += price
                price_counter += 1
        if price_counter > 0:
            self.results = self.total_prices/price_counter	
        return self.results
		
class Fiction(Book):
    
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author():
        return self.author

    def __repr__(self):
        return """
        {title} by {author}.""".format(title = self.title, author = self.author)
		
class Non_Fiction(Book):

    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return """
        {title}, a {level} manual on {subject}""".format(title = self.title, level = self.level, subject = self.subject)
		
class TomeRater():

    def __init__(self):
        self.users = {}
        self.books = {}

    def __repr__(self):
        return """Hello, let us create a library of books and users. Here, the possiblities are endless! """

    def __eq__(self, other):
        return self.books == other.books and self.users == other.users

    def create_book(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.my_book_info = self.check_isbn(self.isbn)
        for values in self.my_book_info.keys():
            if  values == True:
                print("'{my_title}' Book cannot be created! This ISBN has been used by {my_book}!".format(my_title = self.title, my_book = self.my_book_info[values]))
        else:
            return Book(self.title, self.isbn)         

    def check_isbn(self, isbn):
        self.isbn = isbn
        self.return_value = {}
        for book in self.books.keys():
            if book.isbn == self.isbn:
                self.return_value[True] = book.title
                break
        return self.return_value        

    def create_novel(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.my_book_info = self.check_isbn(self.isbn)
        for values in self.my_book_info.keys():
            if  values == True:
                print("Novel cannot be created! This ISBN has been used by {my_book}!".format(my_book = self.my_book_info[values]))
        else:
            return Fiction(self.title, self.author, self.isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        self.title = title
        self.subject = subject
        self.level = level
        self.isbn = isbn
        self.my_book_info = self.check_isbn(self.isbn)
        for values in self.my_book_info.keys():
            if  values == True:
                print("Non-fiction cannot be created! This ISBN has been used by {my_book}!".format(my_book = self.my_book_info[values]))
        else:
            return Non_Fiction(self.title, self.subject, self.level, self.isbn)

    def add_book_to_user(self, book, email, rating = None, price = None):
        self.email = email
        self.result = self.users.get(self.email, "No Value")
        if self.result is "No Value":
            print("No user with email: {my_email}!".format(my_email = self.email))
        else:
            self.users[self.email].read_book(book, rating, price)
            book.add_rating(rating)
            book.add_book_price(price)
        if book in self.books:
            self.books[book] += 1
        else: 
            self.books[book] = 1

    def add_user(self, name, email, user_books = []):
        self.name = name
        self.email = email
        #Check if user email makes sense
        if ".com" in self.email or ".edu" in self.email or ".org" in self.email:
        #Check if user email already exists
            if self.email in self.users.keys():
                print("Username: {email} already exists!".format(email=self.email))
            else:
                self.users[self.email] = User(self.name, self.email)
                if len(user_books) > 0:
                    for my_book in user_books:
                        self.add_book_to_user(my_book, self.email)
        else:
            print("{my_email} is an incorrect email! Please enter the correct email address!".format(my_email = self.email))
            
    def print_catalog(self):
        for book in self.books:
            print (book.title, book.isbn)

    def print_users(self):
        for my_user in self.users.values():
            print (my_user)

    def most_read_book(self):
        self.most_read_book_count = 0
        self.my_most_read_book = None
        for my_book, book_read_count in self.books.items():
            if book_read_count > self.most_read_book_count:
                self.most_read_book_count = book_read_count
                self.my_most_read_book = my_book
        return self.my_most_read_book.title, self.my_most_read_book.isbn

    def most_read_book_object(self):
        self.most_read_book_count = 0
        self.my_most_read_book = None
        for my_book, book_read_count in self.books.items():
            if book_read_count > self.most_read_book_count:
                self.most_read_book_count = book_read_count
                self.my_most_read_book = my_book
        return self.my_most_read_book

    def most_prolific_reader(self):
        self.most_prolific_user_count = 0
        self.my_most_read_user = None
        for my_user_email, my_user_object in self.users.items():
            if len(my_user_object.user_books[my_user_email]) > self.most_prolific_user_count:
                self.most_prolific_user_count = len(my_user_object.user_books[my_user_email])
                self.my_most_read_user = my_user_object
        return self.my_most_read_user.email, self.my_most_read_user.name

    def most_prolific_reader_object(self):
        self.most_prolific_user_count = 0
        self.my_most_read_user = None
        for my_user_email, my_user_object in self.users.items():
            if len(my_user_object.user_books[my_user_email]) > self.most_prolific_user_count:
                self.most_prolific_user_count = len(my_user_object.user_books[my_user_email])
                self.my_most_read_user =  my_user_email
        return self.my_most_read_user
    
    def highest_rated_book(self):
        self.my_average_rating = 0.0
        self.my_highest_rated_book = None
        for my_book in self.books.keys():
            new_rating = my_book.get_average_rating()
            if new_rating > self.my_average_rating:
                self.my_average_rating = new_rating
                self.my_highest_rated_book = my_book
        return self.my_highest_rated_book.title, self.my_highest_rated_book.isbn

    def most_expensive_book(self):
        self.my_average_price = 0.0
        self.my_most_expensive_book = None
        for my_book in self.books.keys():
            new_price = my_book.get_average_price()
            if new_price > self.my_average_price:
                self.my_average_price = new_price
                self.my_most_expensive_book = my_book
        return self.my_most_expensive_book.title, self.my_most_expensive_book.isbn    

    def most_expensive_book_object(self):
        self.my_average_price = 0.0
        self.my_most_expensive_book = None
        for my_book in self.books.keys():
            new_price = my_book.get_average_price()
            if new_price > self.my_average_price:
                self.my_average_price = new_price
                self.my_most_expensive_book = my_book
        return self.my_most_expensive_book   

    def most_positive_user(self):
        self.my_average_rating = 0.0
        self.highest_rated_user = None
        for my_user in self.users.values():
            self.user_rating = my_user.get_average_rating()
            if self.user_rating > self.my_average_rating:
                self.my_average_rating = self.user_rating
                self.highest_rated_user = my_user
        return self.highest_rated_user

    def get_n_most_read_books(self, n):
        self.my_books_copy = {}
        self.n_most_read_book_list = []
        if n <= len(self.books):
            print("Most read", n, "books in descending order are:")
            for i in range(n):
                my_new_array = self.most_read_book()
                self.n_most_read_book_list.append(my_new_array)
                print(my_new_array)
                self.my_books_copy[self.most_read_book_object()] = self.books[self.most_read_book_object()]
                del self.books[self.most_read_book_object()]
            for keys, values in self.my_books_copy.items():
                self.books[keys] = values
        else:
            print(n, "is greater than number of available books in library")

    def get_n_most_prolific_readers(self, n):
        self.my_users_copy = {}
        self.n_most_prolific_readers_list = []
        if n <= len(self.users):
            print("Most prolific", n, "readers in descending order are:")
            for i in range(n):
                my_new_array = self.most_prolific_reader()
                self.n_most_prolific_readers_list.append(my_new_array)
                print(my_new_array)
                self.my_users_copy[self.most_prolific_reader_object()] = self.users[self.most_prolific_reader_object()]
                del self.users[self.most_prolific_reader_object()]
            for keys, values in self.my_users_copy.items():
                self.users[keys] = values
        else:
            print(n, "is greater than number of available readers in library")
    
    def get_n_most_expensive_books(self, n):
        self.my_books_copy = {}
        self.n_most_expensive_book_list = []
        if n <= len(self.books):
            print("Most expensive", n, "books in descending order are:")
            for i in range(n):
                my_new_array = self.most_expensive_book()
                self.n_most_expensive_book_list.append(my_new_array)
                print(my_new_array)
                self.my_books_copy[self.most_expensive_book_object()] = self.books[self.most_expensive_book_object()]
                del self.books[self.most_expensive_book_object()]
            for keys, values in self.my_books_copy.items():
                self.books[keys] = values
        else:
            print(n, "is greater than number of available books in library")
    
    def get_worth_of_user(self, user_email):
        self.total_user_worth = 0.0
        for my_book_prices in self.users[user_email].books_prices.values():
            if type(my_book_prices) is int or type(my_book_prices) is float:
                self.total_user_worth += my_book_prices
            else:
                continue
        return (user_email + "'s worth is: $"+ str(self.total_user_worth))
            
            