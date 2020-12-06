import os
from aws_cdk import core
from aws_cdk.aws_lambda import Runtime, Function, Code
from aws_cdk.aws_apigateway import RestApi, LambdaIntegration, MockIntegration, PassthroughBehavior


class MlopsLambdaClassifierStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        inferenceFunction = Function(self, "MLOpsClassificationInferenceFunction",
                                           code=Code.asset(
                                               os.path.join(os.getcwd(), "./lambda/inference")),
                                           handler="index.handler",
                                           runtime=Runtime.PYTHON_3_8
                                     )

        base_api = RestApi(self, "MLOpsRestApi")

        classification_api = base_api.root.add_resource("classifier")
        classification_api_integration = LambdaIntegration(
            inferenceFunction, proxy=True, )
        classification_api.add_method("POST", classification_api_integration)

        self.add_cors_options(classification_api)

    def add_cors_options(self, apigw_resource):
        apigw_resource.add_method('OPTIONS', MockIntegration(
            integration_responses=[{
                'statusCode': '200',
                'responseParameters': {
                    'method.response.header.Access-Control-Allow-Headers': "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
                    'method.response.header.Access-Control-Allow-Origin': "'*'",
                    'method.response.header.Access-Control-Allow-Methods': "'GET,OPTIONS'"
                }
            }
            ],
            passthrough_behavior=PassthroughBehavior.WHEN_NO_MATCH,
            request_templates={"application/json": "{\"statusCode\":200}"}
        ),
            method_responses=[{
                'statusCode': '200',
                'responseParameters': {
                    'method.response.header.Access-Control-Allow-Headers': True,
                    'method.response.header.Access-Control-Allow-Methods': True,
                    'method.response.header.Access-Control-Allow-Origin': True,
                }
            }
        ],
        )
