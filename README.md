# OpenMind OM1 Hardware Integration Analysis

[![ROS2](https://img.shields.io/badge/ROS2-Humble-blue)](https://docs.ros.org/en/humble/index.html)
[![Gazebo](https://img.shields.io/badge/Gazebo-Simulation-orange)](https://gazebosim.org/)
[![Turtlebot3](https://img.shields.io/badge/Turtlebot3-Robot-green)](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/)


# Overview

The scope of this document is to look at the openmind OM1 repo  ([Openmind OM1](https://github.com/OpenmindAGI/OM1)) from a hardware integration and productization perspective. 
I have also attempted to implement the OM1 framework onto a simulated turtlebot3.

Please refer to this GitHub repo for all the code related to this:   
[My Turtlebot3 OM1 Repo](https://github.com/acc1dentally/Turtlebot3---OM1.git)

---

## Turtlebot3

### 1) Simulate Turtlebot3 with Navigation in ROS2

![preview](https://github.com/user-attachments/assets/5e76b2ee-bb8d-4fff-9374-8e2a54b96083)


#### Simulating Turtlebot3 in ROS2
I started by setting up a basic TurtleBot3 simulation, using the guide from [Turtlebot3 Simulation](https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/).
I am using **ROS2 Humble** and **Gazebo Harmonic** on an **Ubuntu 22.04** installation.

#### Create custom urdf for turtlebot3 and mounted camera
I decided to add in a camera joint to add in vision capability to match functions provided by OM1. I did this by creating a custom urdf to add in an Intel Realsense camera to be attached to the turtlebot3 joint system.

![Screenshot 2025-03-06 112451](https://github.com/user-attachments/assets/e9be2c01-a111-4d39-abb5-7e64cce28b2d)



#### Creating a Custom Ethernet Port for Connection to OM1
To connect the TurtleBot simulation (and by extension, a physical TurtleBot3), I created an **Ethernet connection** allowing users to subscribe and control TurtleBot3 simulations.

---

### 2) Create a Framework of Implementation Similar to Spot in OM1


![turtlebot3](https://github.com/user-attachments/assets/6f49f6cc-8cc2-48e9-af41-fb0c66799bc4)

#### Understanding the Project Implementation for Spot
To correctly implement the OM1 structure for TurtleBot, I examined various folders in the OM1 repo, including:
- `actions`
- `fuser`
- `inputs`
- `plugins`
- `_init.py` files

Additionally, I reviewed Unitree’s documentation:
- [Unitree SDK2 Python](https://github.com/unitreerobotics/unitree_sdk2_python)
- [Unitree Legged SDK](https://github.com/unitreerobotics/unitree_legged_sdk)
- [Cyclone DDS](https://github.com/eclipse-cyclonedds/cyclonedds)

I also examined examples like `conversation`, `cubly`, and `iris` in the OM1 repo.

#### Creating a `config.json`
I developed a simple `config.json` file for the TurtleBot to define:
- Base prompts
- Governance laws
- Simple actions for TurtleBot

#### Creating Custom Actions for TurtleBot3
Implemented basic move and rotate actions:
- **Move forward** based on input
- **Rotate on its axis**

#### Modulating `fuser`, `input`, and `plugins` for TurtleBot3 Implementation
Updated the `fuser`, `input`, and `plugins` code in OM1 to align with the custom `config.json` for TurtleBot3.

---

### 3) Connect TurtleBot3 to OM1 Layer

#### Challenges
**Deploying Spot HelloWorld**

![Screenshot 2025-03-06 070355](https://github.com/user-attachments/assets/7a3da762-98d6-4ef5-93ca-03f884667b22)

- **Troubleshooting:**
![VirtualBox_ameya-ros-ubuntu_06_03_2025_07_11_38](https://github.com/user-attachments/assets/46fd02c8-8829-44d6-9b2c-27a03a6526e7)

  - Set environment variable `ENV` to `SIM`
  - Verified correct installation of Unitree SDK and CycloneDDS with updated paths

#### Action Plan
- Test on **dual boot** to verify hardware connections
- Verify connection through ethernet to openmind layer.
- Revert custom urdfs to proprietary turtlebot urdf descriptions for easier testing of OM1 framework. 	

## Key Takeaways
- Attempting to emulate Gazebo and rviz simulations, especially urdf joint troubleshooting and experimenting, is quite painful on a virtual machine. 


---

## OM1 Notes

![Screenshot 2025-02-28 155551](https://github.com/user-attachments/assets/b3c1d26e-ea71-4bc5-8145-15ea9cf71107)

- **Demonstration videos/gifs** included in the repo showcasing Spot agent capabilities.
- **Implementation for common robot hardware** (e.g., TurtleBot) to increase accessibility.
- **Documentation issues:** Several linked tutorials in the repo are missing or broken.
  - Example: `/development/actions.mdx`, `env.mdx` lack content.

---

## Questions and Observations

| Area | Questions and Observations |
|------|----------------------------|
| **Hardware Abstraction Layer** | How are prompts translated into motion control commands for robots using proprietary SDKs? |
| **Sensor URDF Structure** | How does the sensor URDF structure integrate with the AI and World Captioning Layer? |
| **Video Stream & LLM API Calls** | Is the video stream responsive enough for LLM API calls? |
| **External Environment Error Handling** | What happens if an obstacle appears after a movement prompt? Is `loop.py` robust enough for dynamic error handling? |
| **LLM Prompt Size & Performance** | Does prompt size affect performance? Can prompts be compressed for efficiency? |
| **LLM & Robot Logging** | Will the LLM connect to the robot logging stream for diagnostics? |
| **Motion Control Pipeline & ROS/Cyclonedds** | Does the motion control pipeline rely on proprietary SDKs, or does it integrate with ROS/CycloneDDS? |
| **Custom SLAM Module** | Is the custom SLAM module from proprietary robot code being utilized? |
| **Vision Module Stream & Navigation SLAM Input** | Are the Vision module stream and SLAM inputs discrete, or does SLAM build on the Vision module? |
| **OM1 Computation & New Product Development** | Does robotic hardware support additional OM1 computations for new products, or are extra chipsets required? |
| **Custom URDFs** | Do custom URDFs require ground-up rebuilding, including CAD implementation? |
| **Product Scope & Modularity** | Is the product designed for plug-and-play modularity, or does each client require a bespoke rebuild? |

---

