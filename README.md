![Water Channel Blog](images/jartest.jpg)

# Water Channel Blog 
Welcome! [IHE Delft](http://un-ihe.org)
## Introduction
The global water crisis is a major concern today and will become more severe in the coming years. The availability of 
freshwater becomes more challenging in the semi-arid regions. However, in other areas where freshwater is available(surface and groundwater),contamiantion and degradation of the water quality is a major issue risking the health of millions of people. As per the SDG 6, availability of fresh and safe water for all is a basic necessity for overall human development. Therefore, there is need of ideas and solutions that can help to provide the clean freeshwater to the entire population. 

The overall aim of this project is to develop open access water channel blog with an objective to share the ideas and solutions to address global water issues. All the water practictioner from all over the world (including professional, students) can be a member of the community in the blog. 

A live water channel blog can be found [here](https://waterchanel.herokuapp.com/).

![blog preview](media/image/blogpreview.jpg)

# Table of Contents
 [1. About the Water Channel Blog](#water-blog)

 [2. User Expereince (UX) design](#ux)
  - [User Goals:](#user-goals)
  - [Blog Design thinking:](#user-stories)

  [3. Features](#features)
 - [Existing features](#exist-feature)
 - [future features](#future-feature)

 [4.Technologies used](#technologies-used)

 [5.Testing](#testing)

 [6.Bugs](#bugs)

 [7. Deployment](#deployment)

 [8. How does the blog works?](#blog-work)

 [9. Acknowledgement](#acknowledgement)

  <a name="water-blog"></a>

# 1. About the Water Channel Blog
  [Go to the top](#table-of-contents)

This water channel blog is desinged as a a platform where water professional and students can share the expereince and ideas to solve the water related issues in the world. It can also be used as a knowledge sharing platform.  
   <a name="ux"></a>
# 2. User Expereince (UX) design
  [Go to the top](#table-of-contents)

  Dosing of coagulant (chemical) i.e. FeCl3 is needed to remove the fine particles from drinking water treatment. Moreover, overdosing of the chemicals will support for the resuspension of partcles and is also an environmental issues. Therefore, optimization of the coagulant dose based on the water qaulity is rather important which save cost and environment. This project is aimed to design the app which allows to calcualte the optimum coagulant dose based on the experimental data provided in google sheet and ultimately calcualte the total dose required depending upon the type of coagulant used. 

The following users types can be benifitted from the app:

- Drinking water treatment plant operators
- Professionals dealing with water treatment designs.
- Post graduate students in the field of water supply and environmental engineering.

   <a name="user-goals"></a>
## 2.1 User Goals
  [Go to the top](#table-of-contents)

The main goal of this project is to develop a coagulant dose calcualtor app that allows to calcualte the optimum coagulant dose for diffent water types. This is of great useful for me to apply in my teaching for a demonstration in the laboratory session to my students.

  <a name="user-stories"></a>
## 2.1 Blog Design thinking
  [Go to the top](#table-of-contents)

The user requires certain functionality to enable the app to work as needed.

- Article Detailed View
- Create Posts
- Login and Logout
- Register
- Comments
- Like Posts
- Edit and Delete Posts

Three step processes were followed as below:
- Set the user requirement and added to the user stories within the github project
- After the gradual fullfilment of the requirement, the stories were moved to in progress colum.
- And finallym when requiment was fully meet, it was moved to the complete column.

![User Stories](media/image/userstories.jpg)

 <a name="flow-chart"></a>

# 3. Flow Chart
  [Go to the top](#table-of-contents)

Flow chart was used to conceptualise the optimum coagulant dose calcualtor idea. It was drawn using Lucid Chart. The flow diagram is as shown below.
![flowchart](images/flowchart.jpg)

<a name="features"></a>

# 4. Features
  [Go to the top](#table-of-contents)

<a name="exist-feature"></a>

## 4.1 Existing Feature
### 4.1.1 APP link to google sheet data
- App calcualtion is linked to the google sheet data. The google sheet access is given using google API.
- Google sheet has four worksheet named phRAW, pHRAW2, pHRAW3, pHRAW4 where mainly the experimental data at differnt conditions are stored.The sheet also has worksheet name "dose" where mainly the data calcualted by app based on user input data will be stored (see in Figure below).
- App has a fature to validate the data provided in the google sheet.

![googlesheet](images/google-sheet.jpg)

### 4.1.2 Start of APP 
- Has a short introduction about the app to the user 
- App ask user to provide the input data mainly flow rate in m3/s and storage time in months. 
![introduction](images/feature-a.jpg)

### 4.1.3 User data input validation and error checking
  - Users has to enter data input either in float or integer 
  - User cannot provide input zero or negative
  - User should provide a data input i.e. a number

![user_validation](images/user-validation.jpg)

### 4.1.4 App calcualtion
  - App calcualte the optimum coagulant dose for all experimental conditions based on data input in google sheet
  - Based on the optimum dose calculated and user's input data, app calcualte the coagulant dose needed for differnt types of coagulants used
![dose_calcualtion](images/app-calculation.jpg)

### 4.1.5 Google data sheet update
  - user's input data and app calcualted data is updated in the new row in the google sheet

![update_google_data_sheet](images/dose-calulation-.jpg)

<a name="future-feature"></a>

## 4.2 Future Feature
In future i plan to update the app including more features such as;
 - Allow users to select option for choosing differnt types of coagulants like FeCl3, NaOCl, Al2SO4 etc
 - Provide users the basic dimension of the coagulation unit required for the given type of the water

<a name="technologies-used"></a>

# 5. Technologies-used
  [Go to the top](#table-of-contents)

* [Python3](https://en.wikipedia.org/wiki/Python_(programming_language)) was used as a scripting language for the app development in this project.

* [Lucid Chart](https://www.lucidchart.com/) was used to flow diagram for the app.

* [Github](https://github.com/) was used to create the repository and to store the cproject's code after pushed from Git.
* [Gitpod](https://www.gitpod.io/) was used as the Code Editor for the site
* [PEP8 online](http://pep8online.com/) tool was used for manual testing procedures for code validation.

* [Ami](http://ami.responsivedesign.is/) was used to develop a Mockup screenshot generator
* [Heroku](heroku.com) was used to deploy a final version of the Python Essentials application code.

<a name="testing"></a>

# 6. Testing
  [Go to the top](#table-of-contents)

## 6.1 PEP8 online validation
  I have tested this project manually by passing the code through PEP8 online validation tool and confirmed there are no errors. The screenshot is as shown below:
  ![PEP8_online_validation](images/pep8_online.jpg)
## 6.2 Mannual testing 
### 6.2.1 Google sheet
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Google sheet | checked if the data provided in the google sheet is either float number or integer only except table heading. If that is not true then a message pop up "google sheet data is not valid ! Please check the data entry".| PASS

## 6.2.2 User input 
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
User input | checked if the data provided by user is either integer or float or positive. In case not true then it gives an error message "Please enter numeric value greater than 0" and "Enter value can't be zero or negative, try again". This message po up until the correct input value is provided by user.| PASS
Optimum coagulant dose calculation | checked if the app calcualte the correct optimum coagulant dose or not for all four given conditions based on the google sheet data and criteria used. | PASS
Total coagulant dose calculation based on user input| checked if all the total coagulant dose calulated by the app based on the users input data and app calcualted optimum coagulant dose is correct or not. | PASS
Update google sheet | checked if the data calculated by the app and users input data is updated or not in the googlesheet. | PASS
Update google sheet data in new row | Checked if the data updated in the google sheet is not overwrtten the previously recorded data but instead it is recorded in the new row| PASS

<a name="bugs"></a>

# 7. Bugs
  [Go to the top](#table-of-contents)

## 7.1 Solved bugs
- When i wrote the project, i had most frequently indentation error as i forget to provide a tab
- The data input by users and app calcualted results were overwritten in the google sheet with the previously recorded data. this was solved by writing a code to save the evry new data entry and app calcualtion in a new row.
- When i wrote if statement, i forget to add colon at the end of if statement, which gave me unexpected indentation error. 
- I want to display the calcualted data in bullet points in the app but it took all the data from google sheet (including headings and data). This was solved by using pretty_array package.

## 7.2 Unsolved bugs
No bugs remaining 

 <a name="deployment"></a>

# 8. Deployment
  [Go to the top](#table-of-contents)

  The proejct was deployed to Heroku using the following steps:
- Sign up to Heroku and give a unique name to the app
- Inside the Heroku app page, go to the setting first and in the section config vars, add CREDS and paste entire creds.json file
- Add buildpack python and node.js (python on top and node.js on bottom)
- Go to the diploy section and select github and click connect to github
- Search git hub repository name related to the project to be depoloyed and click connect 
- Deploy to the branch (either mannual or automatic)

 <a name="play-app"></a>

# 9. How does the app works?
  [Go to the top](#table-of-contents)

## 9.1 Google data access and validation
The app has a credential to access google data sheet . The app validates the data input in the google sheet. If the data entry in google sheet is not correct the app gives a message"Google sheet data is not valid. Please check the data entry" (see figure below where data input is not valid in google sheet (highlighted)). Moreover the app users do not have to do anything to the google sheet.

![google-sheet-validation](images/google-sheet-validation.jpg)

## 9.2 Start of the APP
When the users run the coagulant dose calcualtor Heroku  app,
- It first display the what the app is about.
-  Ask user to enter flow rate in m3/s and do the validation of the data. 
- After validation of first input data, the user is asked to provide second input data i.e., storage time. The app does the validation of this second input as well.

![user-input](images/user-input.jpg)

## 9.3 Validation of user input
App validate the user's input data both flow rate and storage time (is data integer, float, and greater than 0). If data is not correct it ask users multiple time to provide correct input.

![user_validation](images/user-validation.jpg)

## 9.4 App calcualtion

If user's input data is validate, the program runs and calcualte the following:
- Optimum coagulant dose for all conditions.
- Total coagulant dose (for differnt type of coagulant used i.e. FeCl3) is calcualted based on the optimum coagulant dose and users input data of flow rate and storage time. This is calculated for all four types of conditions like pHRAW, pHRAW2, pHRAW3 and pHRAW4.

![app_calculation](images/calculation.jpg)

## 9.5 Google data sheet update 
All the new calcualtion and user's input data are updated in the google sheet 
- no overwritten with previous data entry is allowed, 
- data should be entered in new row
- in each simualtion four rows will be added for four differnt types of experimental conditions (pHRAW, pHRAW2, pHRAW3 and pHRAW4)
- Experimental condition is also recored in the last column to understand which data belong to what experiemntal condtions

![google-update](images/google-update.jpg)

## 9.6 Re-start the program 
To run the programm again, user has to click again run the programme.


<a name="acknowledgement"></a>

# 10. Acknowledgement
  [Go to the top](#table-of-contents)


* Inspired from love sandwitch project from the code institute course
* Thanks to my mentor Marcel Mulders for his constructive feedback