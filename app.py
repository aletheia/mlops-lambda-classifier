#!/usr/bin/env python3

from aws_cdk import core

from mlops_lambda_classifier.mlops_lambda_classifier_stack import MlopsLambdaClassifierStack


app = core.App()
MlopsLambdaClassifierStack(app, "mlops-lambda-classifier")

app.synth()
