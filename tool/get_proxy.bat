@echo off
title tool get proxy list after 1800s
:while
scrapy crawl get_proxy
timeout /t 1800
goto while