NAME=churn-classifier
FUNCTION_VERSION=v_$(date +%F-%H-%M-%S)

cd ../lambda/inference
echo "docker build . -t $NAME"
docker build . -t $NAME:$FUNCTION_VERSION

REGION=eu-west-1
ACCOUNT_ID=$(aws sts get-caller-identity | jq -r '.Account')
echo "aws ecr get-login-password --region $REGION| docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com"
aws ecr get-login-password --region $REGION| docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com

# Create image repo if it exists
echo "aws ecr create-repository --repository-name $NAME --image-tag-mutability MUTABLE --image-scanning-configuration scanOnPush=true"
aws ecr create-repository --repository-name $NAME --image-tag-mutability MUTABLE --image-scanning-configuration scanOnPush=true

IMAGE_URI=$(aws ecr describe-repositories | jq -r '.repositories[1].repositoryUri')

REMOTE_IMAGE=$ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$NAME:$FUNCTION_VERSION
echo "docker tag $NAME:$FUNCTION_VERSION $REMOTE_IMAGE"
docker tag $NAME:$FUNCTION_VERSION $REMOTE_IMAGE

echo "Pushing to $REMOTE_IMAGE"
docker push $REMOTE_IMAGE

echo "Create LAMBDA"
aws lambda --region $REGION create-function --function-name ChurnClassifier --package-type Image --code ImageUri=$IMAGE_URI:$FUNCTION_VERSION --role arn:aws:iam::$ACCOUNT_ID:role/ChurnClassifier

