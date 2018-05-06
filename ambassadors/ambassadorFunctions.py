# -*- coding: utf-8 -*-
"""
Created on Sat May  5 23:02:26 2018

@author: Jace
"""

from .models import Ambassador

def get_featured_ambassadors():
	featured_ambassadors = Ambassador.objects.filter(is_featured = True)
	featured_ambassadors = featured_ambassadors.order_by('?')[:4]
	return featured_ambassadors

def num_featured(ambassador_list):
	num_ambassadors = (0,)
	count = 1
	for i in ambassador_list:
		num_ambassadors += (count,)
		count += 1
		print(count)
	return num_ambassadors