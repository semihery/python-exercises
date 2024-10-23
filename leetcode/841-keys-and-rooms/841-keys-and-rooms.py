class Solution(object):
    def canVisitAllRooms(self, rooms):
        visitableRooms = [0] * len(rooms)
        visitableRooms[0] = 1
        visitedRooms = 0
        i = 0

        while True:
            visitableRooms[i] = 2
            visitedRooms += 1
            for x in rooms[i]:
                if visitableRooms[x] == 0:
                    visitableRooms[x] = 1

            try: i = visitableRooms.index(1)
            except: break
        
        if visitedRooms == len(rooms):
            return True
        else:
            return False
            
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        