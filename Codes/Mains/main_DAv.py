import gymnasium as gym

import Codes


def main():
    env = gym.make("env_DAv-v0", rendering=True)
    env.reset()
    env.render()
    while not env.terminated:
        actions = [0, 0, 0, 0]  # Put your actions vector here
        obs, _, _, _, _ = env.step(actions)
        env.render()


if __name__ == "__main__":
    main()
