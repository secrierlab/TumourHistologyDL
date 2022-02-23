# Characteraising the immunological landscape and spatial architecture of colon cancer tissue

This is a Python implementation of the paper:

<pre><code>
@Article{graphbased,
  author  = {Mario Parreno-Centeno and Guidantonio Malagoli Tagliazucchi and Maria Secrier},
  title   = {A deep learning and graph-based approach to characterise the immunological landscape and spatial architecture of colon cancer tissue},
  journal = {arXiv preprint},
  year    = {2022},
}
</pre></code>












## Table of Contents
* [Introduction](#introduction)
* [Predicting the Immunescore level and presence of cells](#predicting)
* [Features](#features)
* [Graph analysis](#graph-analysis)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## Introduction
Tumour immunity is key for the prognosis and treatment of colon adenocarcinoma, but its characterisation remains cumbersome and expensive, requiring sequencing or other complex assays. Detecting tumour-infiltrating lymphocytes in haematoxylin and eosin (H&E) slides of cancer tissue would provide a cost-effective alternative to support clinicians in treatment decisions, but inter- and intra-observer variability can arise even amongst experienced pathologists when assessing a sample. Furthermore, the compounded effect of other cells in the tumour microenvironment is challenging to quantify but could yield useful additional biomarkers.

![image](https://user-images.githubusercontent.com/9571043/155305420-c473bbac-685a-432b-bb3e-bf8926a5f58f.png)



<a name="predicting"/>

## Predicting the Immunescore level and presence of cells
- Tech 1 - version 1.0
- Tech 2 - version 2.0
- Tech 3 - version 3.0


## Graph analysis
You can explore our database following the next steps:
-  download a copy of our database [here](https://secrierlab.github.io/projects/). It is a zip file including all the necessary files.
-  You will need an operational version of the Neo4j software running in your computer. We have used the open source version [Neo4j Community Edition](https://neo4j.com/download-center/#community).
-  Ensure the system service is not running on your machine:
'sudo systemctl start neo4j.service'
-  Unzip the same graph.db.zip into the appropriate database folder.
- Restart the Neo4j system service

sudo systemctl start neo4j.service
sudo systemctl enable neo4j.service
sudo systemctl status neo4j.service
sudo chmod -R 777 /var/lib/neo4j/data/databases/coad
vim /etc/neo4j/neo4j.conf
dbms.active_database = coad.db


You can  For tis work we used . Once you have downloaded a copy of database and installed Neo4j in your computer, to explore our databse you can simply copy the image of the databse to the folder your Neo4J data is stored. 

- Awesome feature 1
- Awesome feature 2
- Awesome feature 3
> Live demo:

[<img width="342" alt="Live demo" src="https://user-images.githubusercontent.com/9571043/155309678-cf766721-4ce9-4c48-aeb3-98ebf23f49db.png">](https://user-images.githubusercontent.com/9571043/155308305-37cf3912-f0ee-4020-a2c2-52c77b8c925c.mp4)


## Screenshots
![Example screenshot](./img/screenshot.png)
<!-- If you have screenshots you'd like to share, include them here. -->


## Setup
What are the project requirements/dependencies? Where are they listed? A requirements.txt or a Pipfile.lock file perhaps? Where is it located?

Proceed to describe how to install / setup one's local environment / get started with the project.


## Usage
How does one go about using it?
Provide various use cases and code examples here.

`write-your-code-here`


## Project Status
Project is: _in progress_ / _complete_ / _no longer being worked on_. If you are no longer working on it, provide reasons why.


## Room for Improvement
Include areas you believe need improvement / could be improved. Also add TODOs for future development.

Room for improvement:
- Improvement to be done 1
- Improvement to be done 2

To do:
- Feature to be added 1
- Feature to be added 2


## Acknowledgements

- MPC was supported by an Academy of Medical Science Springboard award (SBF004\1042).
- GMT was supported by a Wellcome Seed Award in Science (215296/Z/19/Z).
-  MS was supported by a UKRI Future Leaders Fellowship (MR/T042184/1) and work in MS’s lab was supported by a BBSRC equipment grant (BB/R01356X/1) and a Wellcome Institutional Strategic Support Fund (204841/Z/16/Z).
 

## Contact
>To whom correspondence should be addressed [@msecrier](https://www.ucl.ac.uk/biosciences/people/dr-maria-secrier/) - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->
