# EcoEats 
## Inspiration
When you think about sustainability, you often view it at a larger level. This creates a lot of stress on individuals, especially in our experience, to always be doing more in order to reduce their impacts on the planet. However, things like reducing fossil fuel dependence is something only large companies have the ability to change directly, so we wanted to create a project that allows for every day individuals to do their part in reducing the amount of plastic waste that we produce on a smaller level. We can't do this alone, so this map hopes to illustrate to users and restaurants that there is merit in providing alternatives to plastic made items on a larger scale and connecting with your community this way. We display places on the map that push for less plastic waste, so the more green restaurants that are displayed, the more that people will be able to use our web application and the more that restaurants will be held accountable for the type of waste that they produce.

## What it does
Our web application combines flask, python, javascript, and Google Maps/Google Places API in order to create the EcoEater, an interactive map showing restaurants in the user's immediate area providing alternatives to things like plastic cutlery, straws, and to-go boxes. Also built within the website is a chatbot, named EcoBuddy, that we have created using OpenAI to provide users with ways to repurpose plastic waste, rather than throw it away. 

## How we built it
For frontend, we built the web-app with HTML and decorated it with CSS. Google Maps Javascript API and Google Places API were used to generate the Google map in the EcoEater tab via JavaScript and Flask. Python backend was used to store eco-packaging restaurant names and injected into the HTML via Flask to generate pins on the Google Map. OpenAI Assistant API and Javascript were used to create the generative AI chatbot in the EcoBuddy tab. 

## Challenges we ran into
We could not figure out how to configure the OpenAI Assistant API, as the version we are using is the new version and the resources we found were all outdated. The documentation was useful, but we could not figure out how to connect it to Flask, which is what we are using to run our server.

## Accomplishments that we're proud of
We are proud that we attempted to use AI when it is something we have never used before. We also used a new API that we were unfamiliar with, Google Places API, and got it up and running. Configuring the location access for Google Maps Javascript API to generate a map based on the user's location was something new that we attempted.

## What we learned
As a group we learned more generally about options that restaurants offer to their customers that are more eco friendly. This included what restaurants generally do so, and which do not. This can be an important tool to use in order to promote restaurants that are doing their part in reducing plastic waste, in a country hugely connected to the issue of plastics being disposed of in the environment. On a technical level, we learned how to integrate openAI into a web application using flask and python. We also learned more about the design process, in the Google Maps Javascript API and in general.

## What's next for EcoEats
Having more customization in the EcoEats page, in Google Maps Javascript API, to better visualize what restaurants have available. We would love to go further and eventually include restaurants who are certified Green Restaurants as well, showing that they take sustainability to the next level, in both waste and farming practices to diminish things like biowaste and plastics containing PFAS. We would also like to correctly configure the API in order to get an AI generated response and eventually train our AI.