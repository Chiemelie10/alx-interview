#!/usr/bin/python3
"""This module defines a function that opens locked boxes."""


def canUnlockAll(boxes):
    """
    Returns True if all boxes can be opened. Otherwise, returns
    false.
    """

    unlocked_keys = []
    opened_boxes = {}
    opened = True

    for i in range(len(boxes)):
        if i == 0:
            unlocked_keys += boxes[i]
            opened_boxes[i] = True

        if opened is False:
            opened_boxes[i] = False
            if i in unlocked_keys:
                opened = True
                unlocked_keys += boxes[i]
                opened_boxes[i] = True
                # unlocked_keys.remove(i)

                for key, value in opened_boxes.items():
                    if key in unlocked_keys and value is False:
                        unlocked_keys += boxes[key]
                        opened_boxes[key] = True
                        # unlocked_keys.remove(key)
        elif i != 0 and i in unlocked_keys:
            unlocked_keys += boxes[i]
            opened_boxes[i] = True
            # unlocked_keys.remove(i)
        elif i != 0 and i not in unlocked_keys:
            opened = False
            opened_boxes[i] = False

    if False in opened_boxes.values():
        return False

    return True
