#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import GlassdoorScraper as gs

jobsDF = gs.scrapeJobs('Data Science', 'India', 4)

print('data received')
print(jobsDF)

jobsDF.to_csv('test.csv', index=False)