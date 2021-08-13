import numpy as np
import matplotlib.pyplot as plt
import time
import copy


class Environment:
    cliff = -3;
    road = -1;
    sink = -2;
    goal = 2
    goal_position = [2, 3]
    # 3x4크기의 공간에 각각의 칸마다 보상 설정
    reward_list = [[road, road, road, road], [road, road, sink, road], [road, road, road, goal]]
    reward_list1 = [['road', 'road', 'road', 'road'], ['road', 'road', 'sink', 'road'],
                    ['road', 'road', 'road', 'goal']]

    def __init__(self):
        self.reward = np.asarray(self.reward_list)
        # 이동을 하고 그 결과를 반환

    def move(self, agent, action):
        done = False
        new_pos = agent.pos + agent.action[action]  # 새 위치

        if self.reward_list1[agent.pos[0]][agent.pos[1]] == 'goal':
            reward = self.goal  # 목적지 일경우
            observation = agent.set_pos(agent.pos)  # 현재 위치
            done = True
        elif new_pos[0] < 0 or new_pos[0] >= self.reward.shape[0] or new_pos[1] < 0 or new_pos[1] >= self.reward.shape[
            1]:
            reward = self.cliff  # 밖으로 갈경우
            observation = agent.set_pos(agent.pos)  # 현재위치
            done = True
        else:
            observation = agent.set_pos(new_pos)  # 새위치로 이동
            reward = self.reward[observation[0], observation[1]]
        return observation, reward, done


class Agent:
    action = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]])  # 이동에 대한 값
    select_action_pr = np.array([0.25, 0.25, 0.25, 0.25])  # 행동에 대한 확률

    def __init__(self, initial_position):
        self.pos = initial_position
        # 위치 정보 저장

    def set_pos(self, position):
        self.pos = position
        return self.pos

    def get_pos(self):
        return self.pos


def state_value_function(env, agent, G, max_step, now_step):
    gamma = 0.85  # 할인율
    if env.reward_list1[agent.pos[0]][agent.pos[1]] == 'goal':
        return env.goal  # 목적지일경우
    if max_step == now_step:
        pos1 = agent.get_pos()
        for i in range(len(agent.action)):
            agent.set_pos(pos1)
            observation, reward, done = env.move(agent, i)  # 각각의 이동에 대한 결과
            G += agent.select_action_pr[i] * reward
        return G  # 보상의 누적 합계
    else:
        pos1 = agent.get_pos()
        for i in range(len(agent.action)):
            observation, reward, done = env.move(agent, i)  # 각각의 이동에 대한 결과
            G += agent.select_action_pr[i] * reward
            if done == True:
                if observation[0] < 0 or observation[0] >= env.reward.shape[0] or observation[1] < 0 or observation[
                    1] >= env.reward.shape[1]:
                    agent.set_pos(pos1)
                    # 최대 max_step 만큼 반복
            next_v = state_value_function(env, agent, 0, max_step, now_step + 1)
            G += agent.select_action_pr[i] * gamma * next_v  # 이동후 그 이후의 보상값에 gamma를 곱한후 더함
            agent.set_pos(pos1)
        return G
    # 상태 가치 함수값 을 나타내는 테이블 출력


def show_v_table(v_table, env):
    for i in range(env.reward.shape[0]):
        print('+-----------------' * env.reward.shape[1], end='')
        print('+')
        for k in range(3):
            print('|', end='')
            for j in range(env.reward.shape[1]):
                if k == 0:
                    print('                 |', end='')
                if k == 1:
                    print('    {0:8.2f}     |'.format(v_table[i, j]), end='')
                if k == 2:
                    print('                 |', end='')
            print()
    print('+-----------------' * env.reward.shape[1], end='')
    print('+')


# 보상 값의 절대값이 작은쪽으로 이동하도록 계산
def policy_extraction(env, agent, v_table, optimal_policy):
    gamma = 0.9
    for i in range(env.reward.shape[0]):
        for j in range(env.reward.shape[1]):
            temp = -1e+10
            for action in range(len(agent.action)):
                agent.set_pos([i, j])
                observation, reward, done = env.move(agent, action)
                if temp < reward + gamma * v_table[observation[0], observation[1]]:
                    optimal_policy[i] = action
                    temp = reward + gamma * v_table[observation[0], observation[1]]
    return optimal_policy


# 정책에 따른 이동방향 출력
def show_policy(policy, env):
    for i in range(env.reward.shape[0]):
        print('+----------' * env.reward.shape[1], end='');
        print('+');
        print('|', end='')
        for j in range(env.reward.shape[1]):
            if env.reward_list1[i][j] != 'goal':
                if policy[i, j] == 0:
                    print('   ↑   |', end='')
                elif policy[i, j] == 1:
                    print('   →   |', end='')
                elif policy[i, j] == 2:
                    print('   ↓   |', end='')
                elif policy[i, j] == 3:
                    print('   ←   |', end='')
            else:
                print('   *   |', end='')
        print()
    print('+----------' * env.reward.shape[1], end='');
    print('+')


def action_value_function(env, agent, act, G, max_step, now_step):
    gamma = 0.9  # 할인율

    if env.reward_list1[agent.pos[0]][agent.pos[1]] == 'goal':
        return env.goal  # 목적지일 경우
    if max_step == now_step:
        observation, reward, done = env.move(agent, act)  # 최대 이동 횟수 일경우
        G += agent.select_action_pr[act] * reward  # 누적 보상 합계
        return G
    else:
        pos1 = agent.get_pos()
        observation, reward, done = env.move(agent, act)  # 행동에 따른 결과
        G += agent.select_action_pr[act] * reward

        if done == True:
            if observation[0] < 0 or observation[0] >= env.reward.shape[0] or observation[1] < 0 or observation[1] >= \
                    env.reward.shape[1]:
                agent.set_pos(pos1)  # 밖으로 이동한 경우

        pos1 = agent.get_pos()

        for i in range(len(agent.action)):
            agent.set_pos(pos1)
            next_v = action_value_function(env, agent, i, 0, max_step, now_step + 1)  # 이동후 행동을 했을때의 보상 값
            G += agent.select_action_pr[i] * gamma * next_v
        return G
    # 각각의 행동에 따른 값 출력


def show_q_table(q_table, env):
    for i in range(env.reward.shape[0]):
        print('+----------------' * env.reward.shape[1], end='');
        print('+')
        for k in range(3):
            print('|', end='')
            for j in range(env.reward.shape[1]):
                if k == 0:
                    print('{0:10.2f}      |'.format(q_table[i, j, 0]), end='')
                if k == 1:
                    print('{0:6.2f}   {1:6.2f} |'.format(q_table[i, j, 3], q_table[i, j, 1]), end='')
                if k == 2:
                    print('{0:10.2f}      |'.format(q_table[i, j, 2]), end='')
            print()
    print('+----------------' * env.reward.shape[1], end='');
    print('+')


# 각각의 위치에서 가장 이득인 행동 출력
def show_q_table_arrow(q_table, env):
    for i in range(env.reward.shape[0]):
        print('+----------------' * env.reward.shape[1], end='');
        print('+')
        for k in range(3):
            print('|', end='')
            for j in range(env.reward.shape[1]):
                if k == 0:
                    if np.max(q[i, j, :]) == q[i, j, 0]:
                        print('        ↑      I', end='')
                    else:
                        print('                |', end='')
                if k == 1:
                    if np.max(q[i, j, :]) == q[i, j, 1] and np.max(q[i, j, :]) == q[i, j, 3]:
                        print('     ←  →     |', end='')
                    elif np.max(q[i, j, :]) == q[i, j, 1]:
                        print('          →    |', end='')
                    elif np.max(q[i, j, :]) == q[i, j, 3]:
                        print('       ←       |', end='')
                    else:
                        print('                |', end='')
                if k == 2:
                    if np.max(q[i, j, :]) == q[i, j, 2]:
                        print('        ↓      |', end='')
                    else:
                        print('                |', end='')
            print()
        print('+----------------' * env.reward.shape[1], end='');
        print('+')


env = Environment()
initial_position = np.array([0, 0])
agent = Agent(initial_position)
np.random.seed(0)
max_step_number = 8

for max_step in range(max_step_number):
    print('max_step ={}'.format(max_step))
    q_table = np.zeros((env.reward.shape[0], env.reward.shape[1], len(agent.action)))  # q table
    for i in range(env.reward.shape[0]):
        for j in range(env.reward.shape[1]):
            for action in range(len(agent.action)):
                agent.set_pos([i, j])  # 행동별 값 계산 하여 저장
                q_table[i, j, action] = action_value_function(env, agent, action, 0, max_step, 0)
    q = np.round(q_table, 2)
    print('\nQ-table')
    show_q_table(q, env)
    print('\n정책')
    show_q_table_arrow(q, env)


def policy_evaluation(env, agent, v_table, policy):
    while True:
        delta = 0
        temp_v = copy.deepcopy(v_table)
        for i in range(env.reward.shape[0]):
            for j in range(env.reward.shape[1]):
                agent.set_pos([i, j])
                action = policy[i, j]
                observation, reward, done = env.move(agent, action)
                v_table[i, j] = reward + gamma * v_table[observation[0], observation[1]]
        delta = np.max([delta, np.max(np.abs(temp_v - v_table))])
        if delta < 0.000001:
            break
    return v_table, delattr


def policy_improvement(env, agent, v_table, policy):
    pilicyStable = True
    for i in range(env.reward.shape[0]):
        for j in range(env.reward.shape[1]):
            old_action = policy[i, j]
            temp_action = 0
            temp_value = -1e+10

            for action in range(len(agent.action)):
                agent.set_pos([i, j])
                observation, reward, done = env.move(agent, action)
                if temp_value < reward + gamma * v_table[observation[0], observation[1]]:
                    temp_action = action
                    temp_value = reward + gamma * v_table[observation[0], observation[1]]
                if old_action != temp_action:
                    policyStable = False
                policy[i, j] = temp_action
    return policy, policyStable


np.random.seed(0)
env = Environment()
initial_position = np.array([0, 0])
agent = Agent(initial_position)
gamma = 0.0

v_table = np.random.rand(env.reward.shape[0], env.reward.shape[1])
policy = np.random.randint(0, 4, (env.reward.shape[0], env.reward.shape[1]))

max_iter_number = 20000
for iter_number in range(max_iter_number):
    v_table, delta = policy_evaluation(env, agent, v_table, policy)
    policy, policyStable = policy_improvement(env, agent, v_table, policy)
    show_v_table(v_table, env)
    show_policy(policy, env)

    if policyStable == True:
        break
