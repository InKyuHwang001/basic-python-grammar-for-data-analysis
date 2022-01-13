# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 13:16:02 2021

@author: nadai
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import csv
import matplotlib.pyplot as plt
from datetime import datetime
#-------------------------------------------------------------
#크롤링
#! pip install selenium
#X아래 점3개 도움말 크롬정보 크롬버전 확인
#https://chromedriver.chromium.org/downloads
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#! pip install bs4
from bs4 import BeautifulSoup
#원하는 정보만 한정하여 가져오기
#F12누르기 | 도구더보기-개발자도구
#마우스 우클릭 inspect
import time#시간변동으로 인해서
#------------------------------------------------------------

