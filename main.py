

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
    
    pass

def movie_recomendations(movie_file, user_movie_file):
    with open(movie_file, 'r') as file1, open(user_movie_file, 'r') as file2:
        friend_file = set(file1.readlines())
        user_file = set(file2.readlines())
    
    non_duplicates = friend_file.symmetric_difference(user_file)
    with open(output_file, 'w') as output:
        output.writelines(non_duplicates)
    return output_file
    