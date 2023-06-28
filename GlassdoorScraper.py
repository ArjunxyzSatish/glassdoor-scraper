#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 12:02:53 2023

@author: Arjun Satish
"""

# JobTitle
# Salary
# Job Description
# Rating
# Company Name
# Location
# Size
# Founded
# Industry
# Competitors

from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.by import By
import pandas as pd
import time
import sys

jobs = []

def scrapeJobs(term, location, numJobs):
    driver = webdriver.Firefox()
    
    keyword = term.replace(" ", "-")
    
    targetUrl = 'https://www.glassdoor.com/Job/' + location + '-' + keyword + '-jobs-SRCH_IL.0,5_IN115_KO6,18.htm?clickSource=searchBox'

    driver.get(targetUrl)
    time.sleep(4)
    
    page = 1
    
    pageFooter = driver.find_element(By.CLASS_NAME, 'paginationFooter').text
    
    last_space_index = pageFooter.rfind(' ')
    
    pageMax = int(pageFooter[last_space_index + 1:])
    
    
    flag = 0
    
    while(len(jobs) < numJobs):
        if(flag == 1):
            break
        
        jobListings = driver.find_elements(By.XPATH, '//ul[@class="hover p-0 my-0  css-7ry9k1 exy0tjh5"]/li')
        
        for i in range(0, len(jobListings)):
            if(len(jobs) == numJobs):
                print('Got what we need.')
                sys.exit()
            
            try:
                jobListings[i].click()
                time.sleep(2)
                
                try:
                    title = driver.find_element(By.XPATH, '//div[@class="css-1vg6q84 e1tk4kwz4"]').text
                except: 
                    title = ''
            
                try:
                    company = driver.find_element(By.XPATH, '//div[@class="css-87uc0g e1tk4kwz1"]').text
                except:
                    company = ''
                try:
                    salary = jobListings[i].find_element(By.CLASS_NAME, 'salary-estimate').text
                except: 
                    salary = ''            
            
                try:
                    rating = driver.find_element(By.XPATH, '//span[@class="css-1m5m32b e1tk4kwz2"]').text
                except:
                    rating = ''
                
                try:
                    jobDesc = driver.find_element(By.XPATH, '//div[@class="jobDescriptionContent desc"]').text
                except: 
                    jobDesc = ''
            
                try:
                    location = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div/div/div[1]/div[3]').text
                except:
                    location = ''
         
                try:
                    founded = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[2]/div/div/div[1]/div/div[2]/span[2]').text
                except:
                    founded = ''  
            
                try:
                    industry = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[2]/div/div/div[1]/div/div[4]/span[2]').text
                except: 
                    industry = ''
            
                try:
                    sector = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[2]/div/div/div[1]/div/div[5]/span[2]').text
                except: 
                    sector = ''
            
                try:
                    revenue = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[2]/div/div/div[1]/div/div[6]/span[2]').text
                except: 
                    revenue = ''
            
                try:
                    size = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[2]/div/div/div[1]/div/div[1]/span[2]').text
                except:
                    size = ''
                
                try:
                    ownership = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[2]/div/div/div[1]/div/div[3]/span[2]').text
                except:
                    ownership = ''
            
                jobs.append({"Job Title": title,
                         "Company Name": company,
                         "Salary Estimate": salary,
                         "Rating": rating,
                         "Job Description": jobDesc,
                         "Location": location,
                         "Founded": founded,
                         "Industry": industry,
                         "Sectory": sector,
                         "Revenue": revenue,
                         "Size": size,
                         "Type of Ownership": ownership})
             
                
            except:
                close = driver.find_element(By.XPATH, '//button[@class="e1jbctw80 ei0fd8p1 css-1n14mz9 e1q8sty40"]')
                close.click()
                
        try:
            driver.find_element(By.XPATH, '//button[@class="nextButton job-search-1iiwzeb e13qs2072"]').click()
            time.sleep(2)
            print("Thats all in this page. Checking the next page...")
            page += 1
            if(page == pageMax + 1):
                flag = 1
                print("No more jobs on site")
                sys.exit()
        except:
            print("No more jobs")
            break
        
    return(pd.DataFrame(jobs))





  





