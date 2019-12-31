# Overwatch Perfect Flex
The following is a demo for my most recent personal project that I have hosted on Heroku, Overwatch Perfect Flex. This project came to be from an innate curiosity of statistically analyze which champion you should play in order to maximize win-rates given the current state of the enemy and your concurrent teams composition. Given a valid screenshot( as indicated in the demo), my algorithm is able to identify 31! team compositions. This was achieved by becoming proficient in a widely support computer vision open source library called OpenCV-Python. Once champions have been identified for their corresponding teams, a custom weighted tree traversal algorithm was used to determine the global optimal champion(s) selections.

This was my first attempt implementing theoretical algorithms I have studied throughout my undergraduate career and applying those concepts on problems I sympathize with. Completing this rigorous project independently was incredibly satisfying and I plan on iterating through many versions of the match-making algorithm , for as long as I have support :)
## Demo URL
https://overwatchperfectflex.herokuapp.com/
## Demo Instructions
https://i.imgur.com/YNuQTUq.jpg
Save the following screenshot and upload the image where prompted on the homepage 
![demo screenshot](https://i.imgur.com/YNuQTUq.jpg)

## License
[MIT](https://choosealicense.com/licenses/mit/)
