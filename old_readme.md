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
1.	Implement Wifi receiver on GNU radio
2.	Implement a Wifi receiver flow graph on GNU radio that can find the phase difference between the two receiver antennas.
3.	Connect two USRP boards to create a 2 receiver antenna setup
4.	Test the flow graph you created in step 2 on the setup you created in step 3.
5.	Detect angle of elevation using your setup.
6.	Detect azimuth angle using your setup.
7.	Connect a smartphone/IMU to your setup to keep track of changes in the detected elevation and azimuth angles of the hidden device.
8.	Integrate this information with camera app to augment the location of the hidden device.


## Success metrics
* The system can detect unknown broadcasting wireless devices within 10m and the error of distance difference is less than 30cm.
* The AR visualization can correctly display the detected devices and map their locations to the environment with error of distance difference less than 10cm.
* (Stretch goal) The system can calculate and display more details of detected devices, such as device type and transmission rate.
## Experimental validation plan
The experiment that we are planning to conduct is to set up broadcasting wireless divices in a room, which constantly generates radio waves that allow our product to detect. Then we use the USRP product to detect these signals. Once we detect the signals and figure out the exact locations of these hidden devices, we are almost successful in this project. The last thing that we need to validate is that we are going to display these information we gathered on our cellphones. This experiment will be designed specifically with respect to success metrics. But before this final experiment, we will also conduct slightly smaller experiments, just to make sure we meet every major milestones.
