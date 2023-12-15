import random as r
import csv
from tkinter import *
import unittest

class Rec:
    

   def counter(self, text):
       '''
       Counter method for files

       Args:
       self and text

       Returns:
       total_counter
       '''

       file = open(text, 'r')
       count = file.readlines().count


       return count


   def ask_question(self, choice = 'a', movie_input = "Jaws, Horror, 145", music_input = "Life is Good by Drake", 
                    books_input = "Cat in the Hat by Dr.Seuss, Comedy, 23", tvshow_input = "Breaking Bad, Drama, 5"):
       '''
       A menu for asking the user about their preferences in different categories (movies, music, books, and TV shows).
       It also prompts the user to provide input in a specific format for each category and then calls the prompt method.

       Args:
       self

       Returns:
       self.prompt(media_input, 'corresponding_text_file.txt') 
       '''

       while True:
           print("What recomendations do you want?")
           choice = input(" Choose an Option:" +
                           "\n a. movie" +
                           "\n b. music" +
                           "\n c. book" +
                           "\n d. tv show \n")
      

          
           if choice == 'movie' or 'a': #movies   
                   movie_input = input('Add movies that you like in this format: |movie name, genre, run time| \n')
                   return self.prompt(movie_input, 'movies.txt')  

           elif choice == 'music' or 'b': #music            
                   music_input = input('Add songs that you like in this format: |song name, genre, minutes| \n')
                   return self.prompt(music_input, 'songs.txt')                 
           elif choice == 'book' or 'c': #books             
                   books_input = input('Add books that you like in this format: |book name, genre, pages| \n')
                   return self.prompt(books_input, 'books.txt')                   
           elif choice == 'tv show' or 'd': #tv shows        
                   tvshow_input = input('Add tv shows that you like in this format: |show name, genre, number of seasons| \n')
                   return self.prompt(tvshow_input, 'shows.txt')                   
           else:
               print("Wrong input. Try again.")



   def prompt(self, user_input, file):
       '''
       Grabs user input and puts it into the corresponding txt file

       Args: 
       self, user_input, file

       Returns: 
       self.recomendations(file, 'recomendation.txt', 'Genre', genre)
       '''

       self.add_txt_file(user_input, file)
      
       genre = input('what genre are you looking for? \n')
      
       return self.recomendations(file, 'recomendation.txt', 'Genre', genre)
      
    
  
   def add_txt_file(self, user_input, file):
       '''
       Processes user input, extracts information, and updates a data structure 

       Args:
       self, user_input, file

       Returns:
       An updated data structure that splits up user input into correct columns
       '''
       
       entry = user_input.strip('|')
       info_list = []
      
       if entry.strip():
           info = entry.strip(',').split(',')
           if len(info) == 3:
               name = info[0].strip()
               genre = info[1].strip()
               run_time = info[2].strip()    
              
               data = {
                   'name': name,
                   'genre': genre,
                   'num_val': run_time,
                   'friend': 1
               }
              
               existing_friends = self.get_existing_friends(data, file)
               if existing_friends is not None:
                   data['friend'] = existing_friends + 1
                   self.change_friend_val(data, file)
               else:
                   info_list.append(data)


       self.append_entries_to_file(info_list, file)

        
  
   def is_duplicate_entry(self, data, file):
       '''
       Checks to see if a set of data already exists in a file by comparing each row in the file with the user data

       Args:
       self, data, and file

       Returns:
       True or False whether or not it already exists
       '''
       with open(file, 'r') as file:
           reader = csv.DictReader(file, delimiter='\t')
           for row in reader:
               if all(info.strip() == row[key].strip() for key, info in data.items() if key in row):
                   return True
       return False


  
   def append_entries_to_file(self, new_data, file_path):
       '''
       Appends new entries to a file

       Args:
       self, new_data, and file_path

       Returns:
       None
       '''
       with open(file_path, 'a') as file:
           for data in new_data:
               file.write(f"{data['name']} {data['genre']} {data['num_val']}\t1")
  
   def get_existing_friends(self, data, file):
       '''
       Reads a file, parses through it, and checks if there are repeated entries based on user input.
       If there is a repeated entry, it increases counter/returns the number of existing friends
       
       Args:
       self, data, and file 

       Returns:
       integer of friends
       '''
       with open(file, 'r') as file:
           for line in file:
               line_data = line.strip().split('\t')
               data_values = [str(value) for value in data.values()]  # Convert all values to string
               if all(info.strip() == line_data[idx].strip() for idx, info in enumerate(data_values)):
                   existing_friends = line_data[-1].strip()
                   return int(existing_friends) if existing_friends.isdigit() else 0
       return 0


  
   def change_friend_val(self, data, file_path):
       '''
       Updates the Friends value in a file based on user input

       Args:
       self, data, and file_path

       Returns:
       None
       '''
       key_column = 'Title'
       key_value = data['name']


       with open(file_path, 'r') as file:
           reader = csv.DictReader(file, delimiter='\t')
           rows = list(reader)


       for row in rows:
           if row[key_column] and row[key_column].strip() == key_value:
               current_friends_str = row['Friends']
               try:
                   current_friends = int(current_friends_str) if current_friends_str else 0
                   current_friends += 1
                   row['Friends'] = str(current_friends)
               except ValueError:
                   print(f"Invalid friend value: {current_friends_str}")
                   row['Friends'] = '1'


       with open(file_path, 'w', newline='') as file:
           fieldnames = reader.fieldnames
           writer = csv.DictWriter(file, delimiter='\t', fieldnames=fieldnames)
           writer.writeheader()
           writer.writerows(row for row in rows if row is not None)



   def recomendations(self, input_file, output_file, genre_col, genre):
       '''
       Reads a file, filters rows based on a specified genre column and genre, and writes the matching rows to an output file.

       Args: 
       self, input_file, output_file, genre_col, and genre

       Returns
       output_file
       '''
       with open(input_file, 'r') as file1:
           lines = file1.readlines()
          
       header = lines[0].split('\t')
       genre_col_index = None


       for idx, col_name in enumerate(header):
           if genre_col.lower() in col_name.lower():
               genre_col_index = idx
               break


       if genre_col_index is None:
           print(f"Error: Genre column '{genre_col}' not found in the header.")
           return


       print(f"Genre column index: {genre_col_index}")


       with open(output_file, 'w') as output_file:


           output_file.write(lines[0])


           for line in lines[1:]:


               if line.split('\t')[genre_col_index].strip().lower() == genre.lower():
                   output_file.write(line)
                   print(f"Matching record: {line.strip()}")


       return output_file


   def main(self):
       '''
       Main function

       Args:
       self

       Returns:
       Running program
       '''
       self.ask_question()
       

# Tests 

              
class Test(unittest.TestCase):
 

    def test_ask_question(self):
        r = Rec()
        self.assertEqual(r.ask_question('a'), r.prompt(movie_input="Frozen, Family, 123", file='movie.txt'))
        self.assertEqual(r.ask_question('b'), r.prompt(music_input="Hello by Adele, Pop, 2:10", file='songs.txt'))
        self.assertEqual(r.ask_question('c'), r.prompt(book_input="Cat in the Hat by Dr.Seuss, Comedy, 20", file='books.txt'))
        self.assertEqual(r.ask_question('d'), r.prompt(tvshow_input="Breaking Bad, Drama, 5", file='shows.txt'))

    def test_counter(self):
        r = Rec()
        
        count = r.counter("movies.txt")
        self.assertEqual(count, 1)

if __name__ == "__main__":
   # unittest.main()   
    
    r = Rec()
    r.main()

