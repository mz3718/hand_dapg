import mj_envs
import click 
import os
import gym
import numpy as np
import pickle

DESC = '''
Helper script to visualize demonstrations.\n
USAGE:\n
    Visualizes demonstrations on the env\n
'''

# MAIN =========================================================
@click.command(help=DESC)
@click.option('--env_name', type=str, help='environment to load', required= True)
def main(env_name):
    if env_name is "":
        print("Unknown env.")
        return
    demos = pickle.load(open('./demonstrations/'+env_name+'_demos.pickle', 'rb'))
    # render demonstrations
    demo_playback(env_name, demos)

def demo_playback(env_name, demo_paths):
    e = gym.make(env_name)
    e.reset()
    for path in demo_paths:
        e.env.ss(path['init_state_dict'])
        actions = path['actions']
        for t in range(actions.shape[0]):
            e.step(actions[t])
            e.env.mj_render()

if __name__ == '__main__':
    main()