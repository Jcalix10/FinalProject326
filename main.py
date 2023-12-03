import random as r
import pandas as pd

'''
INST335 FINAL PROJECT (MOVIE RECCOMENDER)
'''
class Rec:
      
    def __init__(self):
            pass

    def movie_file_reader(self, reccomendations_csv):
            df = pd.read_csv(reccomendations_csv)  
            rec_list = df.to_dict()

            return rec_list
            

    def dup_counter():
        ''' Method that counts duplicate recommendations from different people 
            and asks the user if they would like to be recommended the most popular result
        '''
        pass


    def ask_question():
        print("What recomendations do you want?")
        choice = input(" Choose an Option:" + 
          "\n a. movie" +
          "\n b. music" +
          "\n c. books" + 
          "\n d. tv show \n")
    
        while True:
            add_choices = True
            if choice == 'a':
                while add_choices == True:
                    movie_input = input('Add 5 movies that you like in this format: |movie name, genre, rum time|')
                    #add code to add it into the txt file
                    more_choice = input('Would you want to add more? Y or N')
                    add_choices = True if more_choice == 'Y' else False  
            elif choice == 'b':
                while add_choices == True:
                    music_input = input('Add 5 songs that you like in this format: |song name, genre, minutes|')
                    #add code to add it into the txt file
                    more_choice = input('Would you want to add more? Y or N')
                    add_choices = True if more_choice == 'Y' else False  
                pass
                pass
            elif choice == 'c':
                while add_choices == True:
                    books_input = input('Add 5 books that you like in this format: |book name, genre, pages|')
                    #add code to add it into the txt file
                    more_choice = input('Would you want to add more? Y or N')
                    add_choices = True if more_choice == 'Y' else False  
                pass
            elif choice == 'd':
                while add_choices == True:
                    tvshow_input = input('Add 5 tv shows that you like in this format: |show name, genre, number of seasons|')
                    #add code to add it into the txt file
                    more_choice = input('Would you want to add more? Y or N')
                    add_choices = True if more_choice == 'Y' else False  
                pass
            else:
                print("Wrong input. Try again.")
    



    def song_recomendations(friend_song_file, user_song_file):
        with open(friend_song_file, 'r') as file1, open(user_song_file, 'r') as file2:
            friend_file = set(file1.readlines())
            user_file = set(file2.readlines())
    
        non_duplicates = friend_file.symmetric_difference(user_file)
        with open(output_file, 'w') as output:
            output.writelines(non_duplicates)
        return output_file
    
    
    def movie_recomendations(movie_file, user_movie_file):
        with open(movie_file, 'r') as file1, open(user_movie_file, 'r') as file2:
            friend_file = set(file1.readlines())
            user_file = set(file2.readlines())
    
        non_duplicates = friend_file.symmetric_difference(user_file)
        with open(output_file, 'w') as output:
            output.writelines(non_duplicates)
        return output_file
    

    def book_reccomendations(book_file, user_book_file):
        with open(book_file, 'r') as file1, open(user_book_file, 'r') as file2:
            friend_file = set(file1.readlines())
            user_file = set(file2.readlines())
    
        non_duplicates = friend_file.symmetric_difference(user_file)
        with open(output_file, 'w') as output:
            output.writelines(non_duplicates)
        return output_file

    def tvshow_reccomendations(tv_show_file, user_tv_show_file):
        with open(tv_show_file, 'r') as file1, open(user_tv_show_file, 'r') as file2:
            friend_file = set(file1.readlines())
            user_file = set(file2.readlines())
    
        non_duplicates = friend_file.symmetric_difference(user_file)
        with open(output_file, 'w') as output:
            output.writelines(non_duplicates)
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
