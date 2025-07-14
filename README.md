# AI6-Workshop-1-PDE
This is the first workshop of the Level 6 AI/ML Engineer programme

## Phase 1: Deploy Infrastructure with CloudFormation

Navigate to CloudFormation:

In the AWS Management Console, search for and select "CloudFormation".

Create the Stack:

Click the "Create stack" button and choose "With new resources (standard)".

Under "Specify template", select "Upload a template file".

Click "Choose file" and select the setup-environment.yaml file from this repo (after it's been cloned to your local machine).

Click "Next".

Configure Stack Details:

For the "Stack name", enter QuickLoan-Infra.

Click "Next".

On the "Configure stack options" page, you don't need to change anything. Click "Next" again.

Acknowledge and Submit:

Scroll to the bottom of the "Review" page.

You must check the box that says "I acknowledge that AWS CloudFormation might create IAM resources."

Click "Create stack". Wait for the status to change from CREATE_IN_PROGRESS to CREATE_COMPLETE.

## Phase 2: Upload Data to the S3 Bucket
Navigate to S3:

In the AWS Management Console, search for and select "S3".

Find Your Bucket:

In the list of buckets, find the one you just created. Its name will start with quickloan-ml-. Click on the bucket name.

Create the 'input' Folder:

Click the "Create folder" button.

For the "Folder name", type input.

Click "Create folder".

Upload the Dataset:

Click on the input folder you just created to navigate inside it.

Click the "Upload" button.

On the upload page, click "Add files".

Select the cs-training.csv file from the AI6-Workshop-1-PDE/data directory on your local machine.

Click the "Upload" button at the bottom of the page.

## Phase 3: Run the Pipeline in JupyterLab
Launch SageMaker Studio:

Navigate to the Amazon SageMaker service in the AWS environment.

Select JupyterLab from the icons on the left. Create a new JupyterLab Space.

Open your JupyterLab space from the Studio dashboard.

Upload the Code:

Using the file browser on the left, upload the deploy_pipeline.py script and the src folder (with its contents) from the GitHub repository into your JupyterLab environment.

Create and Run a Notebook:

In the JupyterLab menu, click File -> New -> Notebook. Select the default Python kernel.

A new .ipynb notebook will open.

In the first cell, type the following line. This is a "magic command" that executes your script.

!python deploy_pipeline.py

Click the "Run" button (a ▶ play icon) in the notebook toolbar to execute the cell.

You will see the script's output directly in the notebook. Once it finishes, you can navigate to Amazon SageMaker -> Pipelines in the console to see the visual graph of your pipeline running.

## Phase 4: Reflect on the Ethics of this Pipeline

Your PDE will guide you in your discussion of the Ethics task related to this pipeline.
