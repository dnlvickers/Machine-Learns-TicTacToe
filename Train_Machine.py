class Train_Machine:
    '''this is the function we will use to train the machine.  Using ReLU with such a small network should make
    training really fast. My goal is to take in the training set of data and train for a set number of epochs. Once
    the console should hopefully log the % epochs completed for debugging purposes.'''
    def __init__(self,machine,train):
        self.computer = machine
        self.training_mode = train