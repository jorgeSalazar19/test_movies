class SortMovies(object):

    
    @classmethod
    def sort_to_average(self, data):
        self._list_average_ratings = []
        for movie in data.get('movies'):
            self._list_average_ratings.append(movie.get('averageRating'))
        import pdb; pdb.set_trace()