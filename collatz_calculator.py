def get_immediate_parents(x):

    if x == 0:
        return []

    #  3p-1 = x is valid
    if ((x - 1) /3) % 1.0 == 0:

        if int((x-1)/3) != 1 and int((x-1)/3) % 2 != 0:

            return [2*x, int((x-1)/3)]

        else:

            return [2*x]

    elif x != 0:

        return [2*x]

    else:

        return []

def calc_all_parents(x,maximum):
    for p in get_immediate_parents(x):
        # record this relationship
        if p not in tree[x] and p != 0:
            tree[x].append(p)

            # get the parents of the parent
            if p < maximum:
                calc_all_parents(p,maximum)

tree = None
def generate_tree(child,maximum):
    global tree
    tree = {}

    for i in range(maximum):
        tree[i] = []

    calc_all_parents(child,maximum)
    
# generate_tree(1,100)
# print(tree)