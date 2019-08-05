from AsymptoticSearchTimeStudy import *
from ImplementationComparisonStudy import *
import numpy as np




class Simulator(object):

    @staticmethod
    def SimulateUniformData(n_array, seed, n_samples,data_max,\
    avg_search_times,widget,implementation_comparison = False):
        """
        n_array     -- array of N values over which search time is to be
                        evaluated
        seed        -- random seed
        n_samples   -- number of samples for each value of n evaluated
        data_max    -- upper limit of uniform distribution from which random
                       data is sampled
        avg_search_times -- matrix of average search times
                            row index: data structure
                            column index: data

        widget     -- ipywidget object corresponding to the progress bar
                      will be incremented when each element of n_array completes
        """
        if not implementation_comparison:
            np.random.seed(seed)
            for i,n in enumerate(n_array):
                data = np.random.uniform(0,data_max,int(n))
                study = AsymptoticSearchTimeStudy(data)

                search_times = np.zeros((avg_search_times.shape[0],n_samples))

                for j in range(0,n_samples):
                    random_index = int(np.random.uniform(0,int(n),1))
                    search_times = study.perform_search(data, search_times,random_index,j)

                for j in range(0,avg_search_times.shape[0]):
                    avg_search_times[j][i] = np.mean(search_times[j][:])

                if widget:
                    widget.value += 1 # signal to increment the progress bar
                    time.sleep(.1)

        else:
            np.random.seed(seed)
            for i,n in enumerate(n_array):
                data = np.random.uniform(0,data_max,int(n))
                study = ImplementationComparisonStudy(data)

                search_times = np.zeros((avg_search_times.shape[0],n_samples))

                for j in range(0,n_samples):
                    random_index = int(np.random.uniform(0,int(n),1))
                    search_times = study.perform_search(data, search_times,random_index,j)

                for j in range(0,avg_search_times.shape[0]):
                    avg_search_times[j][i] = np.mean(search_times[j][:])

                if widget:
                    widget.value += 1 # signal to increment the progress bar
                    time.sleep(.1)

        return avg_search_times
