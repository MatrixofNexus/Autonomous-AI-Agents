from simulations.environment import Environment

def run_simulation(agent, environment, steps=10):
    """Runs a simulation for an agent in an environment."""
    total_reward = 0
    for _ in range(steps):
        state = environment.get_state()
        action = agent.decide(state)
        reward = environment.step(action)
        total_reward += reward
    return total_reward
