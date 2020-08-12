# Machine-Learns-TicTacToe
This code is currently --- not complete ---

This repo is going to follow along my creation of a machine learning (ML) algorithm. I am doing this all from scratch, and the only libarary that I will be using is pygame to create the game interface. I am not an expert on ML, but I have read up on the theory, and I figured creating everything by hand would help to give an better understanding of ML. It will also create a better appreciation of ML libraries like TensoFlow when I get around to using them.

The vision for this project will be to be able to create a new blank machine with new weights. You can have the machine learn for a selected number of games with certain rates, and maybe insert initial training weights which you saved from a previous session. Then you will be able to play it and send it back to train when all is said and done. So, the  todo list is a follows:
 - create ti-tac-toe in pygame where I can play against an AI of default descision weights.
 - create a program to genetically modify those training weights such that the child can play the parent and the winner becomes the new parent
 - be able to modify the number of epochs and variables constraining the randomness of the mutations between generations
 - be able to cancel the training at any point and be able to play the current parent AI generated from the ML process when it completes its number of epochs or gets its training    canceled
 - be able to resubmit the algorithm for more training
 
I anticipate the most issue is going to come from finding descision functions that properly chose a square to land on and can be modified with the weight mutation to create  a better tic-tac-toe AI. It will be messy, and without the use of simplifying libraries it will likely be so simple that my highest hope is that it can just recognize a row has 2 pieces so that is can complete a 3 in a row and win. But mostly, I think it will  be fun exploring the intricacies of this program. Hopefully I will be able to leverage what I learn here into a project using tensorflow and be able to apply it to a game with a much simpler decision tree so that I can get it to aproach an actual global minimum.
