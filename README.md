# glaseye 

glaseye is a project of glasford.io with the eventual goal of reducing crime through means of pacism. glaseye can also be seen as a surveilence tool. The main use of glaseye is to use AI and computer vision to "incidents". But it also contains many other useful items.

## Part 1
Part 1 of glaseye is facial detection of unique visitors. This part is actually sort of funny as it was basically 100% created by an AI, and it seems to work. Which I found to actually be very interesting. 
I debated whether I should post this as it seems like cheating, but I think the world should actually be able to use this. 

Background: I have a building that I need to generate a list of unique visitors and save a picture of the unique visitor's face along with a timestamp in UTC time with the person's first face. 

This works with my current video camera streams. I am revealing my brand of video camera, but if the camera is an IP camera it can probably be used with this.
Furthermore, this is an opensource thing so feel free to do what ever you want, since you don't need any additional equipment to run this you can use security cameras for longer period of time, thereby reducing cost.

To run this use `python glaseye.py urls.txt` where `urls.txt` is your list of camera streams.