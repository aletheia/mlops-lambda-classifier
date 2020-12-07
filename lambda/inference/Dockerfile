FROM public.ecr.aws/lambda/python:3.8

ARG FUNCTION_DIR="/var/task"

# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}

COPY ./index.py ${FUNCTION_DIR}
COPY ./classifier.py ${FUNCTION_DIR}
COPY ./requirements.txt ${FUNCTION_DIR}
COPY ./trained_model.mdl ${FUNCTION_DIR}

RUN pip3 install -r requirements.txt

# ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaruntimeclient" ] 
CMD [ "index.handler" ]