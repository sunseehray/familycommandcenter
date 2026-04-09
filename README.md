# Overview

This is my take on a family command center network server using python. I want to learn more about networking through this project.

The Family Command Center network server aims to be a local server where family members can access a family calendar, a shopping list, a messaging service, and so on. 

Currently, I am building a simple messaging feature guided by ChatGPT to test my setup.

<!-- {Important!  Do not say in this section that this is college assignment.  Talk about what you are trying to accomplish as a software engineer to further your learning.}

{Provide a description the networking program that you wrote. Describe how to use your software.  If you did Client/Server, then you will need to describe how to start both.}

{Describe your purpose for writing this software.}

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.} -->

[Software Demo Video](https://youtu.be/xFMinrLgmD8)

# Network Communication

This project uses a client–server architecture. The server is hosted on a Linux virtual machine (Ubuntu) running in VirtualBox, while the client runs on a Windows 11 host machine.

Communication between the client and server is implemented using TCP (Transmission Control Protocol) over port 5000. TCP was chosen to ensure reliable, ordered delivery of messages.

Messages are exchanged between the client and server in a structured format (e.g., text-based payloads), allowing both sides to interpret and process requests and responses consistently.
<!--
{Describe the architecture that you used (client/server or peer-to-peer)}

{Identify if you are using TCP or UDP and what port numbers are used.}

{Identify the format of messages being sent between the client and server or the messages sent between two peers.}
-->

# Development Environment

The application was developed using Python as the primary programming language. Development and testing were carried out on a Windows 11 host machine, with a Linux (Ubuntu) virtual machine running in VirtualBox used to simulate the server environment.

The following tools and libraries were used:

- Python 3.14.3
- VirtualBox for virtualization
- Ubuntu Linux as the server operating system
- Standard Python networking libraries (e.g., socket) for implementing TCP communication
- dotenv (python-dotenv) for managing environment variables

Development was performed using a code editor (e.g., VS Code), and version control was managed using Git.
<!--
{Describe the tools that you used to develop the software}

{Describe the programming language that you used and any libraries.}
-->
# Useful Websites
<!--
{Make a list of websites that you found helpful in this project}
-->
* [Python Server Libraries](https://docs.python.org/3/library/socketserver.html)
* [Python Socket Libraries](https://docs.python.org/3/library/socket.html)

# Future Work

* Build a GUI instead of running this on a CLI
