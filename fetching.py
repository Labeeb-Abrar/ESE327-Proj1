from ucimlrepo import fetch_ucirepo

def fetchData(id):    
    # fetch dataset 
    evaluation = fetch_ucirepo(id=id)
    x = evaluation.data.features.values.tolist()
    # y = evaluation.data.targets.values.tolist()
    
    return x