#!/usr/bin/env python
import numpy as np
from scipy.linalg import expm
from lab3_header import *

"""
Use 'expm' for matrix exponential.
Angles are in radian, distance are in meters.
"""

def Get_MS():
    # =================== Your code starts here ====================#
    # Fill in the correct values for S1~6, as well as the M matrix
    w_1 = np.array([0,0,1]).T
    w_2 = np.array([0,1,0]).T
    w_3 = np.array([0,1,0]).T
    w_4 = np.array([0,1,0]).T
    w_5 = np.array([1,0,0]).T
    w_6 = np.array([0,1,0]).T

    q_1 = np.array([-0.150, 0.150, 0.162]).T
    q_2 = np.array([-0.150, 0.270, 0.162]).T
    q_3 = np.array([ 0.094, 0.270, 0.162]).T
    q_4 = np.array([ 0.307, 0.177, 0.162]).T
    q_5 = np.array([ 0.307, 0.260, 0.162]).T
    q_6 = np.array([ 0.390, 0.260, 0.162]).T

    v_1 = np.cross(w_1, (-1*q_1))
    v_2 = np.cross(w_2, (-1*q_2))
    v_3 = np.cross(w_3, (-1*q_3))
    v_4 = np.cross(w_4, (-1*q_4))
    v_5 = np.cross(w_5, (-1*q_5))
    v_6 = np.cross(w_6, (-1*q_6))

    S_1 = get_S(w_1.T,v_1.T)
    S_2 = get_S(w_2.T,v_2.T)
    S_3 = get_S(w_3.T,v_3.T)
    S_4 = get_S(w_4.T,v_4.T)
    S_5 = get_S(w_5.T,v_5.T)
    S_6 = get_S(w_6.T,v_6.T)

    S = np.array([S_1,S_2,S_3,S_4,S_5,S_6])

    M = np.array([[0, -1,  0, 0.390],
                  [0,  0, -1, 0.402],
                  [1,  0,  0, 0.220],
                  [0,  0,  0,     1]])


    # ==============================================================#
    return M, S

def get_S(w, v):
    return np.array([[      0, -1*w[2],    w[1], v[0]],
                     [   w[2],       0, -1*w[0], v[1]],
                     [-1*w[1],    w[0],       0, v[2]],
                     [      0,       0,       0,    0]
                    ])


"""
Function that calculates encoder numbers for each motor
"""
def lab_fk(theta1, theta2, theta3, theta4, theta5, theta6):

    # Initialize the return_value
    return_value = [None, None, None, None, None, None]

    # =========== Implement joint angle to encoder expressions here ===========
    print("Foward kinematics calculated:\n")

    # =================== Your code starts here ====================#
    M, S = Get_MS()
    T = M
    theta = [theta1, theta2, theta3, theta4, theta5, theta6]
    for i in range(5,-1,-1):
        T = np.matmul(expm(S[i]*theta[i]),T)



    # ==============================================================#

    print(str(T) + "\n")

    return_value[0] = theta1 + PI
    return_value[1] = theta2
    return_value[2] = theta3
    return_value[3] = theta4 - (0.5*PI)
    return_value[4] = theta5
    return_value[5] = theta6

    return return_value
