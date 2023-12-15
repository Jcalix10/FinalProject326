import tkinter as tk
from tkinter import messagebox
import random as r
import csv

class Rec:
    def __init__(self):
        pass

    def file_reader(self):
        pass

    def counter(self, text):
        pass

    def ask_question(self):
        while True:
            print("What recommendations do you want?")
            choice = input("Choose an Option:" + "\n a. movie" + "\n b. music" + "\n c. books" + "\n d. tv show \n")

            if choice.lower() == 'a':
                movie_input = input('Add movies that you like in this format: |movie name, genre, run time| \n')
                self.show_popup(self.promt(movie_input, 'movies.txt'))

            elif choice.lower() == 'b':
                music_input = input('Add songs that you like in this format: |song name, genre, minutes| \n')
                self.show_popup(self.promt(music_input, 'songs.txt'))

            elif choice.lower() == 'c':
                books_input = input('Add books that you like in this format: |book name, genre, pages| \n')
                self.show_popup(self.promt(books_input, 'books.txt'))

            elif choice.lower() == 'd':
                tvshow_input = input('Add TV shows that you like in this format: |show name, genre, number of seasons| \n')
                self.show_popup(self.promt(tvshow_input, 'shows.txt'))

            else:
                print("Wrong input. Try again.")

    def promt(self, user_input, file):
        self.add_txt_file(user_input, file)
        genre = input('What genre are you looking for? \n')
        return self.recommendations(file, 'recommendation.txt', 'Genre', genre)

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
                data_values = [str(value) for value in data.values()]  
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

    def recommendations(self, input_file, output_file, genre_col, genre):
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

    def random_media(self):
        pass

    def __repr__(self):
        pass

    def main(self):
        self.ask_question()

class RecUI:
    def __init__(self, rec_instance):
        self.rec = rec_instance

    def show_popup(self, message):
        print("Popup:", message)

    def ask_question(self):
        while True:
            print("What recommendations do you want?")
            choice = input("Choose an Option:" + "\n a. movie" + "\n b. music" + "\n c. books" + "\n d. tv show \n")

            if choice.lower() == 'a':
                movie_input = input('Add movies that you like in this format: |movie name, genre, run time| \n')
                self.show_popup(self.rec.promt(movie_input, 'movies.txt'))

            elif choice.lower() == 'b':
                music_input = input('Add songs that you like in this format: |song name, genre, minutes| \n')
                self.show_popup(self.rec.promt(music_input, 'songs.txt'))

            elif choice.lower() == 'c':
                books_input = input('Add books that you like in this format: |book name, genre, pages| \n')
                self.show_popup(self.rec.promt(books_input, 'books.txt'))

            elif choice.lower() == 'd':
                tvshow_input = input('Add TV shows that you like in this format: |show name, genre, number of seasons| \n')
                self.show_popup(self.rec.promt(tvshow_input, 'shows.txt'))

            else:
                print("Wrong input. Try again.")

if __name__ == "__main__":
    rec = Rec()
    rec_ui = RecUI(rec)
    rec_ui.ask_question()