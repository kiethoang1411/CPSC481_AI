from search import *
# YOUR CODE GOES HERE

class WolfGoatCabbage:
    def __init__(self):
        self.initial = frozenset([frozenset(['F', 'W', 'G', 'C']), frozenset([])])
        self.goal = frozenset([frozenset([]), frozenset(['F', 'W', 'G', 'C'])])

    def goal_test(self, state):
        return state == self.goal

    def result(self, state, action):
        state = [set(s) for s in state]
        if 'F' in state[0]:
            src, dest = 0, 1
        else:
            src, dest = 1, 0
        if action == 'WG':
            assert 'W' in state[src] and 'G' in state[src]
            state[src].remove('W')
            state[dest].add('W')
            state[src].remove('G')
            state[dest].add('G')
        elif action == 'GC':
            assert 'G' in state[src] and 'C' in state[src]
            state[src].remove('G')
            state[dest].add('G')
            state[src].remove('C')
            state[dest].add('C')
        elif action == 'W':
            assert 'W' in state[src]
            state[src].remove('W')
            state[dest].add('W')
        elif action == 'C':
            assert 'C' in state[src]
            state[src].remove('C')
            state[dest].add('C')
        state = [frozenset(s) for s in state]
        return tuple(state)

    def actions(self, state):
        state = [set(s) for s in state]
        possible_actions = []
        if 'F' in state[0]:
            src, dest = 0, 1
        else:
            src, dest = 1, 0
        for item in state[src]:
            if item != 'F':
                new_state = [set(s) for s in state]
                new_state[src].remove(item)
                new_state[dest].add(item)
                if self.is_safe_state([frozenset(s) for s in new_state]):
                    possible_actions.append(item)
        return possible_actions

    def is_safe_state(self, state):
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
    
        
'''
    class EightPuzzle(Problem):
    """ The problem of sliding tiles numbered from 1 to 8 on a 3x3 board, where one of the
    squares is a blank. A state is represented as a tuple of length 9, where  element at
    index i represents the tile number  at index i (0 if it's an empty square) """

    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)

    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""

        return state.index(0)

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = self.find_blank_square(state)

        if index_blank_square % 3 == 0:
            possible_actions.remove('LEFT')
        if index_blank_square < 3:
            possible_actions.remove('UP')
        if index_blank_square % 3 == 2:
            possible_actions.remove('RIGHT')
        if index_blank_square > 5:
            possible_actions.remove('DOWN')

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal

    def check_solvability(self, state):
        """ Checks if the given state is solvable """

        inversion = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if (state[i] > state[j]) and state[i] != 0 and state[j] != 0:
                    inversion += 1

        return inversion % 2 == 0

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is 
        h(n) = number of misplaced tiles """

        return sum(s != g for (s, g) in zip(node.state, self.goal))
 '''