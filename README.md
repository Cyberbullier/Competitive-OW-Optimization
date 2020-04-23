# Overwatch Perfect Flex
The following is a demo for Overwatch Perfect Flex, my most recent personal project that I have hosted on Heroku. This project originated from an innate curiosity about how to statistically analyze which champion you should play in order to maximize win-rates  given the current ally and enemy team composition. Given a valid screenshot (as illustrated in the demo), my algorithm is able to identify 31! different team compositions. This was achieved by becoming proficient in a widely support computer vision open source library called OpenCV-Python. Once champions composition of the teams have been established, a custom weighted tree traversal algorithm determines the global optimal champion selection(s). 

This was my first attempt at implementing theoretical algorithms that I have studied throughout my undergraduate career, and applying those concepts to problems that I have encountered. Completing this rigorous project independently was incredibly satisfying, and I plan on iterating through and refining the match-making algorithm I have created for as long as I have support 🙂

## Demo URL
https://overwatchperfectflex.herokuapp.com/
## Demo Instructions
https://i.imgur.com/YNuQTUq.jpg
Save the following screenshot and upload the image where prompted on the homepage 
![demo screenshot](https://i.imgur.com/YNuQTUq.jpg)


## Future Plans?
 Markup : * Add support for newer champions (eg. Ashe, Doomfist, Echo, etc...)
             
          * I plan on introducing heuristics of different states of the game ie, different maps. A bit ambitious, but I eventually want to get to a point where I'm able to interact with Blizzard's API to scrape concurrent win rates for each ELO, processing both unstructured and structured data.
 
## License
[MIT](https://choosealicense.com/licenses/mit/)
