'''
In a mystic dungeon, n magicians are standing in a line. Each magician has an attribute that gives you energy. Some magicians can give you negative energy, which means taking energy from you.
You have been cursed in such a way that after absorbing energy from magician i, you will be instantly transported to magician (i + k). This process will be repeated until you reach the magician where (i + k) does not exist.
In other words, you will choose a starting point and then teleport with k jumps until you reach the end of the magicians' sequence, absorbing all the energy during the journey.
You are given an array energy and an integer k. Return the maximum possible energy you can gain.
'''

def maximumEnergy(energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        dp = {}
        len_energy = len(energy)
        for i in range(len_energy-1, -1, -1):
            if i + k >= len_energy:
                dp[i] = energy[i]
            else:
                dp[i] = dp[i+k] + energy[i]
        return max(dp.values())
        
        
print(maximumEnergy([8, -5], 1))

