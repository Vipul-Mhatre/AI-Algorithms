class AlphaBetaPruning:
    def __init__(self, depth, maximizing_player=True):
        self.depth = depth
        self.maximizing_player = maximizing_player  

    def alpha_beta(self, node, depth, alpha, beta, is_maximizing_player):
        if depth == 0 or not node.get_children():
            return node.evaluate()

        if is_maximizing_player:
            max_eval = float('-inf')
            for child in node.get_children():
                eval = self.alpha_beta(child, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  
            return max_eval
        else:
            min_eval = float('inf')
            for child in node.get_children():
                eval = self.alpha_beta(child, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  
            return min_eval

class Node:
    def __init__(self, state, children=None):
        self.state = state
        self.children = children or []

    def evaluate(self):
        return self.state 

    def get_children(self):
        return self.children

if __name__ == "__main__":
    leaf1 = Node(state=3)
    leaf2 = Node(state=12)
    leaf3 = Node(state=8)
    leaf4 = Node(state=2)

    internal1 = Node(state=0, children=[leaf1, leaf2])  
    internal2 = Node(state=0, children=[leaf3, leaf4])  
    root = Node(state=0, children=[internal1, internal2])

    alpha_beta_pruning = AlphaBetaPruning(depth=3, maximizing_player=True)
    best_value = alpha_beta_pruning.alpha_beta(root, 3, float('-inf'), float('inf'), True)
    print(f"The best value is: {best_value}")