#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:14:15 2023

@author: owethuphekani
"""

def final_months_taken_to_save_downpayment(home_cost, annual_salary, percentage_saved, annual_savings_rate, annual_income_raise, property_appreciation):
    down_payment = (0.2 * home_cost)
    monthly_salary = (annual_salary/12)
    salary_taxes = monthly_salary * (1 - 0.085 - 0.22 - 0.0765)
    monthly_savings = (percentage_saved * salary_taxes)
    
    current_savings = 0
    r = annual_savings_rate
    months = 0 
    
    while current_savings < down_payment:
        current_savings += current_savings * (r/12) + monthly_savings
        months += 1
        if months % 12 == 0: #should i use 6/12?
            annual_salary = annual_salary * (1 + annual_income_raise)
            monthly_salary = (annual_salary * (1 - 0.085 - 0.22 - 0.0765)) / 12
            monthly_savings = percentage_saved * monthly_salary
            home_cost = home_cost * (1 + property_appreciation)
            down_payment = 0.2 * home_cost
        
    return months
print('Months after annaul raise: ', final_months_taken_to_save_downpayment(668000,75000,0.25,0.034, 0.0125, 0.05))

import urllib.request
bathroom_code_input = urllib.request.urlopen('https://raw.githubusercontent.com/AlR0d/courses/main/4465/bsdeg_keypad.txt').read().decode('utf-8')

security_keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [None, 0, None]]