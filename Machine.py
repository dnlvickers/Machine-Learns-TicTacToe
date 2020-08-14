class Machine():
    '''we are going to initialize the machine with training weights and I want to be smart about this
    essentially the game board doesn't matter if it gets rotated. So only 3 types of inputs matter:
    the center, the sides, and the corners. But we will run 4 corner, 4 side neurons, and one center in our network.
    We will use ReLU to get if a neuron fires and by how much. Next, and this is where it gets tricky, I want to rescale
    each output to a  maximum of 1, which will be the square that we adjust. The reason for this is that
    the training data will be simply which square to click next (1.0) and the rest will want to be (0.0).
    So we want the network to have the best move have the highest possible output. This is a custom output,
    which is probably a bad idea, but science must go on!'''
    def __init__(self):
        self.cornerWeights = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] #this is the weight for a piece in the bottom left
        self.sideWeights = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] #this is the weight for a piece on the bottom
        self.centerWeights = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] #weights for center, obviously
        self.weights = [self.cornerWeights, self.sideWeights, self.centerWeights] #put weights into a list for convenience later
        self.trainingRate = 0.1

    def train_machine(self,board,expected):
        '''this funciton is pretty big since it trains the weights. We will feed in a filtered gamme board which has
        been adequately rotated, and then we will take the expectation to begin calculated the prediction of
        the current model for the machine. After this, we will then propogate out corrections to the machine'''
        pass

    def encode_game_board(self,decoded_board,timesToRotate):
        '''to get away with only 3 sets of weights, we need to rotate the game board  and encode it in the language of
        the machine'''
        pass

    def decode_game_board(self,encoded_board,timesToRotate):
        '''this funciton take the board from the language of the machine and outputs it into the state the game
        can understand'''
        pass

    def calculate_output(self,board,type):
        '''we will take in the game board, which is the input, and the target cell which we will decode to determine
        if it is a corner, side, or center'''
        pass