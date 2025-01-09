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
        # Update state
        self.state = [min(max(s + a, 0), 1) for s, a in zip(self.state, agent_action)]  # Keep state values in [0, 1]
        
        # Calculate reward
        reward = -sum((s - 0.5) ** 2 for s in self.state)
        return reward

    def reset(self):
        """Resets the environment."""
        self.state = np.random.rand(self.size)
