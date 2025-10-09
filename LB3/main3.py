from typing import Callable, Dict, List
from collections import namedtuple


Tree = Dict[str, List["Tree"]]


def left_branch(root: int) -> int:
    """Левая ветвь"""
    return root * 2 + 1


def right_branch(root: int) -> int:
    """Правая ветвь"""
    return 2 * root - 1


def gen_bin_tree(
    height: int = 6,
    root: int = 9,
    l_b: Callable[[int], int] = left_branch,
    r_b: Callable[[int], int] = right_branch,
) -> Tree:
    """Рекурсивное построение бинарного дерева."""
    if height < 0:
        raise ValueError("Height must be >= 0")

    if height == 0:
        return {str(root): []}

    return {
        str(root): [
            gen_bin_tree(height - 1, l_b(root), l_b, r_b),
            gen_bin_tree(height - 1, r_b(root), l_b, r_b),
        ]
    }


# ===== Альтернативная структура =====

Node = namedtuple("Node", ["value", "left", "right"])


def gen_bin_tree_node(
    height: int,
    root: int,
    l_b: Callable[[int], int],
    r_b: Callable[[int], int],
):
    """Бинарное дерево через namedtuple."""
    if height < 0:
        return None
    if height == 0:
        return Node(root, None, None)

    return Node(
        root,
        gen_bin_tree_node(height - 1, l_b(root), l_b, r_b),
        gen_bin_tree_node(height - 1, r_b(root), l_b, r_b),
    )