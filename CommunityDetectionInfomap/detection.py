import matplotlib.colors as colors
from infomap import Infomap
import networkx as nx
import matplotlib.pyplot as plt


def findCommunities(G):
    """
    Compute the number of communites in the Network.

    See https://www.mapequation.org/assets/publications/mapequationtutorial.pdf

    Parameters
    ----------
    G : graph
        A networkx Graph.

    Returns
    -------
    count : integer
        Number of communities found.

    Examples
    --------
    A ray enters an air--water boundary at pi/4 radians (45 degrees).
    Compute exit angle.

    >>> import networkx as nx
    >>> g=nx.karate_club_graph()
    >>> findCommunities(g)
    5
    """
    im = Infomap("--two-level --directed")
    for e in G.edges():
      im.addLink(*e)
    im.run()
    communities = {}
    for node in im.tree:
      communities[node.node_id] = node.module_id

    nx.set_node_attributes(G, communities, 'community')
    print('There are found ', im.num_top_modules, 'communities.')
    return im.num_top_modules


def drawNetwork(G):
    """
    Draw the graph of detected communites.

    See https://www.mapequation.org/assets/publications/mapequationtutorial.pdf

    Parameters
    ----------
    G : graph
        A networkx Graph.

    Returns
    -------
    count : graph
        Returns the Network graph of detected communities.

    Examples
    --------
    A ray enters an air--water boundary at pi/4 radians (45 degrees).
    Compute exit angle.
    
    >>> import networkx as nx
    >>> g=nx.karate_club_graph()
    >>> drawNetwork(g)
    """
    pos = nx.spring_layout(G)
    communities = [v for k, v in nx.get_node_attributes(G, 'community').items()]
    numCommunities = max(communities) + 1
    cmapLight = colors.ListedColormap(['#a6cee3', '#b2df8a', '#fb9a99', '#fdbf6f', '#cab2d6'], 
    'indexed', numCommunities)
    cmapDark = colors.ListedColormap(['#1f78b4', '#33a02c', '#e31a1c', '#ff7f00', '#6a3d9a'], 
    'indexed', numCommunities)
    nx.draw_networkx_edges(G, pos)
    nodeCollection = nx.draw_networkx_nodes(G,
      pos = pos,
      node_color = communities, 
      cmap = cmapLight)
    darkColors = [cmapDark(v) for v in communities]
    nodeCollection.set_edgecolor(darkColors)
    for n in G.nodes():
      plt.annotate(n, xy = pos[n], textcoords = 'offset points', horizontalalignment = 'center',
        verticalalignment = 'center', xytext = [0, 2], color = cmapDark(communities[n]))
    plt.axis('off')
    plt.show()
