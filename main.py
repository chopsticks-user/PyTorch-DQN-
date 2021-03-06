import numpy as np
import gym
from ann import dqn
#from ultis import plot_learning_curve

if __name__ == "__main__":
    
    env = gym.make("ALE/BankHeist-v5", render_mode = "human")
    
    bot = dqn(in_features = (210, 160, 3), out_features = 18, n_actions = 18, batch_size = 128, hidden_layers_dims=[256, 256, 256])
    env.reset()

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    j = 0
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    for i in range(500):
        obs = env.reset()
        done = False

        #debugging space
        ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        

        actions = []

        
        ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        while not done:
            action = bot.decision(obs)
            new_obs, reward, done, _ =  env.step(action)
            bot.transition(obs, action, new_obs, reward, done)
            bot.learn()
            obs = new_obs

            #debugging space
            ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
            actions.append(action)
            if(j % 10 == 0):
                print("Episode {}: Action: {}, Total reward: {}., Epsilon: {:.4f}, Loss: {}".format(j, actions, bot.reward, bot.epsilon, bot.loss), ", Learning rate: ", bot.alpha)
                actions.clear()
            j += 1



            ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''       
    
    env.close()