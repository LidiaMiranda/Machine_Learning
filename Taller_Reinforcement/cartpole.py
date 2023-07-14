import gym

env = gym.make('CartPole-v1',render_mode='human')

episodios = 10
totalR = []


for episodio in range(episodios):
    t=0
    observation = env.reset()
    for _ in range(200):
        env.render()
        print(observation)
        accion = env.action_space.sample()

        observation, reward, done, info = env.step(accion)
        t += 0
        if done:
            totalR.append(t)
            breakº

env.close()

