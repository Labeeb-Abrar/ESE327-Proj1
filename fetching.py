from ucimlrepo import fetch_ucirepo

class Node:
    def __init__(self, data, header):
        self.data = data
        self.header = header
    def __str__(self):
        return f"{self.data} --> {self.header}"

def main():    
    # fetch dataset 
    car_evaluation = fetch_ucirepo(id=19)
    
    # data (as pandas dataframes) 
    x = car_evaluation.data.features
    y = car_evaluation.data.targets
    
    car_variables = car_evaluation.variables

    # variable information 
    print(car_variables) 
    pass
if __name__ == '__main__':
    main()