import numpy as np

class Environment:
    def __init__(self, size=10):
        self.size = size
        self.state = np.random.rand(size)

    def get_state(self):
        """Returns the current state of the environment."""
        return self.state

    def step(self, agent_action):
        """Applies an agent's action and updates the environment."""
        self.state = self.state + agent_action
        reward = -np.sum((self.state - 0.5) ** 2)  # Reward for stabilizing around 0.5
        return reward

    def reset(self):
        """Resets the environment."""
        self.state = np.random.rand(self.size)
