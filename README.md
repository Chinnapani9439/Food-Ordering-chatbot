# Food Ordering Chatbot Using Google Dialogflow
![image](https://user-images.githubusercontent.com/80595262/236020927-e695c9f6-256c-472e-a109-140103e0f33f.png)
## Process
![image](https://github.com/Chinnapani9439/Wends_chatbot/blob/main/process_dig.png)

## Steps befor running the code

Creating an Agent:
1) Start by clicking on the “Create Agent” tab
2) Give the name of the agent as Wendy’s_Chat_Bot
3) Then our agent would be ready with the name “Name of the bot”

Bot Development
1) Clicking out the preset intents i.e. default welcome intents
2) Creating a response to the welcome intent and testing it.
3) Creating new intents as per our requirements and add some queries such as:

“What are your delivery timings?”
“Is there anything new?”
“I’d like to order a burger”

Points to Remember
1) Add a variety of Expressions
2) Group Expressions correctly under well-defined Intents
3) Keep Responses precise
4) Always click ‘Save’.

Creating Entities
1) After Intents, you need to define entities. Entities are powerful tools used to extract parameter values from the user’s query. Any actionable data that you want to get from a user’s request should have a corresponding entity.
2) Well, for each user expression mapped to an intent, the agent needs to figure out the respective input that the user wants info about. This, the agent does with the help of Entities.
3) So for each intent you create, every user expression should contain a corresponding entity that your bot agent needs to figure out. Now by default, the agent can’t do that — you need to train it to do so.

Training the Agent
1) Dialog Flow provides a training tool that allows you to add annotations. It helps to improve the classification accuracy of the agent. Here you will also receive a log of all the queries sent to your agent and what the agent responded in return.
2) This is very useful if you tell your agent something and it responds with an output you don’t like. It can also be helpful if you realize later that you forgot a synonym of an entity, and users are using that a lot, then you can tell your agent what to do in that case.

Adding the Response
1) Draft a concluding response.
2) Include the ‘$value’ in the message so that it can copy useful information from the Parameters.
3) Toggle on the Intent as ‘end of conversation’.

Integration

Actual chatbot deployment on platforms, like your websites, etc. is a complicated procedure that required publishing the bot. But we can still get an idea of how the chatbot would appear when functional. Here’s how:

1) Navigate to the ‘Integration’ section in the left column
2) Toggle ‘Web Demo’  or ‘Web Demo Beta’ On, then click it to enter

![image](https://github.com/Chinnapani9439/Wends_chatbot/blob/main/feature.png)

Here is the example image of the streamlit app where the chatbot is integrated:

![image](https://github.com/Chinnapani9439/Wends_chatbot/blob/main/main.png)

Here in this image we can see the chatbot intracting with the users:

![image](https://github.com/Chinnapani9439/Wends_chatbot/blob/main/chatbot.png)


External API and Databases

The Backend Services as Webhook to Chat Bot application is served via Flask Restful API

The current explicit features provided by Backend Services are:
1) Addition of User selected choices to Cart
2) Removal of Items from Cart
3) Total Bill of Items in Cart
4) Cataloging of User provided information and ordered items to BigQuery (DataBase) 

Few Implicit Features provided by Webhook includes conditional trigger of few features (intents)
Based on user conversation flow


*********************************** THANK YOU ************************************















