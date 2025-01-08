import numpy as np

class Agent:
    def __init__(self, id, brain_size=10):
        self.id = id
        self.brain = np.random.rand(brain_size)  # Randomly initialized "brain"

    def decide(self, inputs):
        """Decides an action based on inputs."""
        return np.dot(self.brain, inputs)

    def mutate(self, mutation_rate=0.1):
        """Mutates the agent's brain to enable evolution."""
        for i in range(len(self.brain)):
            if np.random.rand() < mutation_rate:
                self.brain[i] += np.random.normal()

    def __repr__(self):
        return f"Agent-{self.id} with brain {self.brain}"
