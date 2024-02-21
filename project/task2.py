from pyformlang.regular_expression import Regex
from pyformlang.finite_automaton import DeterministicFiniteAutomaton
from pyformlang.finite_automaton import NondeterministicFiniteAutomaton
from pyformlang.finite_automaton import State, Epsilon
from pyformlang.finite_automaton import Symbol
import networkx as nx
from typing import Set
import copy


def regex_to_dfa(regex: str) -> DeterministicFiniteAutomaton or None:
    try:
        regex = Regex(regex)
    except:
        print("Invalid regex format")
        return None

    nfa = regex.to_epsilon_nfa()
    dfa = nfa.to_deterministic()
    return dfa


def graph_to_nfa(
    graph: nx.MultiDiGraph, start_nodes: Set[int] = None, final_nodes: Set[int] = None
) -> NondeterministicFiniteAutomaton:
    nfa = NondeterministicFiniteAutomaton()

    if len(start_nodes) == 0 or start_nodes is None:
        start_nodes = graph.nodes
    else:
        start_nodes = []

    if len(final_nodes) == 0 or final_nodes is None:
        final_nodes = graph.nodes
    else:
        final_nodes = []

    for node in graph.nodes:
        graph.nodes(data=True)[node]["is_start"] = False
        graph.nodes(data=True)[node]["is_final"] = False

    for node in start_nodes:
        graph.nodes(data=True)[node]["is_start"] = True
        nfa.add_start_state(State(node))

    for node in final_nodes:
        graph.nodes(data=True)[node]["is_final"] = True
        nfa.add_final_state(State(node))

    eps_edges = []

    for edge in graph.edges(data=True):
        if edge[2]["label"] == "eps":
            eps_edges.append(edge)
        else:
            nfa.add_transition(State(edge[0]), Symbol(edge[2]["label"]), State(edge[1]))

    for e in eps_edges:
        e_to = e[1]
        e_from = e[0]
        for e2 in graph.edges(data=True):
            if e2[0] == e_to:
                nfa.add_transition(State(e_from), Symbol(e2[2]["label"]), State(e2[1]))

    return nfa