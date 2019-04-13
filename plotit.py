import matplotlib.pyplot as plt

def plot(dict_, x_label, y_label, title, y_list=False):
  if type(dict_) is type({}):
    if type(y_list) is type([]):
      for element in dict_:
        plt.plot(y_list,dict_[element], label=element)
    else:
      for element in dict_:
        plt.plot(range(len(dict_[element])),dict_[element], label=element)
      
    plt.xlabel(str(x_label))
    plt.ylabel(str(y_label))
    plt.title(str(title))
    plt.legend()
    plt.show()