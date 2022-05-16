
import networkx as nx
from CommunityDetectionInfomap.detection import findCommunities
g = nx.karate_club_graph()


def test_findCommunities():
    "check if the community count is equevalt to already existing one (5)"
    assert findCommunities(g) == 5
