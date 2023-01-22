import matplotlib.pyplot as plt

tree_connections = []

def draw():
    plt.axes().set_aspect("equal")
    for l in tree_connections:
        plt.plot([l[0], l[2]], [l[1], l[3]], 'black', linewidth='1')
    plt.gcf().set_size_inches(10, 10)
    plt.xlim(min([r[0] for r in tree_connections]), max([r[2] for r in tree_connections]))
    plt.ylim(min([r[1] for r in tree_connections]), max([r[3] for r in tree_connections]))
    plt.savefig("fig.png")

if __name__ == "__main__":
    with open("../cpp/tree_connections.txt") as f:
        for l in [l.rstrip() for l in f]:
            tree_connections.append([float(x) for x in l.split(" ")])

    draw()
