from typing import List


class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        folders.sort()
        parents = []

        for folder in folders:
            i, j = 0, 1
            to_add = True
            while j < len(folder):
                if folder[j] == '/':
                    sp = folder[i:j]
                    if sp in parents:
                        to_add = False
                        break
                j += 1
            if to_add:
                parents.append(folder)
        return parents
