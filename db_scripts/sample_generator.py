import pandas as pd
import csv



def main():

    names = ["James", "Robert", "John", "Michael", "David", "William", "Richard", "Joseph"]
    password = 'pass'

    generate_movies()
    generate_users(names, password)
    generate_lists(len(names))



def generate_movies():
    data_frame = pd.read_csv('db_scripts/IMDB_Data.csv')
    data_frame = data_frame.drop(columns=['Rank','Runtime','Votes','Revenue','Metascore'])
    data_frame.to_csv('db_scripts/sample_movie.csv', index=False, quotechar='"',
                      header=None, quoting=csv.QUOTE_NONNUMERIC)


def generate_users(names,password):
    with open('db_scripts/sample_users.csv', 'w') as f:
        f.write('name,password\n')
        for name in names:
            f.write(f'{name},{password}\n')


def generate_lists(num):
    with open('db_scripts/sample_lists.csv', 'w') as f:
        f.write('name\n')
        for ele in range(num):
            f.write(f'{ele}\n')




if __name__ == '__main__':
    main()