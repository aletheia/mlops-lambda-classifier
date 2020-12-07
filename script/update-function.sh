NAME=churn-classifier
FUNCTION_NAME=ChurnClassifier
FUNCTION_VERSION=v_$(date +%F-%H-%M-%S)
cd ../lambda/inference
echo "docker build . -t $NAME"
docker build . -t $NAME:$FUNCTION_VERSION

REGION=eu-west-1
ACCOUNT_ID=$(aws sts get-caller-identity | jq -r '.Account')
echo "aws ecr get-login-password --region $REGION| docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com"
aws ecr get-login-password --region $REGION| docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com

IMAGE_URI=$(aws ecr describe-repositories | jq -r '.repositories[1].repositoryUri')

REMOTE_IMAGE=$ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$NAME:$FUNCTION_VERSION
echo "docker tag $NAME:$FUNCTION_VERSION $REMOTE_IMAGE"
docker tag $NAME:$FUNCTION_VERSION $REMOTE_IMAGE

echo "Pushing to $REMOTE_IMAGE"
echo "docker push $REMOTE_IMAGE"
docker push $REMOTE_IMAGE

echo "update LAMBDA"
echo "aws lambda update-function-code --function-name $FUNCTION_NAME --image-uri=$IMAGE_URI:$FUNCTION_VERSION"
aws lambda update-function-code --function-name $FUNCTION_NAME --image-uri=$IMAGE_URI:$FUNCTION_VERSION
