from models.agent_model import Agent

def test_agent_creation():
    agent = Agent(1)
    assert len(agent.brain) > 0
    print("Agent creation test passed!")

if __name__ == "__main__":
    test_agent_creation()
