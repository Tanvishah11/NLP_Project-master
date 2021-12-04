import re
import os
import pandas as pd

class DataProcessing:
    def __init__(self):
        self.REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]")
        self.REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

    def read_file(self,path):
        """
        to read a file
            path : str = valid path to the file
            returns : list of file contents
        """
        extarcted_file = []
        for line in open(path, 'r'):
            extarcted_file.append(line.strip())
        return self.data_cleanup(extarcted_file)

    def data_cleanup(self, data):
        """
        for data cleanup
            data : List = STRING DATA TO BE CLEANED UP
            returns : List(str) of cleaned data
        """
        data = [self.REPLACE_NO_SPACE.sub("", line.lower()) for line in data]
        data = [self.REPLACE_WITH_SPACE.sub(" ", line) for line in data]
        return data

    def save_processed_data(self,data,name):
        data_frame = pd.DataFrame(data, columns=['text'])
        data_frame.to_pickle("./"+name+".pkl")

    def read_saved_data(self,name):
        return pd.read_pickle("./"+name+".pkl")


if __name__ == "__main__":
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    TRAIN_NEG = os.path.abspath(os.path.join(ROOT_PATH, '../shared/imdb/train/neg'))
    TRAIN_POS = os.path.abspath(os.path.join(ROOT_PATH, '../shared/imdb/train/pos'))
    print(TRAIN_NEG)
    files = [os.path.join(TRAIN_NEG, file_) for file_ in os.listdir(TRAIN_NEG)]

    TEST = DataProcessing()
    cleaned_data = [ TEST.read_file(file_path) for file_path in files]
    TEST.save_processed_data(cleaned_data, "train_positive")
