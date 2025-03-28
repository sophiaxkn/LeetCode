from itertools import count


class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        There are n employees in a company, numbered from 0 to n - 1.
        Each employee i has worked for hours[i] hours in the company.
        The company requires each employee to work for at least target hours.
        You are given a 0-indexed array of non-negative integers hours
        of length n and a non-negative integer target.
        Return the integer denoting the number of employees who worked at least target hours.
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        counter = 0

        for employeeId, employeeHours in enumerate(hours):
            if employeeHours >= target:
                counter += 1
        return counter