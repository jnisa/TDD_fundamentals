## **Data & Cloud Engineering**

Introduction to Data Engineering and Cloud paradigm, relies on Python as the programming language across all the strands (Data Manipulation and Visualization) and AWS as the cloud the service to wrap-up the Python modules already mentioned. This course covers the most common practices that you will be involved with while working on the Analytics & Cognitive department, and more specifically in the Data Engineering Team.

This course will rely on the following programme:
>- Day 1: Functional Programming + Jupyter Notebooks + Exploratory Data Analysis (EDA) + Data Visualization 
>- Day 2: AWS Cloud Enginnering: Ingestion (boto3) + Storage (S3) + Transformation (AWS Lambda) + GitOps
>- Day 3: Test Drive Development (TDD) + AWS Cloud Engineering: Transformation (AWS Lambda) + Orchestration (AWS Step Functions) + GitOps
>- Day 4: AWS Cloud Engineering: Virtualized DW (AWS Athena) + Enrichment (AWS Lambda + AWS StepFunctions) + GitOps

### **Requirements**

To thrive in the modules mentioned above it is required the possession of the following:
>- Python (v3.7.0 or above)
>- Anaconda Navigator
>- Git Bash

### **Basic Git Operations**

Along the course (as you can see in the programme above) you will be challenged to get interaction with GitOps. To that matter, here is a cheatsheet where you can check on how to perform basic git interactions:

>- `git checkout [-b] [branch-name]`          - used to go to a specific git branch or create one (by adding `-b`);
>- `git clone [-b [branch-name]] [http-link]` - clone all the directories and files of the repository to your computer;
>- `git status`                               - check the changes that were made in your current git branch;
>- `git add .`                                - add the latest modifictions to your current branch;
>- `git commit -m "[commit-message]"`         - create a git commit with a message attached;
>- `git push origin [branch-name]`            - push the changes to branch specified;
>- `git pull origin [branch-name]`            - pull the latest version of the branch.

#### **To be considered**

To accomplish all the tasks in a proper manner you must take into account the following guidelines:

1. **The first thing that you must to do is to clone the branch `feature/launch-pad`** that has the structure of the code where you must add the product of what you are developing;
2. Your changes must be made in branch that follows the following syntax: `feature/[FirstName-LastName]`.