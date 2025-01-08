from models.agent_model import Agent
import random

def evolve_population(agents, fitness_function, mutation_rate=0.1):
    """Evolves the agents based on their fitness."""
    fitness_scores = [fitness_function(agent) for agent in agents]
    top_agents = select_top_agents(agents, fitness_scores)

    # Generate new population
    new_agents = []
    for _ in range(len(agents)):
        parent = random.choice(top_agents)
        child = Agent(parent.id)
        child.brain = parent.brain.copy()
        child.mutate(mutation_rate)
        new_agents.append(child)

    return new_agents

def select_top_agents(agents, fitness_scores, top_k=5):
    """Selects the top-k agents based on fitness."""
    sorted_agents = sorted(zip(agents, fitness_scores), key=lambda x: x[1], reverse=True)
    return [agent for agent, _ in sorted_agents[:top_k]]
