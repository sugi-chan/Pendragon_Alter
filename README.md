# Pendragon_Alter

This repo contains the code to train a reinforcement learning based bot for the game Fate Grand Order as well as have the bot play FGO on a mobile device. See this medium post for details [here](https://medium.com/datadriveninvestor/project-pendragon-an-ai-bot-for-fate-grand-order-23f51b6e3268) on how that was done. 

This repo is featured in this post INSERT BLOG LINK WHEN POSTED.

the colesseum.py file contains the simulated FGO environment
netlearner.py contains the network and related functions that help it train
main.py allows you to run the learner, train the network, and it saves models, currently models are saved to a models folder within the working directory

the Pendragon_Alter.py file is where I reintergrated the new reinforcement learning model back into the framework I built to allow a python bot to play a mobile phone game. So that file and the utils.py will contain the changes needed to allow the new network to play. 

One odd problem I found is that since Keras+Tensorflow are quire memory greedy... I think Tensorflow just allocates all available memory to itself... it meant that I was not able to run this new network alongside the other CNNs that I build for the original bot. As such I have to call each model within their relevant functions and delete them when the function completes... this is quite inefficient so I would like to figure out a better work around in the future but for now it is alright. 
