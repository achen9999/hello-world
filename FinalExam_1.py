# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 09:27:24 2019

@author: chenan1
"""
##Problem 3
# =============================================================================
# def sum_digits(s):
#     """ assumes s a string
#         Returns an int that is the sum of all of the digits in s.
#           If there are no digits in s it raises a ValueError exception. """
#     answer = 0
#     iferror = True
#     digits = ['1','2','3','4','5','6','7','8','9','0']
#     for i in s:
#         if i in digits:
#             answer += int(i)
#             iferror = False
#     if iferror == True:
#         raise ValueError
#     return answer
# 
# print(sum_digits('030057as!'))
# =============================================================================

## Problem 4
# =============================================================================
# def primes_list(N):
#     '''
#     N: an integer
#     Returns a list of prime numbers
#     '''
#     primes = []
#     for i in range(2,N+1):
#         primeInd = True
#         for prime in primes:
#             if i % prime == 0:
#                 primeInd = False
#                 break
#         if primeInd == True:
#             primes.append(i)
#     return primes
# 
# print(primes_list(40))
# =============================================================================

##Problem 5
# =============================================================================
# def dict_interdiff(d1, d2):
#     '''
#     d1, d2: dicts whose keys and values are integers
#     Returns a tuple of dictionaries according to the instructions above
#     '''
#     intersect, diff = {}, {}
#     d1c = d1.copy()
#     d2c = d2.copy()
#     
#     for key in d1c:
#         try:
#             intersect[key] = f(d1c[key],d2c.pop(key))
# 
#         except KeyError:
#             diff[key] = d1c[key]
#             
#     for key2 in d2c:
#         diff[key2] = d2c[key2]
#     
#     return (intersect, diff)
# 
# def f(a,b):
#     return a+b
# 
# d1 = {1:30, 2:20, 3:30, 5:80}
# d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
# 
# print(dict_interdiff(d1, d2))
# =============================================================================

##Problem 6
# =============================================================================
# class USResident(Person):
#     """ 
#     A Person who resides in the US.
#     """
#     def __init__(self, name, status):
#         """ 
#         Initializes a Person object. A USResident object inherits 
#         from Person and has one additional attribute:
#         status: a string, one of "citizen", "legal_resident", "illegal_resident"
#         Raises a ValueError if status is not one of those 3 strings
#         """
#         Person.__init__(self, name)
#         self.status = status
#         if status not in ['citizen','legal_resident','illegal_resident']:
#             raise ValueError
#         
#     def getStatus(self):
#         """
#         Returns the status
#         """
#         return self.status
# =============================================================================
    
##problem 7
# =============================================================================
# class Container(object):
#     """ Holds hashable objects. Objects may occur 0 or more times """
#     def __init__(self):
#         """ Creates a new container with no objects in it. I.e., any object 
#             occurs 0 times in self. """
#         self.vals = {}
#     def insert(self, e):
#         """ assumes e is hashable
#             Increases the number times e occurs in self by 1. """
#         try:
#             self.vals[e] += 1
#         except:
#             self.vals[e] = 1
#     def __str__(self):
#         s = ""
#         for i in sorted(self.vals.keys()):
#             if self.vals[i] != 0:
#                 s += str(i)+":"+str(self.vals[i])+"\n"
#         return s
#     
# 
# class ASet(Container):
#     def remove(self, e):
#         """assumes e is hashable
#            removes e from self"""
#         try:
#             del self.vals[e]
#         except:
#             pass
# 
#     def is_in(self, e):
#         """assumes e is hashable
#            returns True if e has been inserted in self and
#            not subsequently removed, and False otherwise."""
#         if e in self.vals.keys():
#             return True
#         else:
#             return False
#         
# d1 = ASet()
# d1.insert(4)
# print(d1.is_in(4))
# d1.insert(5)
# print(d1.is_in(5))
# d1.remove(5)
# print(d1.is_in(5))
# =============================================================================
