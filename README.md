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
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## Introduction
Tumour immunity is key for the prognosis and treatment of colon adenocarcinoma, but its characterisation remains cumbersome and expensive, requiring sequencing or other complex assays. Detecting tumour-infiltrating lymphocytes in haematoxylin and eosin (H&E) slides of cancer tissue would provide a cost-effective alternative to support clinicians in treatment decisions, but inter- and intra-observer variability can arise even amongst experienced pathologists when assessing a sample. Furthermore, the compounded effect of other cells in the tumour microenvironment is challenging to quantify but could yield useful additional biomarkers.

![image](https://user-images.githubusercontent.com/9571043/155305420-c473bbac-685a-432b-bb3e-bf8926a5f58f.png)



<a name="predicting"/>

## Predicting the Immunescore level and presence of cells

To predict the level of Immunescore and presence of cells, we used a model consisting of two parts: a convolutional neural network (CNN) feature extractor followed by a non-linear classifier. We based the feature extractor backbone in the InceptionV3 architecture. 

To train the model, first you have to arrange a folder structure of the dichotomised dataset such as:


  <pre><code>
  ├── train                  
  │   ├── high level class          
  │   └── low level class           
  └── test                  
      ├── high level class          
      └── low level class    
  </pre></code>
  
After, pointing to the path of your foldefr structure in the train.py file, to start the training you have only to run:

  <pre><code> python train.py </pre></code>
  
It will generate two graps showing the learning curves and accuracy performnace in the same folder than the train.py file is included. In addition, it will save the model for each epochs in a folder call weigths. 


<a name="explore"/>

## Exploring our database

You can explore our database following the next steps:
-  download a copy of our database [here](https://drive.google.com/file/d/1reNyA2uYW23SYnTMFCCgIBHov5voY6i7/view?usp=sharing/). It is a zip file including all the necessary files.
-  You will need a version of the Neo4j software running in your computer. We have used the open source version [Neo4j Community Edition](https://neo4j.com/download-center/#community).
- Ensure the system service is not running on your machine. In Linux:
  <pre><code> sudo systemctl stop neo4j.service </pre></code>
- Unzip the same graph.db.zip into the appropriate database folder. By default in Linux <neo4j-home>/data/database
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
Once you have an operational copy of our database you can replicate the queries we conduct in the paper for our analysis following the Jupyter notebook [in](https://github.com/secrierlab/TumourHistologyDL/blob/main/graph-analysis/queries_Neo4j.ipynb).
  



## Acknowledgements

- MPC was supported by an Academy of Medical Science Springboard award (SBF004\1042).
- GMT was supported by a Wellcome Seed Award in Science (215296/Z/19/Z).
-  MS was supported by a UKRI Future Leaders Fellowship (MR/T042184/1) and work in MS’s lab was supported by a BBSRC equipment grant (BB/R01356X/1) and a Wellcome Institutional Strategic Support Fund (204841/Z/16/Z).
 

## Contact
>To whom correspondence should be addressed [@msecrier](https://www.ucl.ac.uk/biosciences/people/dr-maria-secrier/) - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->
