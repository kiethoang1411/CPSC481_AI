from search import *


class WolfGoatCabbage(Problem):

    def __init__(self,initial=frozenset({'G', 'F', 'W', 'C'}),goal=set()):
        super().__init__(initial, goal)       
    def goal_test(self,state):
        if state == self.goal:
            return True
        else:
            return False

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
        for i in hashmap:
            if state==i:
                return hashmap[i]

    def result(self, state, action):
        nextState = set()
        for i in state:
            nextState.add(i)

        x = [nextState.add(i) if i not in state else nextState.remove(i) for i in action]
        return frozenset(nextState)

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)