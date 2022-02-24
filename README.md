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
* [Exploring our database](#explore)
* [Graph analysis](#analysis)
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


<a name="explore"/>
## Exploring our database

You can explore our database following the next steps:
-  download a copy of our database [here](https://secrierlab.github.io/projects/). It is a zip file including all the necessary files.
-  You will need a version of the Neo4j software running in your computer. We have used the open source version [Neo4j Community Edition](https://neo4j.com/download-center/#community).
-  Ensure the system service is not running on your machine. In Linux:
<pre><code> sudo systemctl stop neo4j.service </pre></code>
-  Unzip the same graph.db.zip into the appropriate database folder. By default in Linux <neo4j-home>/data/database
- Restart the Neo4j system service
<pre><code> sudo systemctl start neo4j.service 
sudo systemctl enable neo4j.service
</pre></code>
- Ensure Neo4j us running:
  <pre><code> sudo systemctl enable neo4j.service </pre></code>
  
> You can see a live demo in:

[<img width="342" alt="Live demo" src="https://user-images.githubusercontent.com/9571043/155316306-bd8b2b9a-b224-4061-9d1f-de707ddd9543.png">](https://user-images.githubusercontent.com/9571043/155308305-37cf3912-f0ee-4020-a2c2-52c77b8c925c.mp4)



<a name="analysis"/>
## Graph analysis
Once you have an operational copy of our database you can replicate the queries we conduct in the paper for our analysis following the Jupyter notebook in.
  

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
