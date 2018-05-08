# -*- coding: utf-8 -*-
"""
Created on Mon May  7 03:15:13 2018

@author: Jace
"""

from django import forms
from .models import Subscription
	
class Subscribe(forms.ModelForm):
	class Meta:
		model = Subscription
		fields = ['s_name','s_email', 'wants_help', 'wants_newsletter']
	
