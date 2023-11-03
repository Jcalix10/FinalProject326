import random as r
import pandas as pd

'''
INST335 FINAL PROJECT (MOVIE RECCOMENDER)
'''


def movie_file_reader(reccomendations_csv):
         recs = pd.read_csv(reccomendations_csv)  
            

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
          "\n c. books\n")
    
    while True:
        if choice == 'a':
            pass
        elif choice == 'b':
            pass
        elif choice == 'b':
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
    

def book_filter():
        ''' Method to filter through each txt file and find recommended book
        '''
        pass

def tv_show_filter():
        ''' Method to filter through each txt file and find recommended tv show
        '''
        pass

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
