# MLOps with Container support for AWS Lambda
This project is a showcase to demonstrate how the recently added [Container support for AWS Lamnda](https://aws.amazon.com/it/blogs/aws/new-for-aws-lambda-container-image-support/), introduced at re:Invent 2020 can be a game changer and open new possibilities.

## Container support for AWS Lambda
At re:Invent 2020, AWS announced a long-awaited update for AWS Lambda by many developers and data scientists because it could change the way we build functions. It comes with bonus features that make this release something very welcome in the serverless world: starting from today it is possible to package a lambda function starting from an OCI file format.
The best part is that a custom Dockerfile could either extend a lambda base image, provided by AWS for any supported runtime and published on DockerHub, or start from a fresh Alpine or Debian image, thus customizing Linux dependencies, packages, and everything we usually do with a dockerized app container.
This has some serious implications for people willing to use AWS Lambda to serve the machine learning model.
Moreover a new announced feature of container image support for AWS Lambda is the image size limit of 10GB. This means a lot to us: all the libraries required by a machine learning stack and even the weights of the model can now be packaged and published to a docker registry

More info about container support for AWS Lambda can be found:
* in the [AWS Blog launch post](https://aws.amazon.com/it/blogs/aws/new-for-aws-lambda-container-image-support/)
* in [this article](https://towardsdatascience.com/serverless-comes-to-machine-learning-with-container-image-support-in-aws-lambda-ee9d729d48d7)

## About this use case
This repository has the goal to show how a machine learning model can be packaged and deployed to AWS Lambda with no effort. We choose to focus on a common problem in Customer Experience: customer churn. We used a dataset publicly [available on Kaggle](https://www.kaggle.com/sakshigoyal7/credit-card-customers) to train our machine learning model with scikit-learn on tabular data. For our use case, we leveraged an already implemented **DecisionTree** as shown in a [couple of examples on kaggle](https://www.kaggle.com/sakshigoyal7/credit-card-customers/notebooks).

A Jupyter Notebook with the implemented training model and its evaluation (using F1 score) can be found in **notebooks** folder. A raw python version of this trained model, without feature encoding (since encoded feature don't correlate with attrition) is available in **src/training**. A sample request to the deployed model can be run from **api/inference.http** after code deploy.

## Getting started
Starting using this repo is as easy as just checkout and deploy

```bash
git clone https://github.com/aletheia/mlops-lambda-classifier.git
cd mlops-lambda-classifier
```

Then we have to choose the preferred deployment method: bash script or AWS CDK.

### Bash script deployment
Assuming the AWS CLI is configured with your credentials:
```bash
cd script
./create-function.sh
```

To update the function code after changes to **lambda/inference** code:

```bash
./update-function
```

### Function deployment with AWS CDK
Here we use the [released Container support in AWS CDK](https://github.com/aws/aws-cdk/issues/11809) support, released since v1.76
Assuming the AWS CLI is configured with your credentials, the deploy is pretty straightforward, just like any standart AWS CDK deploy:
```bash
cdk deploy
```
