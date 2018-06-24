@echo off
title tool crawl book in vinabook
start call get_proxy.bat
timeout /t 5
scrapy crawl tool