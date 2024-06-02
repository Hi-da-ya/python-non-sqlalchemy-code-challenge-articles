class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if not (5 <= len(title) <=50):
            raise ValueError("Title must be between 5 and 50 characters")
        self.__title = title
    #setting author name property
    @property
    def title(self):
        return self.__title 

    @title.setter
    def title(self, value):
        raise AttributeError("Name cannot be modified after instantiation")
           
        
class Author:
    def __init__(self, name):
          if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
          self.__name = name
    #setting author name property
    @property
    def name(self):
        return self.__name 

    @name.setter
    def name(self, value):
        raise AttributeError("Name cannot be modified after instantiation")

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    #setting name property
    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2<= len(value) <= 16:
            self._name = value
    #setting category property
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category        

            


    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass