[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/perfectson/public-beat-the-market-) 

# public-beat-the-market-

https://gitpod.io/#prebuild/https://github.com/perfectson/beat-the-market-public

#errata and updates
https://www.followingthetrend.com/2019/08/trading-evolved-errata-and-updates/

#set quandl
export QUANDL_API_KEY="MY_API_KEY"
zipline ingest -b quandl

#install jupyter
 python -m ipykernel install --user
 jupyter notebook --generate-config
 jupyter notebook --NotebookApp.allow_origin=\'$(gp url 8888)\'

 #more knowledge
 https://programtalk.com/python-examples/zipline.utils.calendars.get_calendar/
 https://pythonprogramming.net/custom-markets-trading-calendar-bitcoin-python-programming-for-finance/?completed=/custom-data-zipline-local-python-programming-for-finance/