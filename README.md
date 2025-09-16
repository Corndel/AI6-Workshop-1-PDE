# AI6-Workshop-1-PDE
This is the first workshop of the Level 6 AI/ML Engineer programme

## Phase 1: Deploy Infrastructure with CloudFormation

### 1. Navigate to CloudFormation:

1. Access the AWS Management Console by your preferred method. For example, launch an AWS AI Cloud Sandbox from [A Cloud Guru](https://app.pluralsight.com/hands-on/playground/ai-sandboxes).

> The **AWS Management Console** is a web-based interface that allows users to access and manage AWS services visually. It provides tools for configuring, monitoring, and deploying cloud resources without needing to use the command line.

> **A Cloud Guru** is an online learning platform that specializes in cloud computing education, offering courses and hands-on labs for AWS, Azure, Google Cloud, and other technologies. You should be able to access it with the PluralSight credentials you were given when you joined the programme. If you haven't got these, or you've had trouble with the account, please let your Coach know and they'll be able to help.

2. In the AWS Management Console, search for and select "CloudFormation".

> AWS **CloudFormation** is a service that helps you model and set up your AWS resources using templates written in JSON or YAML. It automates the provisioning and management of infrastructure, making deployments repeatable and consistent.

### 2. Create the Stack:

> A **Stack** is a collection of AWS resources that are created, updated, or deleted together as a single unit based on a template. It allows you to manage infrastructure as code, so you can deploy and manage resources consistently and repeatedly.

1. Click the "Create stack" button and choose "With new resources (standard)".
2. Under "Specify template", select "Upload a template file".
3. Click "Choose file" and select the *setup-environment.yaml* file from this repo (after it's been cloned to your local machine).

> An **AWS CloudFormation YAML file** (like *setup-environment.yaml*) is a text-based template written in YAML syntax that defines the infrastructure and configuration of AWS resources. It describes what resources to create (like EC2 instances, S3 buckets, etc.) and how they should be configured, enabling automated and repeatable deployments.

4. Click "Next".

### 3. Configure stack details

1. For the "Stack name", enter QuickLoan-Infra.
2. Click "Next".
3. On the "Configure stack options" page, you don't need to change anything, but you do need to tick the "I acknowledge that AWS CloudFormation might create IAM resources." box at the bottom of the page.
4. Click "Next" again.
5. Scroll to the bottom of the "Review" page and click "Submit".

### 4. Wait for stack creation to complete

1. Wait for the status for this stack in the "Stacks" panel to change from `CREATE_IN_PROGRESS` to `CREATE_COMPLETE`. This may take a few minutes and you may want to click the "Refresh" button in the "Stacks" panel to check progress.

## Phase 2: Upload Data to the S3 Bucket
### 1. Navigate to S3

1. In the AWS Management Console, search for and select "S3".

> Amazon **S3** (Simple Storage Service) is a scalable object storage service that allows you to store and retrieve any amount of data from anywhere on the web. It's commonly used for backup, archiving, hosting static websites, and serving files for applications.

### 2. Find your Bucket

1. In the list of buckets, find the one that was just created as part of your stack. Its name will start with `quickloan-ml-`.
2. Click on the bucket name.

### 3. Create the 'input' Folder

1. Click the "Create folder" button.
2. For the "Folder name", type `input`.
3. Click "Create folder".

### 4. Upload the Dataset

1. Click on the `input` folder you just created to navigate inside it.
2. Click the "Upload" button. (There may be a couple; you can use either.)
3. On the upload page, click "Add files".
4. Select the *cs-training.csv* file from the *AI6-Workshop-1-PDE/data* directory on your local machine.
5. Click the "Upload" button at the bottom of the page. (This should only take a few seconds, depending on your upload speed.)

## Phase 3: Run the Pipeline in JupyterLab
### 1. Create a JupyterLab space

1. Navigate to the Amazon SageMaker AI service in the AWS environment. (Note that Amazon SageMaker AI was formerly named Amazon SageMaker. The latter is still available in the search in AWS Console, but you will only receive a notice of the name change if you navigate there. You should use the former.)

> **Amazon SageMaker AI** is a fully managed service from AWS that simplifies the process of building, training, and deploying machine learning (ML) models at scale. It provides an integrated development environment, pre-built algorithms, automated model tuning, and tools for data preparation, monitoring, and governance, making it easier for developers and data scientists to create production-ready AI solutions.

2. Click "Studio" under "Applications and IDEs" on the left.
3. Click "Open Studio", which will open SageMaker Studio in a new tab.
4. Select JupyterLab from the icons on the left. Create a new JupyterLab Space by clicking the "Create JupyterLab space" button.

> **JupyterLab** is an open-source web-based interactive development environment for working with notebooks, code, and data. It supports multiple programming languages (like Python, R, and Julia) and provides a flexible interface for data science, machine learning, and scientific computing workflows.

5. Name your JupyterLab e.g. `QuickLoan` and click "Create space".
6. Open your JupyterLab space by clicking "Run space". This can take a minute or so. (Pay attention to the notification at the bottom of the screen, which will give you a time estimate for completion.)
7. Once the space is ready, click "Open JupyterLab".

### 2. Upload the Code

1. Using the file browser on the left, upload the *deploy_pipeline.py* script and the *src* folder (with its contents) from the GitHub repository into your JupyterLab environment. It's important that you match the folder structure of the repository i.e. that the *src* folder is adjacent to the *deploy_pipeline.py* script.

### 3. Create and Run a Notebook

1. In the JupyterLab menu, click the "Python 3 (ipykernel)" button under the "Notebook" heading in the Launcher tab, *or* click File -> New -> Notebook. Select the default Python 3 kernel.
2. A new .ipynb notebook will open. It's important that this has opened at the top level (i.e. adjacent to the *src* folder, *not* within it), otherwise subsequent commands won't work. Your folder structure should look like this:

```
src/
    evaluate.py
    process.py
deploy_pipeline.py
Untitled.ipynb
```

3. In the first cell of the notebook, type the following command that executes your script: `!python deploy_pipeline.py`
4. Click the "Run" button (a ▶ play icon) in the notebook toolbar to execute the cell.
5. You will see the script's output directly in the notebook. While it's still running, you can navigate to SageMaker Studio -> Pipelines, then click through to your pipeline, and finally through to a specific execution of that pipeline, or order to see the visual graph of your pipeline running.


## Phase 4: Reflect on the Ethics of this Pipeline

Your coach will guide you in your discussion of the Ethics task related to this pipeline.

<img src="Ethics First AI.png"><br>

We have created for you a cheat sheet (above) of the most important ethical tasks at each stage.

By now, your pipeline has been executing for several minutes. The data has been processed, and the XGBoost model is being trained on a powerful cloud instance. Soon, a file named model.tar.gz will be created and saved to S3. While the pipeline automates the technical steps, this is the perfect time to reflect on what this model file truly represents and the responsibilities that come with it.

### The Model as a Regulated Asset

A trained model file like model.tar.gz isn't just a technical asset; it's a concentration of data and decision-making logic, making it subject to numerous policies and regulations. For the QuickLoan model you are building, key considerations would include:

> Data Privacy: The cs-training.csv file contains sensitive financial information. Even if personally identifiable information is removed, the model is still a derivative of this data and falls under regulations like GDPR. Policies must govern its access to ensure it cannot be reverse-engineered to reveal information about the individuals in the training set.

> Intellectual Property: The trained model is a valuable corporate asset for the fictional "QuickLoan" company. The model.tar.gz file would be protected as a trade secret. Internal policies would strictly control who can access or copy this file to protect the company's investment.

> Fairness and Safety: Since this is a financial model for loan applications, fairness regulations from bodies like the UK's Financial Conduct Authority (FCA) are paramount. The model you are creating cannot be an unexplainable "black box." In a real-world scenario, the company would be required to prove that the model's decisions are fair and not discriminatory based on protected characteristics.

> Security and Export Controls: While less likely for this specific model, advanced AI models can be classified as dual-use technology. In such cases, transferring a model.tar.gz file across international borders could be restricted under national export control laws.

As you watch your pipeline complete in the AWS console, consider how these policies would shape the way your model.tar.gz file is stored, versioned, and ultimately deployed. This intersection of technology, law, and ethics is central to the role of a modern AI Engineer.
