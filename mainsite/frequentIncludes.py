# -*- coding: utf-8 -*-
"""
Created on Mon May  7 04:46:11 2018

@author: Jace
"""
import ambassadors.ambassadorFunctions as af

active = "active"

def returnIncludes():
		i = 0;
		a_list = list(af.get_featured_ambassadors())
		listList = []
		a_key = "ambassador_list"
		for a in a_list:
			listList.append([a_list[i],i])
			i += 1
			
		includes = {a_key: a_list}
		return includes