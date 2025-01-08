from simulations.environment import Environment

def test_environment():
    env = Environment(5)
    assert len(env.get_state()) == 5
    print("Environment test passed!")

if __name__ == "__main__":
    test_environment()
