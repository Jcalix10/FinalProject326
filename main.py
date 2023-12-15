import random as r
import csv
from tkinter import *

'''
INST335 FINAL PROJECT (MOVIE RECCOMENDER)
'''

class Rec(Frame):
      
    def __init__(self, master):
        super(Rec, self).__init__(master)
        self.grid()
        self.pack()
        self.create_widgets()

    def printinput(self):
        self.inputValue = self.moviebox.get("1.0", "end-1c")
        self.movie_input_value = self.inputValue.strip() if self.inputValue else ""
        print("Movie input:", self.movie_input_value)


        self.promt(self.movie_input_value, 'movies.txt')

        

    def movie(self):
        
        self.clear_screen()
        self.textbox2 = Label(self, text="Add movies that you like in this format: |movie name, genre, rum time|")
        self.textbox2.pack(padx= 20, pady=20)
        self.moviebox= Text(root, height=1, width=30)
        self.moviebox.pack()

        buttonCommit = Button(root, height=1, width=10, text="Confirm", command=lambda: self.printinput())
        buttonCommit.pack()
        

        #movie_input = self.inputValue #input('Add movies that you like in this format: |movie name, genre, rum time| \n') 
        
       

    def book(self):
        self.clear_screen()
        books_input = input('Add books that you like in this format: |book name, genre, pages| \n')
        return self.promt(books_input, 'books.txt') 
        
    def song(self):
        self.clear_screen()
        music_input = input('Add songs that you like in this format: |song name, genre, minutes| \n')
        return self.promt(music_input, 'songs.txt') 

    def tvshow(self):
        self.clear_screen()
        tvshow_input = input('Add tv shows that you like in this format: |show name, genre, number of seasons| \n')
        return self.promt(tvshow_input, 'shows.txt') 

    def create_widgets(self):
        bottomf = Frame(root)
        bottomf.pack(side = BOTTOM)

        button_quit = Button(bottomf, text = "Exit Program", command= self.quit)
        button_quit.pack(padx=20, pady=20, side=BOTTOM)

        self.textbox1 = Label(self, text = "What recomendations do you want?")
        self.textbox1.pack(padx= 20, pady=20)

        self.bttn1 = Button(self, text="Movie", command = self.movie)
        self.bttn1.pack(ipadx= 20, ipady= 20, side=LEFT)

        self.bttn2 = Button(self, text="Book", command = self.book)
        self.bttn2.pack(ipadx= 20, ipady= 20, side= RIGHT)

        self.bttn3 = Button(self, text="Song", command = self.song)
        self.bttn3.pack(ipadx= 20, ipady= 20, side= LEFT)

        self.bttn4 = Button(self, text="Tv Show", command = self.tvshow)
        self.bttn4.pack(ipadx= 20, ipady= 20, side=RIGHT)


    def clear_screen(self):
        self.bttn1.pack_forget()
        self.bttn2.pack_forget()
        self.bttn3.pack_forget()
        self.bttn4.pack_forget()
        self.textbox1.pack_forget()
         

    def counter(self, text):

        file = open(text, 'r')
        reading = file.readlines()
        total_counter = -1
        dup_counter = 0
        dup_list = []

        for num in reading:
            if reading.count(num) >= 2:
                dup_list.append(num)
                dup_counter +=1

            total_counter += 1

        return total_counter, dup_counter, dup_list 

    '''
    def ask_question(self):

        while True:
            print("What recomendations do you want?")
            choice = input(" Choose an Option:" + 
                            "\n a. movie" +
                            "\n b. music" +
                            "\n c. books" + 
                            "\n d. tv show \n")
                
            if choice == 'a': #movies    
                    movie_input = input('Add movies that you like in this format: |movie name, genre, run time| \n')
                    return self.promt(movie_input, 'movies.txt') 

            elif choice == 'b': #music             
                    music_input = input('Add songs that you like in this format: |song name, genre, minutes| \n')
                    return self.promt(music_input, 'songs.txt')                  
            elif choice == 'c': #books              
                    books_input = input('Add books that you like in this format: |book name, genre, pages| \n')
                    return self.promt(books_input, 'books.txt')                    
            elif choice == 'd': #tv shows         
                    tvshow_input = input('Add tv shows that you like in this format: |show name, genre, number of seasons| \n')
                    return self.promt(tvshow_input, 'shows.txt')                    
            else:
                print("Wrong input. Try again.")

    '''
    def promt(self, user_input, file):

        '''self.add_txt_file(user_input, file) 

        self.clear_screen
        self.textbox3 = Label(self, text="What genre are you looking for?")
        self.textbox3.pack(padx= 20, pady=20)
        self.entry = Entry(self)
        self.entry.pack()
        var.trace("w", self.printinput)

        genre = input('What genre are you looking for?')
        
        return self.recomendations(file, 'recomendation.txt', 'Genre', genre)
        
        pass'''
        
        self.add_txt_file(user_input, file)
        self.clear_screen()  # Added parentheses to call the method

        self.textbox3 = Label(self, text="What genre are you looking for?")
        self.textbox3.pack(padx=20, pady=20)
        self.entry = Entry(self)
        self.entry.pack()

        # You need to decide how to handle this line since var is not defined in the method
        # var.trace("w", self.printinput)

        genre = input('What genre are you looking for?')
        return self.recomendations(file, 'recomendation.txt', 'Genre', genre)

    
    def add_txt_file(self, user_input, file):
        if user_input is None or not user_input.strip():
            print("User input is empty or None.")
            # Handle the case appropriately, e.g., return an error or ask for input again
            return
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
        with open(file, 'r') as file:
            reader = csv.DictReader(file, delimiter='\t')
            for row in reader:
                if all(info.strip() == row[key].strip() for key, info in data.items() if key in row):
                    return True
        return False






    
    def append_entries_to_file(self, new_data, file_path):
        with open(file_path, 'a') as file:
            for data in new_data:
                file.write(f"{data['name']}	{data['genre']}	{data['num_val']}\t1")
    
    def get_existing_friends(self, data, file):
        with open(file, 'r') as file:
            for line in file:
                line_data = line.strip().split('\t')
                data_values = [str(value) for value in data.values()]  # Convert all values to string
                if all(info.strip() == line_data[idx].strip() for idx, info in enumerate(data_values)):
                    existing_friends = line_data[-1].strip()
                    return int(existing_friends) if existing_friends.isdigit() else 0
        return 0

            




    
    def change_friend_val(self, data, file_path):
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

    
    
    def random_media():
        ''' Method that chooses a random choice of media to output for the reader 
            - called only if the reader selects that they don’t want to choose something 
            from the playlist on their own
            '''
        pass
    
    def __repr__():
        pass

    def main(self):
        self.ask_question()
        ''' Main method that filters chosen files and creates new list of recommendations for user
        '''
        pass

root = Tk()
var = StringVar()
root.title("WatchMate")
root.geometry("640x480")
app = Rec(root)
root.mainloop()
  


'''if __name__ == "__main__":
    r = Rec()
    r.main()
 '''