# AWISSA Experiments

Goal: To find a two variables that exhibit clustering and use those clusters (by means of cluster analysis) to differentiate vegitation fires from wildfires.

Note: All data will filter out points marked by VIRRS data as low confidence under the "confidence" attribute.

[VIRRS data attributes](https://www.earthdata.nasa.gov/learn/find-data/near-real-time/firms/vnp14imgtdlnrt#ed-viirs-375m-attributes)

1. The K-means algorithim is an unsupervised learning method used to identify clusters of data points. K-means clustering into two clusters on a graph of frp and bright_ti5 is shown below:

![K-means clustering of frp against bright_ti5](frp_bright_ti5_kmeans.png)

Doesn't seem to be a clear clustering comparing the variables frp (Fire Radiative Power) and bright_ti5.

Main problem with detecting slash-and-burn method is that it's not only used to clear farmed areas, but also to clear new plots of forest land to be used as farm land. Herein lies the main limitation of methods such as spectroscopy or frp. The fires labeled as slash-and-burn will only be of farmed land while lots of the slash-and-burn takes place in virgin forest.

Another potential is using live satalite imagery to track the clearing of forest land into farmed land, using AI to label what is farm land and what is forest. That way, if there is a fire deep into forest land where no farms are nearby, the fire is surely wild.

Looking on NASA WorldView, some map layers that can be analysed by a convolutional neural network include "Human Built-Up and Settlement Extent" and "Settlements".


Pilot-GPT Test:

Name: AWISSA

Prompt: I want you to program AWISSA: Addressing Wildfire Issues in Sub-Saharan Africa. The project is meant to address the problems NASA has with detecting wildfires in Africa. Most agricultural African nations use slash-and-burn agriculture to farm their lands. However, satalites are unable to differentiate between a harmless slash-and-burn fire and a dangerous wildfire. I want you to programmatically figure out how, using NASA APIs and satalite data, these fires can be differentiated using statistical analysis. Then, once you find a viable method, I want you to use machine learning to train a model that is able to take in those variables you found out can be used (from NASA satalites) and returns the likelihood that the fire is a wildfire. This model can then be factored into NASA's detection algorithims, potentially saving millions of lives. I want you to create the the project preferably using Python, NodeJS, or both. If you believe you can make any code you wrote in Python faster by rewriting in C++ as well, that would be a nice bonus!

Conclusion: I need money to run this ish.