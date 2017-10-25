# -*- coding: UTF-8 -*-
import gym
import numpy as np
import random
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam

from collections import deque
import matplotlib.pyplot as plt


class DQN:
    def __init__(self, env):
        self.env = env
        self.memory = deque(maxlen=2000)

        self.gamma = 0.85
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.999
        self.learning_rate = 0.005
        self.tau = .125

        self.model = self.create_model()
        self.target_model = self.create_model()

    def create_model(self):
        model = Sequential()
        state_shape = self.env.observation_space.shape
        model.add(Dense(24, input_dim=state_shape[0], activation="relu"))
        model.add(Dense(48, activation="relu"))
        model.add(Dense(24, activation="relu"))
        model.add(Dense(self.env.action_space.n))
        model.compile(loss="mean_squared_error",
                      optimizer=Adam(lr=self.learning_rate))
        return model

    def act(self, state):
        self.epsilon *= self.epsilon_decay
        self.epsilon = max(self.epsilon_min, self.epsilon)
        if np.random.random() < self.epsilon:
            return self.env.action_space.sample()
        return np.argmax(self.model.predict(state)[0])

    def remember(self, state, action, reward, new_state, done):
        self.memory.append([state, action, reward, new_state, done])

    def replay(self):
        batch_size = 32
        if len(self.memory) < batch_size:
            return

        samples = random.sample(self.memory, batch_size)
        for sample in samples:
            state, action, reward, new_state, done = sample
            target = self.target_model.predict(state)
            if done:
                target[0][action] = reward
            else:
                Q_future = max(self.target_model.predict(new_state)[0])
                target[0][action] = reward + Q_future * self.gamma
            self.model.fit(state, target, epochs=1, verbose=0)

    def target_train(self):
        self.target_model.set_weights(self.model.get_weights().copy())

    def save_model(self, fn):
        self.model.save(fn)


def main():
    env = gym.make('CartPole-v0')

    trials = 2000 + 1

    dqn_agent = DQN(env=env)

    steps = []
    rewards = []
    for trial in range(trials):
        cur_state = env.reset().reshape(1, env.observation_space.shape[0])
        step = 0
        reward_trial = 0
        done = False
        while not done:
            step += 1
            action = dqn_agent.act(cur_state)
            new_state, reward, done, _ = env.step(action)
            env.render()
            reward_trial += reward

            new_state = new_state.reshape(1, env.observation_space.shape[0])
            dqn_agent.remember(cur_state, action, reward, new_state, done)

            dqn_agent.replay()
            dqn_agent.target_train()

            cur_state = new_state
            if done:
                steps.append(step)
                rewards.append(reward_trial)
                print('The %s trial, play %s steps.' % (trial, step))
                break
    plt.plot(steps, label='steps')
    plt.legend()
    plt.title('Without Target Function')
    plt.xlabel('Trials')
    plt.ylabel('Action Numbers')
    plt.savefig('Without')

    return steps, rewards


if __name__ == "__main__":
    main()
