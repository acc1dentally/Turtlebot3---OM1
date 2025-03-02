# Turtlebot3---OM1

This small repo was my attempt to try and adapt OM1 for turtlebot3. Unfortunately, it is incomplete and does not work yet. 
Coming from primarily a mechanical and mechatronics background, I will require some time to study in more depth. 


Some additional thoughts based on the assignment: 

Overview:

The scope of this document is to look at the openmind repo from a hardware integration and productization perspective. 

https://github.com/OpenmindAGI/OM1

I primarily used ROS2 Humble and Gazebo to explore and test, with Turtlebot3 + camera. 

Deploying the repo: 

Repo was deployed without issues. No Unitree Spot hardware on hand. 

I staged a Turtlebot3 sim with mounted Intel Realsense - connected with ethernet. No additional OM1 framework developed. You can find the code for this here: 

I looked at the existing config and src for the Spot and tried to reproduce some basic framework for Turtlebot3 with no results. 
Custom config and copying base classes for input, fuser, etc. 
At this moment, I don’t know enough about the unitree sdk to try and convert its prebuilt plugins for turtlebot

Turtlebot3:




Config for a turtlebot3 agent: turtle.json, with system prompt base, system governance and agent inputs.
Custom connector with interface and ros2.py with simple move and rotate actions. 

Designing a framework for turtlebot - Vision, sound, battery/system, lidar → High priority?

Interfacing (new) sensor .xacros with openmind architecture

Turtlebot3 sim demonstration – can LLM de deployed for a simulated environment by pushing an rviz vision stream with a gazebo environment?
 Actionable Items: 

Demonstration videos/gifs inside the repo to showcase capabilities for the Spot agent. 

Implementation for ubiquitous, easily available or replicable robot hardware (eg. Turtlebot).

Documentation: Several documentations and tutorials linked in the repo are broken/do not exist. Should probably 5be fixed/added. 
Eg - /development/actions.mdx, env.mdx, etc. currently have no content. 

Questions and Observations: 



Documentation added for many sections like robotics and getting started is thorough and comprehensive and lays information out in a well written manner.

Code snippets are well described and commented. Easy to parse and understand. 

System logging is comprehensively added in action files. 

Architecture Diagram very succinctly lays out each layer and how it is connected to the LLM.

Hardware Abstraction Layer for products use proprietary sdk - how are prompts translated into motion control commands for the robot? 

How does sensor URDF structure slot into the AI and World Captioning Layer? 

Is the video stream responsive enough for LLM API calls via architecture?

External Environment error handling for prompt execution - what does that look like? 
For eg - obstacle introduced after prompt to move in a direction. Is loop.py robust enough for on-the-fly error handling?

LLM Prompt compression for more efficient user direction? Does prompt size have any reasonable effect on performance?

System Diagnostics: Is the LLM planned to be connected to robot logging message stream?

Motion control pipeline: proprietary robot motion control solutions connected through ROS/Cyclonedds to Architecture? 

Custom SLAM module essential for vision based motion systems. Are you leveraging it from the robot proprietary codebase? 

How is Vision module stream → Navigation SLAM module input handled? Are they discrete streams or SLAM built on top of the Vision module? 

Development for new products: Does robotic hardware support additional openmind OM1 computation or are extra chipsets required to be installed? 

Do custom URDFs require ground up rebuild as well as CAD implementation? 

Product scope: Plug and play modularity or bespoke rebuild for each client product?
