from environment import Env

class Agent:
    def __init__(self):
        pass

    def get_action(self, state):
        return 0



if __name__ == "__main__":
    env = Env()
    agent = Agent()

    state = env.reset()
    env.plot_goal()

    action = agent.get_action(state)
    next_state, reward, done = env.step(action)
    state = next_state

    # env.plot_current_state()
