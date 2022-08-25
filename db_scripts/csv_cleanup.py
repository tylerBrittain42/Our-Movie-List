import pandas as pd


'''Removing the following columns from the csv
    Rank
    Runtime
    votes
    revenue
    metascore
'''

def main():
    data_frame = pd.read_csv('db_scripts/IMDB_Data.csv')
    data_frame = data_frame.drop(columns=['Rank','Runtime','Votes','Revenue','Metascore'])
    data_frame.to_csv('db_scripts/IMDB_Data_formatted.csv', index=False)


if __name__ == '__main__':
    main()