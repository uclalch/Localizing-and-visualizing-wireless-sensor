# Localizing and Visualizing Wireless Sensors.

## Objective
Nowadays Iot is developing in an incredibly fast pace, and tons of sensors are involved into this process, which provides us better experiences with Iot concepts. In order to allow users to access the sensors' measurements faster and easier, we are trying to generate a method that not only localizes the surrounding unknown sensors accurately, but also displays those sensors on a smartphone's screen everytime they are captured by the camera of that smart phone.

## Envisioned Approach

To start with our project, we have to first think about how to localize the unknown sensors within a moderate range. There are two approaches that we are potentially using. One method is using radio signal to localize the sensors. We are planning to use USRP to realize this approach, which has two antennas that can be used to localized the sensors in spherical coordinates. In addition, some kinds of information of detected sensor can be decuded from the collected RF data and properties. Another approach is to use visual learning to capture the small signal sent by the sensors via LED blinking or so. Both methods will give us an accurate detection of the location of each sensor. Then we will have an app developed on iOS or Android platform. The app basically activates the camera, filters the surrounding sensors' signal and displays all the correspoding measurements on screen.

## Planned Deliverables
1. USRP localization logic
2. AR application to visualize located sensors

## Timeline
* **Week 4:** Read papers about USRP locatization.
* **Weeks 5-6:** Implement localization logic.
* **Weeks 7-8:** Develop AR application to display localization data.
* **Weeks 9-10:** Testing

## Division of Work
* Jinchi and Arther will concentrate on implementing the USRP localization logic.
* Gabriel will focus on developing the AR application.
* All team members will have some role in all parts of the project.

## Current Focus of Work (Week 5)
* Jinchi and Arther learn about GnuRadio for programing the USRP device.
* Gabriel test the AR framework.

## Literature Reviewed
* When IoT met Augmented Reality: Visualizing the Source of the Wireless Signal in AR View (AR framework)
* Accurate Indoor Localization With Zero Start-up Cost (USRP localization)
* GnuRadio Tutorials and various Github Repositories.

## Major milestones
Waiting
## Success metrics
Waiting
## Experimental validation plan
Waiting
