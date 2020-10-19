# ZALotteryPythonProject
  - South African Lottery API: 
    - This API was Developed using these software stack:
       
       - Selenium Webdriver (Webpage Content Scrapper),
            - Which scraps; the South African National lottery site https://www.nationallottery.co.za
                - for info on; How to play the games.
                - for info about; latest Draw results, for each game.
                - for info about; past Draw results History, for each game.
      
       - MongoDB Cluster (for Remote Data Storage),
            - An ability to query and update a remote MongoDB Cluster;
             for the usage of Data Analysis **[work in-progress]**.
      
       - Python Default Packages (which offer the following),
            - A primitive ability to randomly pick numbers for each Game;
             through the 'quick_pick' functionality.
       
       - MatLibPlot (for Data analysis), **[work in-progress]**
       
       - Flask (for hosting, a Web Server Gateway Interface),
            - Game Resource Info; offered by this API include but not limited to these Games:
                - Lotto
                    - API url reference '/lotto'
                - Lotto Plus 1
                    - API url reference '/lotto_plus_1'
                - Lotto Plus 2
                    - API url reference '/lotto_plus_2'
                - Daily Lotto
                    - API url reference '/daily_lotto'
                - Powerball
                    - API url reference '/powerball'
                - Powerball Plus
                    - API url reference '/powerball_plus'
            
            - API Provides the following; and referenced using the API url as seen from the last description:
                - How to play the games.
                    - API url reference suffix '/info'
                - Latest draw results.
                    - API url reference suffix '/draw'
                - Previous draw results.  
                    - API url reference suffix '/history'
                - Update a game; Draw results Cluster
                    - API url reference suffix '/draw_update'
                - Update all games; Draw results Cluster
                    - API url reference 'all/draw_update'
   
       - Docker (for Server Integration Implementation), **[work in-progress]**
       
       - Git, and Github (for code Version Control System).  

  - More functionality, is to be added:
    - Such as a collaborative Cloud Cluster, 
       - Where recently played; Game Draw numbers, by our users; can be analysed,
        and cross referenced with the MongoDB Cluster Data to make a Robust QuickPicker;
        through usage of Artificial Intelligence such as Machine Learning. [**work in-progress]**
       
 ## Disclaimer
 
 I created this repository; just for fun, and to showcase Python usage.
 "I'd like you to contribute to this repo". 
 _Lets add more useful functionality to this repo..._
