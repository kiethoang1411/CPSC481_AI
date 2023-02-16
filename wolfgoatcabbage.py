from search import *
# YOUR CODE GOES HERE

class WolfGoatCabbage:
    def __init__(self):
        self.initial = frozenset([frozenset(['F', 'W', 'G', 'C']), frozenset([])])
        self.goal = frozenset([frozenset([]), frozenset(['F', 'W', 'G', 'C'])])

    def goal_test(self, state):
        return state == self.goal

    def result(self, state, action):
        state = [set(s) for s in state] # convert state to a list of sets
        if 'F' in state[0]:
            first_set, second_set = 0, 1
        else:
            first_set, second_set = 1, 0
        if action == 'WG':
            assert 'W' in state[first_set] and 'G' in state[first_set]
            state[first_set].remove('W')
            state[second_set].add('W')
            state[first_set].remove('G')
            state[second_set].add('G')
        elif action == 'GC':
            assert 'G' in state[first_set] and 'C' in state[first_set]
            state[first_set].remove('G')
            state[second_set].add('G')
            state[first_set].remove('C')
            state[second_set].add('C')
        elif action == 'W':
            assert 'W' in state[first_set]
            state[first_set].remove('W')
            state[second_set].add('W')
        elif action == 'C':
            assert 'C' in state[first_set]
            state[first_set].remove('C')
            state[second_set].add('C')
        state = [frozenset(s) for s in state] # convert state back to a tuple of frozensets
        return tuple(state)

    def actions(self, state):
        state = [set(s) for s in state]
        possible_actions = []
        if 'F' in state[0]:
            first_set, second_set = 0, 1
        else:
            first_set, second_set = 1, 0
        for item in state[first_set]:
            if item != 'F':
                new_state = [set(s) for s in state]
                new_state[first_set].remove(item)
                new_state[second_set].add(item)
                if self.is_safe_state([frozenset(s) for s in new_state]):
                    possible_actions.append(item)
        return possible_actions

    def isGoodState(self, state):
        for side in state:
            if 'W' in side and 'G' in side and 'F' not in side:
                return False
            if 'G' in side and 'C' in side and 'F' not in side:
                return False
        return True

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
    
        
