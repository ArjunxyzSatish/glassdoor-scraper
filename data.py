#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import GlassdoorScraper as gs
import pandas as pd

jobsDF = gs.scrapeJobs('Data Science', 'India', 333333)

jobsDF.to_csv('test.csv', index=False)