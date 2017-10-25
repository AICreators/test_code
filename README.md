Reinforcement Learning: An Introduction
Build Status

Python code for Sutton & Barto's book Reinforcement Learning: An Introduction (2nd Edition)

If you have any confusion about the code or want to report a bug, please open an issue instead of emailing me directly.
Contents
Click to view the sample output
Chapter 1

Tic-Tac-Toe
Chapter 2

Figure 2.1: An exemplary bandit problem from the 10-armed testbed
Figure 2.2: Average performance of epsilon-greedy action-value methods on the 10-armed testbed
Figure 2.3: Optimistic initial action-value estimates
Figure 2.4: Average performance of UCB action selection on the 10-armed testbed
Figure 2.5: Average performance of the gradient bandit algorithm
Figure 2.6: A parameter study of the various bandit algorithms
Chapter 3

Figure 3.5: Grid example with random policy
Figure 3.8: Optimal solutions to the gridworld example
Chapter 4

Figure 4.1: Convergence of iterative policy evaluation on a small gridworld
Figure 4.2: Jack’s car rental problem
Figure 4.3: The solution to the gambler’s problem
Chapter 5

Figure 5.1: Approximate state-value functions for the blackjack policy
Figure 5.3: The optimal policy and state-value function for blackjack found by Monte Carlo ES
Figure 5.4: Weighted importance sampling
Figure 5.5: Ordinary importance sampling with surprisingly unstable estimates
Chapter 6

Figure 6.2: Random walk
Figure 6.3: Batch updating
Figure 6.4: Sarsa applied to windy grid world
Figure 6.5: The cliff-walking task
Figure 6.7: Interim and asymptotic performance of TD control methods
Figure 6.8: Comparison of Q-learning and Double Q-learning
Chapter 7

Figure 7.2: Performance of n-step TD methods on 19-state random walk
Chapter 8

Figure 8.3: Average learning curves for Dyna-Q agents varying in their number of planning steps
Figure 8.5: Average performance of Dyna agents on a blocking task
Figure 8.6: Average performance of Dyna agents on a shortcut task
Figure 8.7: Prioritized sweeping significantly shortens learning time on the Dyna maze task
Chapter 9

Figure 9.1: Gradient Monte Carlo algorithm on the 1000-state random walk task
Figure 9.2: Semi-gradient n-steps TD algorithm on the 1000-state random walk task
Figure 9.5: Fourier basis vs polynomials on the 1000-state random walk task
Figure 9.8: Example of feature width’s effect on initial generalization and asymptotic accuracy
Figure 9.10: Single tiling and multiple tilings on the 1000-state random walk task
Chapter 10

Figure 10.1: The cost-to-go function for Mountain Car task in one run
Figure 10.2: Learning curves for semi-gradient Sarsa on Mountain Car task
Figure 10.3: One-step vs multi-step performance of semi-gradient Sarsa on the Mountain Car task
Figure 10.4: Effect of the alpha and n on early performance of n-step semi-gradient Sarsa
Figure 10.5: Differential semi-gradient Sarsa on the access-control queuing task
Chapter 11

Figure 11.2: Baird's Counterexample
Figure 11.6: The behavior of the TDC algorithm on Baird’s counterexample
Figure 11.7: The behavior of the ETD algorithm in expectation on Baird’s counterexample
Chapter 12

Figure 12.3: Off-line λ-return algorithm on 19-state random walk
Figure 12.6: TD(λ) algorithm on 19-state random walk
Figure 12.8: True online TD(λ) algorithm on 19-state random walk
Figure 12.10: Sarsa(λ) with replacing traces on Mountain Car
Figure 12.11: Summary comparison of Sarsa(λ) algorithms on Mountain Car
Environment
Python2 or Python3
Numpy
Matplotlib
Six
Seaborn
Usage
git clone https://github.com/ShangtongZhang/reinforcement-learning-an-introduction.git
cd reinforcement-learning-an-introduction/chapterXX
python XXX.py
Contribution
This project contains almost all the programmable figures in the book. However, when I completed this project, the book is still in draft and some chapters are still incomplete. Furthermore, due to the limited computational capacity of my machine, I can only use limited runs and episodes for some experiments, so the sample output is much less smooth than that in the book.

If you want to contribute some exercises of the book or some missing examples, fix some bugs in existing code, provide sample outputs with higher quality, add some new interesting experiments related to RL, feel free to open an issue or make a pull request. I will appreciate it very much. Also, feel free to comment on the sample outputs, some curves are really interesting.

Following are known missing figures/examples:

Example 3.4: Pole-Balancing
Example 3.6: Draw Poker
Example 5.2: Soap Bubble
Example 8.5: Rod Maneuvering
Figure 12.14: The effect of λ (I don't have time to replicate it for now)
Chapter 14 & 15 are about psychology and neuroscience
Chapter 16: Backgammon, The Acrobot, Go
