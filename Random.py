#! /usr/bin/env python3

import math
import numpy as np
import sys

#################
# Random class
#################
# class that can generate random numbers
class Random:
    """A random number generator class"""

    # initialization method for Random class
    def __init__(self, seed = 5555):
        self.seed = seed
        self.m_v = np.uint64(4101842887655102017)
        self.m_w = np.uint64(1)
        self.m_u = np.uint64(1)
        
        self.m_u = np.uint64(self.seed) ^ self.m_v
        self.int64()
        self.m_v = self.m_u
        self.int64()
        self.m_w = self.m_v
        self.int64()

    # function returns a random 64 bit integer
    def int64(self):
        with np.errstate(over='ignore'):
            self.m_u = np.uint64(self.m_u * np.uint64(2862933555777941757) + np.uint64(7046029254386353087))
        self.m_v ^= self.m_v >> np.uint64(17)
        self.m_v ^= self.m_v << np.uint64(31)
        self.m_v ^= self.m_v >> np.uint64(8)
        self.m_w = np.uint64(np.uint64(4294957665)*(self.m_w & np.uint64(0xffffffff))) + np.uint64((self.m_w >> np.uint64(32)))
        x = np.uint64(self.m_u ^ (self.m_u << np.uint64(21)))
        x ^= x >> np.uint64(35)
        x ^= x << np.uint64(4)
        with np.errstate(over='ignore'):
            return (x + self.m_v)^self.m_w

    # function returns a random floating point number between (0, 1) (uniform)
    def rand(self):
        return 5.42101086242752217E-20 * self.int64()

    # function returns a random integer (0 or 1) according to a Bernoulli distr.
    def Bernoulli(self, p=0.5):
        if p < 0. or p > 1.:
            raise ValueError("Probability must be between 0 and 1.")
        
        R = self.rand()

        if R < p:
            return 1
        else:
            return 0

    def Normal(self, mu=0.0, sigma=1.0, size=None):
        if size is None:
            return mu + sigma * math.sqrt(-2.0 * math.log(self.rand())) * math.cos(2.0 * math.pi * self.rand())
        else:
            return np.array([mu + sigma * math.sqrt(-2.0 * math.log(self.rand())) * math.cos(2.0 * math.pi * self.rand()) for _ in range(np.prod(size))]).reshape(size)


    def Random_Range(self,a, b, size=None):
        if size is None:
            return (self.rand() * abs(b - a)) + min(a, b)
        else:
            return np.array([(self.rand() * abs(b - a)) + min(a, b) for _ in range(np.prod(size))]).reshape(size)

