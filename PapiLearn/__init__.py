from gym.envs.registration import register

register(
    id='PapiLearn-v0',
    entry_point='gym_game.envs:PapiLearnEnv',
    max_episode_steps=1000,
)