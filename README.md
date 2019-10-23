# Localizing-and-visualizing-wireless-sensors.

Objective Description

Nowadays Iot is developing in an incredibly fast pace, and tons of sensors are involved into this process, which provides us better experiences with Iot concepts. In order to allow users to access the sensors' measurements faster and easier, we are trying to generate a method that not only localizes the surrounding unknown sensors accurately, but also displays those sensors on a smartphone's screen everytime they are captured by the camera of that smart phone.

Envisioned Approach

To start with our project, we have to first think about how to localize the unknown sensors within a moderate range. There are two approaches that we are potentially using. One method is using radio signal to localize the sensors. We are planning to use USRP to realize this approach, which has two antennas that can be used to localized the sensors in spherical coordiante. Another approach is to use visual learning to capture the small signal sent by the sensors via LED blinking or so. Both methods will give us an accurate detection of the location of each sensor. Then we will have an app developed on ios or android platform. The app basically activates the camera, filters the surrounding sensors' signal and displays all the correspoding measurements on screen.

Planned Deliverables


