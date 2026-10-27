# static_viz
CAPP Data Visualization 

# Cherin Lee Milestone 2

Cherin Lee

## What is your current goal? Has it changed since the proposal?

Yes my current goal is now much more focused and includes geographic data. Rather 
than using the betting platform data, I decided to go with the data provided by The 
Transparency Project. Now my project is about looking at data for online gamblers
who registered for accounts in 2005 and are primarily in europe. 

## Are there data challenges you are facing? Are you currently depending on mock data?

I am not relying on mock data - my challenge was initially getting the Kashi betting
platform data but after it was emphasized that it's better to have clean data I 
pivoted. I feel like this limits my analysis, making it less timely and location 
relevant, but at the end of the day it's more about looking at a visual analysis. 

## Describe each of the provided images with 2-3 sentences to give the context and how it relates to your goal.

image1.json

For the chloropleth graphs I am trying to show a sense of concentration of where people are placing online bets. I think the final draft will be focused on Europe (most of the sample) and have have another measure of intensity for amount of debt so that you can compare who is gambling a lot and who is losing a lot. I'm not sure if the map is as helpful because the data is so concentrated in Europe.

image2.json

With the bar charts I hope to show the distribution of number of users in a way that is easier to read than a heat map. By isolating the "top betting" countries it is easier to compare country by name and by number of better. My final draft will have a better looking version of the simplified barchart with less jarring colors and maybe some subtitles detailing the mean number of gamblers, something to give more context. I want to think of the data visualizations as giving an overview by country and then zooming into outliers (Germany) and seeing the performance of heavily betting countries.


image3.json

This stacked bar chart contains betting performance data so that I can describe 
how this betting is actually affecting the people included in the dataset. 

I think it would be cool to use the granular individual level data to compare what types of people are betting across the countries, if younger people have worse outcomes or bet more frequently which I would show with a line graph or series of stacked barcharts.

## What form do you envision your final narrative taking? (e.g. An article incorporating the images? A poster? An infographic?)

I imagine a static poster or infographic to display my charts, I think I will have 
visualizations that go in order by subject size: first worldwide betting, then Europe,
then Germany. 

## Questions

1. I originally wanted to show gambling patterns domestically but then came across this already cleaned global dataset -
   however there are a lot of countries that are missing / not included. I'm worried that if there is no context for the
   data it will look like Germany has a super super big gambling problem (most entries), would it be better to constantly
   emphasize the proportions (gamblers out of total gamblers in the country, gamblers out of total gamblers in the sample)
   or is a long-ish disclaimer at the beginning of my final infographic preferred? 




______________________________________________________________________________________________





# Milestone 1

## Description

I want to understand the current state of gambling / sports betting and create a visualization that presents timely data in an accessible way - assuming that most people also are new to this concept.

## Data Sources

{include 2-4 data sources with the following:}

### Data Source 1: {Kalshi API Dataset}

URL: {[URL](https://docs.kalshi.com/getting_started/historical_data)}

Size: {50000} rows, {50} columns

{Historical Kalshi trade data: volume of settled markets, completed trades, and fulfilled orders. Live endpoints return current and recent data: open and recently closed markets, active orders, and recent fills. I am hoping to pull the data and get recent consumer trends from the past 10 years with location, size of bets, and consumer demographics. I am interested in seeing if there are trends / events that can connect to the patterns like a big advertisement or launch of deal (first $200 bet is covered), something like that.}


### Data Source 2: {Population Trends in Internet Sports Gambling}

URL: {http://www.thetransparencyproject.org/Availabledataset}

Size: {46,339} rows, {22} columns

{This is longitudinal analysis of online gambling participation and activity ending in 2006, 18 months of data. Data from the Division on Addictions (DOA) and bwin Interactive Entertainment.}

## Questions


