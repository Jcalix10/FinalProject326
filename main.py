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
            

    def counter(text):

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


    def ask_question():
        """Promts the user to enter their choices

        Returns:
            txt file: returns a file with their recomended movie/music/books/tv shows
        """
        print("What recomendations do you want?")
        choice = input(" Choose an Option:" + 
          "\n a. movie" +
          "\n b. music" +
          "\n c. books" + 
          "\n d. tv show \n")
    
        while True:
            add_choices = True
            if choice == 'a': #movies
                while add_choices == True:
                    movie_input = input('Add movies that you like in this format: |movie name, genre, rum time|')
                    return Rec.promt(movie_input, 'movies.txt') 
            elif choice == 'b': #music
                while add_choices == True:
                    music_input = input('Add songs that you like in this format: |song name, genre, minutes|')
                    return Rec.promt(movie_input, 'music.txt') 
                pass
            elif choice == 'c': #books
                while add_choices == True:
                    books_input = input('Add books that you like in this format: |book name, genre, pages|')
                    return Rec.promt(movie_input, 'books.txt') 
                pass
            elif choice == 'd': #tv shows
                while add_choices == True:
                    tvshow_input = input('Add tv shows that you like in this format: |show name, genre, number of seasons|')
                    return Rec.promt(movie_input, 'shows.txt') 
                pass
            else:
                print("Wrong input. Try again.")
    
    def promt(input, file):
        """_summary_

        Args:
            input (_type_): _description_
            file (_type_): _description_

        Returns:
            _type_: _description_
        """
        Rec.add_txt_file(file, file) 
        
        genre = input('what genre are you looking for? \n')
        
        return Rec.recomendations(file, 'recomendation.txt', 'Genre', genre)
        
        pass
    
    def add_txt_file(string_input, file):
        entry = string_input.strip('|')
        info_list = []
        
        for i in entry:
            if i.strip():
                info = entry.strip(',').split(',')
                name = info[0].strip()
                genre = info[1].strip()
                run_time = info[2].strip()     
                
                data = {
                    'name': name,
                    'genre': genre,
                    'num_val': run_time
                }
                
                if not Rec.is_duplicate_entry(data, file):
                    info_list.append(data)
                else:
                    #add code to change the friends val in txt
                    pass   

        Rec.append_entries_to_file(info_list, file)        

       
        pass
    def chage_friend_val(data, file, ):
        column_name = 'Friends'
        key_column = 'Title'
        key_value = data['name']  
        
        with open(file, 'r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        for row in rows:
            if row[key_column] == key_value:
                row[column_name] += 1

        with open(file, 'w', newline='') as file:
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            writer.writerows(rows)
        pass
    def is_duplicate_entry(data, file):
        with open(file, 'r') as file:
            for line in file:
                if all(info.strip() in line for info in data.values()):
                    return True  

        return False
    
    def append_entries_to_file(new_data, file_path):
        with open(file_path, 'a') as file:
            for data in new_data:
                file.write(f"{data['name']}	{data['genre']}	{data['num_val']}	1")
    
    
    def recomendations(input_file, output_file, genre_col, genre):
        with open(input_file, 'r') as file1:
            lines = input_file.readlines()
    
        filtered_records = [line.strip() for line in lines if line.split(' ')[genre_col].strip() == genre]

        with open(output_file, 'w') as output_file:
            for record in filtered_records:
                output_file.write(record + '\n')
        return output_file
    
    
    def random_media():
        ''' Method that chooses a random choice of media to output for the reader 
            - called only if the reader selects that they don’t want to choose something 
            from the playlist on their own
            '''
        pass
    
    def __repr__():
        pass

    def main():
        ''' Main method that filters chosen files and creates new list of recommendations for user
        '''
        pass

    if __name__ == "__main__":
        main()
