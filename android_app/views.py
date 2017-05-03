from __future__ import print_function
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import sys
import json

			######################################

			##	##	######      ###   ###
			##	##	######      #### ####
			##########	####	    ## ### ##
			########## 	####	    ##  #  ##
		 	## 	## 	## 	    ##     ##
		     	## 	##      ##          ##     ##

			######################################


def index(request):
	return	HttpResponse('<html><body>Hello, World!</body></html>')

@csrf_exempt
def get_grades(request): # p_user, p_pass
	if request.method == 'POST':

		p_user = request.POST.get('p_user')
		p_pass = request.POST.get('p_pass')
		print(str(p_user) + " : " + str(p_pass))

		reload(sys)
		sys.setdefaultencoding('utf-8')

		driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
		driver.get("https://my.sdu.edu.kz/")
		elem = driver.find_element_by_name("username")
		elem.clear()
		elem.send_keys(str(p_user))
		password = driver.find_element_by_name("password")
		password.send_keys(str(p_pass))
		elem.send_keys(Keys.RETURN)
		password.send_keys(Keys.RETURN)
		
		driver.get("https://my.sdu.edu.kz/index.php?mod=grades")
		
		soup = BeautifulSoup(driver.page_source)
		grades_output = soup.find_all("td", {"class": "clsTd"})

		mat = []
		counter = 0
		grades = {}
		lect_counter = 0
		arr_strings = ['code', 'n', 'p', 'l', 'course_name', 'cr', 'ects', 'abs', 'mt1', 'mt2', 'fin', 'avg', 'lg']
		for i in range(13, len(grades_output)):
			if(i % 13 == 0 and i > 13):	
				grades[lect_counter] = row	
			if(i % 13 == 0):	
				lect_counter += 1
				row = {}	

			## this is right output
			#print (grades_output[i].text.strip(), end=", ")
	
			row[arr_strings[i % 13]] = grades_output[i].text.strip()
		

			## num 1	
			#mat[counter].append(grades_output[i].text.strip())
			#counter += 1
			#if(i % 13 == 12):
			#	counter = 0
	
			## num 2
			#mat.append(grades_output[i].text.strip())

		## num 1 & 2
		#print(mat)
		grades['len'] = lect_counter - 1 ### optional for others
		#print(json.dumps(grades))
		driver.close()
		#driver.implicitly_wait(5)
		return HttpResponse(json.dumps(grades))
					
	else:
		return HttpResponse('hello');
