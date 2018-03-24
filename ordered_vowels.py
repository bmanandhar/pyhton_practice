#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:27:51 2018

@author: bijayamanandhar
"""

def ordered_vowel_words(str):
	ordered_words = ""
	for word in str.split():
		if ordered_vowel_word(word):
			ordered_words += word + " "
	return ordered_words.strip()

def ordered_vowel_word(word):
	vowels = 'aeiou'
	last_vowel = ''
	for char in word:
		if char in vowels:
			if char >= last_vowel:
				last_vowel = char
			else:
				return False
	return True
    
print(ordered_vowel_words("These are complicated stuff"))    
print(ordered_vowel_words("c"))    
    

print("Tests for ordered vowel words")
print(ordered_vowel_words("amends state human") == "amends state")
print(ordered_vowel_words("These are complicated stuff") == "These are stuff")
print(ordered_vowel_words("afoot") == "afoot")
print(ordered_vowel_words("ham got hit") == "ham got hit")
print(ordered_vowel_words("crypt") == "crypt")
print(ordered_vowel_words("o") == "o")
print(ordered_vowel_words("tamely") == "tamely")
phrase = "this is a test of the vowel ordering system"
result = "this is a test of the system"
print(ordered_vowel_words(phrase) == result)