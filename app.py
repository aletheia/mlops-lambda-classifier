#!/usr/bin/env python3

from aws_cdk import core

from stacks.mlops_lambda_stack import MlopsLambdaClassifierStack


app = core.App()
MlopsLambdaClassifierStack(app, "mlops-lambda-classifier")

app.synth()
