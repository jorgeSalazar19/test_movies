# imports
from managerData import ManagerData
from serviceSort import SortMovies

class Movie(SortMovies, ManagerData):

    def __init__(self, path_movies):
        self._path_movies = path_movies
        self._data_movies = None
        # call method for upload movies
        self.upload_movies()
    

    @property
    def data_movies(self):
        return self._data_movies
    

    def upload_movies(self):
        self._data_movies = self.upload(self._path_movies)
        self.calculated_average_rating(self.data_movies)
    

    def sort_movies(self):
        self.sort_to_average(self._data_movies)



# funtion main for the test sort and upload files
if __name__ == "__main__":

    # upload data and calculate averga rating for each movie into the json
    movies = Movie('movies.json')
    movies.sort_movies()