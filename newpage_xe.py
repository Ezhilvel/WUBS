# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 11:00:25 2018

@author: admin2
"""

"""
Created on Mon Jun 25 12:00:04 2018
@author: admin2
"""


#importing libs
import selenium
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver 
from pprint import pprint
import numpy as np
import pandas as pd
import numpy
from numpy import vstack
from numpy import hstack
import re
import csv

c_ccy = pd.read_csv("E:\WUBS\c_ccy.csv", sep=',')

###########################
#run from this 
driver = webdriver.Chrome("E:\WUBS\chromedriver.exe") 

#list institutes
urls = "https://www.flywire.com/"
driver.get(urls)

##-----------------------------------------------------------------------------------------------------------------------------------
driver.switch_to.window(driver.window_handles[0])
action = ActionChains(driver)
link = driver.find_element_by_tag_name('a')
action.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()

sleep(2)
##-----------------------------------------------------------------------------------------------------------------------------------

payment_method = []
pt_amount = []
country = []
institute_name = []
CCY_Full = []
fx_rate = []
EUR_Count= 0

To_CCY = "USD"
amount = 5000
amount_int = "5000"

Currency_List = ['FJD',	'MXN',	'STD',	'EUR',	'SCR',	'TVD',	'CDF',	'BBD',	'HNL',	'UGX',	'ZAR',	'STN',	'CUC',	'BSD',	'SDG',	'SDG',	'IQD',	'CUP',	'GMD',	'TWD',	'RSD',	'MYR',	'FKP',	'XOF',	'UYU',	'CVE',	'OMR',	'KES',	'SEK',	'BTN',	'GNF',	'MZN',	'MZN',	'SVC',	'ARS',	'QAR',	'IRR',	'EUR',	'XPD',	'THB',	'UZS',	'XPF',	'BDT',	'LYD',	'KWD',	'XPT',	'RUB',	'ISK',	'EUR',	'MKD',	'DZD',	'PAB',	'SGD',	'JEP',	'KGS',	'XAF',	'XAG',	'EUR',	'CHF',	'HRK',	'EUR',	'DJF',	'TZS',	'VND',	'XAU',	'AUD',	'KHR',	'IDR',	'KYD',	'BWP',	'SHP',	'EUR',	'TJS',	'RWF',	'DKK',	'BGN',	'MMK',	'NOK',	'SYP',	'XBT',	'LKR',	'CZK',	'EUR',	'EUR',	'XCD',	'HTG',	'BHD',	'EUR',	'EUR',	'KZT',	'SZL',	'YER',	'AFN',	'AWG',	'NPR',	'MNT',	'GBP',	'BYN',	'HUF',	'BYN',	'BIF',	'XDR',	'BZD',	'MOP',	'NAD',	'EUR',	'TMT',	'PEN',	'WST',	'TMT',	'EUR',	'EUR',	'GTQ',	'CLP',	'EUR',	'TND',	'SLL',	'DOP',	'KMF',	'GEL',	'MAD',	'AZN',	'TOP',	'AZN',	'PGK',	'CNH',	'UAH',	'ERN',	'MRO',	'CNY',	'MRU',	'BMD',	'PHP',	'PYG',	'JMD',	'EUR',	'COP',	'USD',	'GGP',	'ETB',	'VEF',	'SOS',	'VEF',	'VUV',	'LAK',	'BND',	'ZMW',	'LRD',	'ALL',	'GHS',	'EUR',	'ZMW',	'SPL',	'TRY',	'ILS',	'GHS',	'GYD',	'KPW',	'BOB',	'MDL',	'AMD',	'TRY',	'LBP',	'JOD',	'HKD',	'EUR',	'LSL',	'CAD',	'EUR',	'MUR',	'IMP',	'RON',	'GIP',	'RON',	'NGN',	'CRC',	'PKR',	'ANG',	'SRD',	'EUR',	'SAR',	'TTD',	'MVR',	'SRD',	'INR',	'KRW',	'JPY',	'AOA',	'PLN',	'SBD',	'EUR',	'MWK',	'MGA',	'EUR',	'EUR',	'MGA',	'BAM',	'EGP',	'NIO',	'NZD',	'BRL']

 
countries = ['Afghanistan',	'Albania',	'Algeria',	'Angola',	'Argentina',	'Australia',	'Austria',	'Azerbaijan',	'Bahamas',	'Bahrain',	'Bangladesh',	'Barbados',	'Belarus',	'Belgium',	'Bhutan',	'Bolivia',	'Bosnia and Herzegovina',	'Botswana',	'Brazil',	'Brunei Darussalam',	'Bulgaria',	'Burundi',	'Cambodia',	'Cameroon',	'Canada',	'Central African Republic',	'Chad',	'Chile',	'China',	'Colombia',	'Congo',	'Costa Rica',		'Croatia',	'Cyprus',	'Czech Republic',	'Denmark',	'Dominican Republic',	'Ecuador',	'Egypt',	'El Salvador',	'Estonia',	'Ethiopia',	'Fiji',	'Finland',	'France',	'Gabon',	'Gambia',	'Georgia',	'Germany',	'Ghana',	'Gibraltar',	'Greece',	'Grenada',	'Guatemala',	'Guinea',	'Guyana',	'Haiti',	'Honduras',	'Hong Kong',	'Hungary',	'Iceland',	'India',	'Indonesia',	'Iraq',	'Ireland',	'Israel',	'Italy',	'Jamaica',	'Japan',	'Jordan',	'Kazakhstan',	'Kenya',	'Korea, Republic of',	'Kuwait',	'Kyrgyzstan',	'Latvia',	'Lebanon',	'Lithuania',	'Madagascar',	'Malaysia',	'Maldives',	'Malta',	'Mauritius',	'Mexico',	'Moldova, Republic of',	'Monaco',	'Mongolia',	'Montenegro',	'Morocco',	'Mozambique',	'Myanmar',	'Namibia',	'Nepal',	'Netherlands',	'New Zealand',	'Nicaragua',	'Niger',	'Nigeria',	'Norway',	'Oman',	'Pakistan',	'Panama',	'Papua New Guinea',	'Paraguay',	'Peru',	'Philippines',	'Poland',	'Portugal',	'Puerto Rico',	'Qatar',	'Reunion',	'Romania',	'Russian Federation',	'Rwanda',	'Saint Vincent and the Grenadines',	'Saudi Arabia',	'Senegal',	'Serbia',	'Seychelles',	'Singapore',	'Slovakia',	'Slovenia',	'Somalia',	'South Africa',	'Spain',	'Sri Lanka',	'Suriname',	'Sweden',	'Switzerland',	'Syrian Arab Republic',	'Taiwan',	'Tajikistan',	'Tanzania, United Republic of',	'Thailand',	'Trinidad and Tobago',	'Tunisia',	'Turkey',	'Turkmenistan',	'Uganda',	'Ukraine',	'United Arab Emirates',	'United Kingdom',	'United States',	'Uruguay',	'Uzbekistan',	'Venezuela',	'Vietnam',	'Western Sahara',	'Yemen',	'Zambia',	'Zimbabwe']
                    
    
    
for j in range(0,len(countries)) :
    CCY_corrdidor = []
    fx_rate_corridor = []
    driver.switch_to.window(driver.window_handles[0])
    elem_9 = driver.find_elements_by_class_name("Heading")
    while(elem_9 == []):
        driver.back()
        driver.forward()
        j = j+1
        elem_9 = driver.find_elements_by_class_name("Heading")
    c = countries[j]
    elem_9 = driver.find_elements_by_class_name("Heading")
    for e in elem_9:
        institute = (e.text)
    elem_5 = driver.find_element_by_id("sender_country")
    elem_5.send_keys(c)
    elem_5.send_keys(Keys.ENTER)
    elem_6  = driver.find_element_by_id("amount")
    elem_6.clear()
    elem_6.send_keys('10000.00')
    time.sleep(3)
    elem_7 = driver.find_element_by_class_name("Navigation-slider")
    elem_7.click()
    time.sleep(5)
    try:
        elem_9 = driver.find_element_by_class_name("PaymentOptions-showMore")
        elem_9.click()
        time.sleep(2)
    except:
        a=5
    elem_7 = driver.find_elements_by_class_name("Offer-name")
    elem_8 = driver.find_elements_by_class_name("Offer-price")
    for e in elem_7:
        payment_method.append(e.text)
        country.append(c)  
    for e in elem_8:
        pt_amount.append(e.text) 
        institute_name.append("MIT")
    
    for a,b in zip(elem_7, elem_8):
        c1 = "NAC"
        if a.text == "":
            c1 = "DC"
        if a.text[0:8] == "Domestic" and c == "India":
            c1 = "INR"
        if c1 == "NAC" and b.text[-1:] == "€":
            c1 = "EUR"
        if c1 == "NAC" and b.text[-1:] == "£":
            c1 = "GBP"
        if c1 == "NAC" and b.text[:2] == "R$":
            c1 = "BRL"
        if c1 == "NAC" and b.text[-1:] == "l$":
            c1 = "LRD"
        if c1 == "NAC" and b.text[-1:] == "A$":
            c1 = "AUD"
        if c1 == "NAC" and b.text[:1] == "$" and ('Canadian' in a.text or c == "Canada"):
            c1 = "CAD"
        if c1 == "NAC" and b.text[:1] == "$" :
            c1 = "USD"
        if c1 == "NAC" and a.text[-1:] == ")" and a.text[-4:-1] in Currency_List:
            c1 = a.text[-4:-1]
        if c1 == "NAC" and a.text[-3:] in Currency_List: 
            c1 = a.text[-3:]
        if c1 == "NAC" and a.text[-3:] not in Currency_List: 
            c2 = a.text[-3:]
            xyz = c_ccy.loc[c_ccy['c'] == c, 'CCY'].item()
            c1 = xyz
        From_CCY = c1
        CCY_corrdidor.append(From_CCY)
        ccy_set = list(set(CCY_corrdidor))
    fx_rate_set = []
    for cs in ccy_set:
        driver.switch_to.window(driver.window_handles[1])
        if cs == 'USD':
            fx_rate_set.append(amount_int)
        if cs == 'EUR' and EUR_Count%5 == 0:
            time.sleep(3)
            xe = "https://www.xe.com/currencyconverter/convert/?Amount=" +  amount_int +"&From=" + To_CCY + "&To=" + cs
            driver.get(xe)
            time.sleep(3)
            elem_9 = driver.find_element_by_class_name("converterresult-toAmount")
            time.sleep(3)
            fx_rate_set.append(elem_9.text)
            last_EUR = elem_9.text            
            time.sleep(3)
            EUR_Count = EUR_Count + 1
        if cs == 'EUR' and EUR_Count%5 != 0:
            fx_rate_set.append(last_EUR)
        if cs != 'USD' and cs != 'EUR':
            time.sleep(3)
            xe = "https://www.xe.com/currencyconverter/convert/?Amount=" +  amount_int +"&From=" + To_CCY + "&To=" + cs
            driver.get(xe)
            time.sleep(3)
            elem_9 = driver.find_element_by_class_name("converterresult-toAmount")
            time.sleep(3)
            fx_rate_set.append(elem_9.text)
            time.sleep(3)
    for cc in CCY_corrdidor:
        ccy_index = ccy_set.index(cc)
        fx_rate_corridor.append(fx_rate_set[ccy_index])
        CCY_Full.append(cc)
        fx_rate.append(fx_rate_set[ccy_index])
    
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)
    driver.back()
    time.sleep(3)
    res__21 = vstack((payment_method,pt_amount, country, institute_name, CCY_Full, fx_rate)) 






########    

my_df__21 = pd.DataFrame(res__21)
my_df__21
my_df__21.to_csv('file_MIT 5000 full xe.csv', index=False, header=True)