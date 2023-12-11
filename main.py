import random as r
import csv

'''
INST335 FINAL PROJECT (MOVIE RECCOMENDER)
'''
class Rec:
      
    def __init__(self):
            pass

    def file_reader(self):
           pass
            

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


    def ask_question(self):

        while True:
            print("What recomendations do you want?")
            choice = input(" Choose an Option:" + 
                            "\n a. movie" +
                            "\n b. music" +
                            "\n c. books" + 
                            "\n d. tv show \n")
        

            add_choices = True
            if choice == 'a': #movies
                while add_choices == True:
                    movie_input = input('Add movies that you like in this format: |movie name, genre, rum time|')
                    return self.promt(movie_input, 'movies.txt') 
            elif choice == 'b': #music
                while add_choices == True:
                    music_input = input('Add songs that you like in this format: |song name, genre, minutes|')
                    return self.promt(music_input, 'songs.txt') 
                pass
            elif choice == 'c': #books
                while add_choices == True:
                    books_input = input('Add books that you like in this format: |book name, genre, pages|')
                    return self.promt(books_input, 'books.txt') 
                pass
            elif choice == 'd': #tv shows
                while add_choices == True:
                    tvshow_input = input('Add tv shows that you like in this format: |show name, genre, number of seasons|')
                    return self.promt(tvshow_input, 'shows.txt') 
                pass
            else:
                print("Wrong input. Try again.")
                
    
    def promt(self, user_input, file):

        self.add_txt_file(user_input, file) 
        
        genre = input('what genre are you looking for? \n')
        
        return self.recomendations(file, 'recomendation.txt', 'Genre', genre)
        
        pass
    
    def add_txt_file(self, user_input, file):
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
                    'num_val': run_time
                }
                
                if not self.is_duplicate_entry(data, file):
                    info_list.append(data)
                else:
                    self.change_friend_val(data, file)

        self.append_entries_to_file(info_list, file) 

       
        pass
    
    def is_duplicate_entry(self, data, file):
        with open(file, 'r') as file:
            for line in file:
                if all(info.strip() in line for info in data.values()):
                    return True  


    
    def append_entries_to_file(self, new_data, file_path):
        with open(file_path, 'a') as file:
            for data in new_data:
                file.write(f"{data['name']}	{data['genre']}	{data['num_val']}	1")
    
    def change_friend_val(self, data, file_path):
        column_name = 'Friends'
        key_column = 'name'
        key_value = data['name']  
        
        with open(file_path, 'r', newline='') as file:
            reader = csv.DictReader(file, delimiter='\t')
            rows = list(reader)

        for row in rows:
            if key_column in row and row[key_column] == key_value:
                if column_name in row:
                    row[column_name] = str(int(row[column_name]) + 1)
                else:
                    row[column_name] = '1'

        with open(file_path, 'w', newline='') as file:
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='\t')

            writer.writeheader()
            writer.writerows(rows)
        
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

if __name__ == "__main__":
    r = Rec()
    r.main()
 
