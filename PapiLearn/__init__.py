from gym.envs.registration import register

register(
    id='PapiLearn-v0',
    entry_point='PapiLearn.envs:PapiLearnEnv',
    max_episode_steps=10000,
)