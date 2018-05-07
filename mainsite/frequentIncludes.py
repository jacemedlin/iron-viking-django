# -*- coding: utf-8 -*-
"""
Created on Mon May  7 04:46:11 2018

@author: Jace
"""
from newsletter.forms import Subscribe
import ambassadors.ambassadorFunctions as af

includes = {'ambassador_list': af.get_featured_ambassadors(), 'subscribe_form':Subscribe}
active = "active"