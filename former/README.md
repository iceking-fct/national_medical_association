### Online Voting System in Python Django ###



A fully functional project based on Online Voting System which uses Python with Django Web Framework. Following  Django project contains all the important features which can be in use for any election. It has a number of important features that will allow the voters to manage and vote online.



AUTHORS: [MIRACLE AMAJAMA](https://github.com/iceking-fct)

         SAMUEL EBILOMA (samuelebiloma208@gmail.com)

         GODWIN OKPEH




## About Online Voting System Django Project ##

This Python Django-based e-voting system focuses on facilitating secure online voting and managing voter and candidate information. The system also provides graphical representations of key data and robust voter record management capabilities.

The system is structured around two primary user roles: Voter and Administrator.

Voter Functionality: Registered voters can cast their votes and review their submitted ballots. To maintain election integrity, the system enforces a one-vote-per-voter restriction. While voters can select different candidates for various positions, they can only cast a single ballot. After voting, voters can access a record of their ballot, displaying the names of the candidates they selected.




## Admin Panel ##

The administrative panel provides comprehensive system control, enabling administrators to manage voters, candidates, positions, and other critical system parameters. Each managed element includes relevant details such as names and other pertinent information.

The initial system setup involves defining positions and candidates. Each position and candidate record includes specific fields, such as name, maximum allowable votes, and a biographical description. These elements are essential for ensuring the integrity and proper execution of the online voting process.

Positions are defined as the roles candidates are contesting in the upcoming election. To add a candidate, administrators must provide the candidate's designated position, name, biographical information, and a single photograph. These records are managed within their respective sections of the administrative panel.



## Voter Management and Votes ##

This system provides robust management of both voter data and vote records, accessible through an administrative panel.

Voter Management: Administrators are required to input comprehensive voter details, including name, email address, phone number, and a system-generated password for initial login credentials.

Vote Management: The system employs a systematic approach to vote counting and management, with real-time visibility provided to administrators via their panel. Following vote submission, administrators can generate detailed reports listing each voter's name, selected candidate, and the corresponding position. These reports are searchable within each data field, facilitating efficient data retrieval. Vote results can also be downloaded in PDF format.

Furthermore, administrators have the ability to view and manage ballot positions and update the election title at any time.




Technologies Used:	Python with Django templates, JavaScript, HTML5, CSS3.
Database:	PostgreSQL.
