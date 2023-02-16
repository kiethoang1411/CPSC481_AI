from search import *


class WolfGoatCabbage(Problem):

    def __init__(self,initial=frozenset({'G', 'F', 'W', 'C'}),goal=set()):
        super().__init__(initial, goal)   
            
   # This is a method called goal_test, which takes a state as an argument and returns True if the state matches the goal state, False otherwise.
    def goal_test(self,state):
        if state == self.goal:
            return True
        else:
            return False

    # This is a method called actions, which takes a state as an argument and returns a list of valid actions that can be taken from that state.
    # It uses a hashmap to map each state to its valid actions.
    def actions(self,state): 
        hashmap = {
                    frozenset({'F', 'G', 'W', 'C'}):[{'F','G'}],
                    frozenset({'W', 'C'}):[{'F'}],
                    frozenset({'W', 'C','F'}):[{'W','F'},{'C','F'}],
                    frozenset({'W'}): [{'G','F'}],
                    frozenset({'C'}): [{'G','F'}],
                    frozenset({'G', 'F', 'C'}):[{'C','F'}],
                    frozenset({'G', 'F', 'W'}): [{'W','F'}],
                    frozenset({'G'}): [{'F'}],
                    frozenset({'G', 'F'}): [{'G','F'}]
        }
        # It loops over the hashmap, and if the given state matches one of the states in the hashmap, 
        # it returns the corresponding valid actions for that state.
        for i in hashmap:
            if state==i:
                return hashmap[i]

    # This is a method called result, which takes a state and an action as arguments and returns the resulting state after the given action is taken.
    def result(self, state, action):
        nextState = set()
        # It creates a copy of the current state to ensure that it is not modified.
        for i in state:
            nextState.add(i)
        # It applies the given action to the state by adding or removing the corresponding items from the set.
        x = [nextState.add(i) if i not in state else nextState.remove(i) for i in action]
        # It returns the resulting state as a frozenset.
        return frozenset(nextState)

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)