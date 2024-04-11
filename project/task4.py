from scipy.sparse import dok_matrix, block_diag, dok_matrix

from project.task3 import FiniteAutomaton, intersect_automata, transitive_closure
from task3 import paths_ends


def reachability_with_constraints(
    fa: FiniteAutomaton,
    constraints_fa: FiniteAutomaton,
    matrix_class=dok_matrix,
    matrix_class_id="dok",
) -> dict[int, set[int]]:

    m, n = constraints_fa.size(), fa.size()

    def get_front(s):
        front = matrix_class((m, m + n), dtype=bool)
        for i in constraints_fa.start_idxs():
            front[i, i] = True
        for i in range(m):
            front[i, s + m] = True
        return front

    def diag(mat):
        result = matrix_class(mat.shape, dtype=bool)
        for i in range(mat.shape[0]):
            for j in range(mat.shape[0]):
                if mat[j, i]:
                    result[i] += mat[j]
        return result

    labels = fa.labels() & constraints_fa.labels()
    result = {s: set() for s in fa.start_states}
    adj = {
        label: block_diag(
            (constraints_fa.basa[label], fa.basa[label]), format=matrix_class_id
        )
        for label in labels
    }

    for v in fa.start_idxs():
        front = get_front(v)
        for _ in range(m * n):
            front = sum(
                [matrix_class((m, m + n), dtype=bool)]
                + [diag(front @ adj[label]) for label in labels]
            )
            for i in constraints_fa.final_idxs():
                for j in fa.final_idxs():
                    if front[i, j + m]:
                        result[v].add(j)
    return result


def reachability_all_pairs(
    graph_fa,
    regex_fa,
    start_nodes,
    final_nodes,
    matrix_class=dok_matrix,
    matrix_class_id="dok",
) -> list[tuple[object, object]]:
    return paths_ends(
        graph_fa, regex_fa, matrix_class=matrix_class, matrix_class_id=matrix_class_id
    )
