# an instance attribute holds info regarding an instance but is available to the whole class
# a class attribute hs a class scope and is called on the class itself

# class Album:
#     album_count = 0
#     def __init__(self, date):
#         Album.album_count +=1
#         self.release_date = date

# album = Album(2007)
# album = Album(2007)
# album = Album(2007)
# print(f"We are at album count {album.album_count} released in {album.release_date}")

#  to define  a class method we use a @classmethod decorator




class Album:
      GENRES = ["Hip-Hop", "Pop", "Jazz"] # --> This is a class constant. It is used for data that does not change though it can be reassigned. It is written in capital letters to differentiate it from class attribute.
      album_count =0

      def __init__(self, name, genre):
            self.name = name
            self.genre = genre
      @classmethod # Definig a classmethod, start by using the @classmethod decorator
      def increase_album_count(cls): # --> then make sure to pass cls in the() just like passing self in methods
            cls.album_count +=1 # --> pass your code here
new_count = Album.increase_album_count() #I have called the increment function so count increases by one so it is currently at one
new_count = Album.increase_album_count() # I have called the increment function for the second time so currently count is at two
new_count = Album.increase_album_count() # I have called the increment function for the third time so count currently at three
my_album = Album("Her loss", "Pop")
print(my_album.album_count) 
print(my_album.genre)