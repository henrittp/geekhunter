from typing import List


def process_input(contents: List[str]) -> List[int]:
    """Get Carlos' position in the simulation.

    Args:
        contents (list[str]): List of inputs containing the quantity of v elements, v elements,
        quantity of c elements and c elements.

    Returns:
        list[int]: List containing the positions Carlos would occupy in the ranking for each
        sales simulation.

    Raises:
        None
    """
    v_elements_qty = int(contents[0])
    v_elements = list(set([int(x) for x in contents[1].split(" ")]))
    c_elements_qty = int(contents[2]) if len(contents) > 3 else 0
    c_elements = (
        [int(x) for x in contents[3].split(" ")] if len(contents) > 3 else [int(x) for x in contents[2].split(" ")]
    )

    total_v_elements = sum(v_elements)

    ranking = sorted(v_elements, reverse=True)
    results = []
    for sales in c_elements:
        pos = len([x for x in ranking if x > sales]) + 1
        results.append(pos)
    return results


contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

results = process_input(contents)
for result in results:
    print(result)
