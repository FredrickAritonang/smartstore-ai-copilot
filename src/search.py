import heapq
from typing import Dict, List, Tuple

def uniform_cost_search(
    graph: Dict[str, List[Tuple[str, float]]], 
    start: str, 
    goal: str
) -> Tuple[float, List[str]]:
    """
    Algoritma Uniform Cost Search (UCS) untuk memetakan alur eskalasi tiket penanganan komplain.
    """
    pq: List[Tuple[float, List[str]]] = [(0.0, [start])]
    visited: set = set()

    while pq:
        current_cost, path = heapq.heappop(pq)
        current_node = path[-1]

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            return current_cost, path

        for neighbor, cost in graph.get(current_node, []):
            if neighbor not in visited:
                total_cost = current_cost + cost
                heapq.heappush(pq, (total_cost, path + [neighbor]))

    return float("inf"), []


if __name__ == "__main__":
    # Graf Alur Penanganan Komplain E-Commerce SmartStore AI
    customer_service_graph: Dict[str, List[Tuple[str, float]]] = {
        "Pesan_Masuk": [("Bot_Auto_Check", 1.0), ("Human_Agent_L1", 10.0)],
        "Bot_Auto_Check": [("Cek_SOP_Retur", 2.0), ("Cek_Status_Kurir", 1.5)],
        "Cek_Status_Kurir": [("Info_Lokasi_Paket", 1.0)],
        "Cek_SOP_Retur": [("Auto_Approve_Refund", 2.0), ("Human_Agent_L2", 15.0)],
        "Info_Lokasi_Paket": [("Tiket_Selesai", 0.5)],
        "Auto_Approve_Refund": [("Tiket_Selesai", 1.0)],
        "Human_Agent_L1": [("Human_Agent_L2", 5.0)],
        "Human_Agent_L2": [("Tiket_Selesai", 5.0)],
        "Tiket_Selesai": []
    }

    start_stage = "Pesan_Masuk"
    target_stage = "Tiket_Selesai"

    cost, path = uniform_cost_search(customer_service_graph, start_stage, target_stage)

    print("=== EVALUASI BASELINE SEARCH (UCS) - SMARTSTORE AI ===")
    print(f"Tahap Awal    : {start_stage}")
    print(f"Tahap Akhir   : {target_stage}")
    print(f"Jalur Tercepat : {' -> '.join(path)}")
    print(f"Total Waktu   : {cost} Menit")