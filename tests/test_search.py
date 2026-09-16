from src.search import uniform_cost_search

def test_ucs_optimal_path():
    graph = {
        "Start": [("A", 2.0), ("B", 5.0)],
        "A": [("Goal", 3.0)],
        "B": [("Goal", 1.0)],
        "Goal": []
    }
    cost, path = uniform_cost_search(graph, "Start", "Goal")
    assert cost == 5.0
    assert path == ["Start", "A", "Goal"]

def test_ucs_unreachable_goal():
    graph = {
        "Start": [("A", 1.0)],
        "A": [],
        "Goal": []
    }
    cost, path = uniform_cost_search(graph, "Start", "Goal")
    assert cost == float("inf")
    assert path == []