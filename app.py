#!/usr/bin/env python3

from aws_cdk import core

from stacks.mlops_lambda import MlopsLambdaClassifierStack


app = core.App()
MlopsLambdaClassifierStack(app, "mlops-lambda-classifier")

app.synth()
