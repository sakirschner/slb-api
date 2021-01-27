# Student LeaderBoard API
Student Leader Board API Source Code Built With <a href="https://www.djangoproject.com/">Django</a>, <a href="https://www.django-rest-framework.org/">Django Rest Framework</a>, and Python. The application is intended create and store class room data on students and their achievements so it can be utilized as a way to gameify their classroom performance and encourage better participation, esepcially in a remote learning environment. 

Once up and running you can create, manipulate, and access data by either accessing the REST endpoints or via the admin portal.

The front end for this application can be found [here](https://github.com/sakirschner/student-leader-board-client).
<br><br>

## Getting Started
---
The API is fully dockerized so you can easily run a few commands to get the application up and running. (You must have docker installed on your machine to properly run the API. You can install docker <a href="https://docs.docker.com/get-docker/">here</a>.)  
- ### Build the docker image:
    - This step allows you to run the application with all of its dependencies without having to worry about your manchine's environment setup.
    <br><br>
        ```
        docker-compose build
        ```
- ### Apply migrations:
    - Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.
    <br><br>
        ```
        docker-compose run --rm app sh -c "python manage.py migrate"
        ```
- ### Run the server:
    - This will spin up a server on your machine for local development.
    <br><br>
        ```
        docker-compose up
        ```
The API will now be running on port 8000 and is accessible via <a href="http://localhost:8000">localhost:8000</a>.
<br><br>

## Using the API
--- 
If you navigate to the url you will be able to view and test all the API endpoints. 

![Django Rest Framework Interface](rest.png)

However, most of the endpoints require an access token, so in order to properly use the api you must follow these steps.
- ### Create a superuser
    - A superuser will have permission for all the acpabilities of the API. This will also give you access to the admin portal which is described below.
        <br><br>
        ```
        docker-compose run --rm app sh -c "python manage.py createsuperuser"
        ```  
    - Follow the instructions which prompt you to enter an email address and password.

- ### Generate an access token
    - Using your superuser credentials you can make a ```POST``` request to generate a new access token to the following url with the JSON body:
        <br><br>
        ```
        http://localhost:8000/api/user/token/

        {
            "email": <SUPERUSER EMAIL>,
            "password": <SUPERUSER PASSWORD>
        }
        ```
    - The response will return a token in JSON format like the example below:
    <br><br>
        ```
        {
            "token": "4c96699425993cbd8f5417a911fc497bc3921bd7"
        }
        ```

- ### Use the access token for your requests
    - Using the token that you generated above you can now apply this to your Request Headers for any API call. Follow the format below:
    <br><br>
        ```
        {
            "Authorization": "Token 4c96699425993cbd8f5417a911fc497bc3921bd7"
        }
        ```

If you intend to access the api endpoints via the browser you must use an extension like <a href="https://chrome.google.com/webstore/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj?hl=en">ModHeader</a> to set the request headers in the browser.
<br><br>

### Admin Portal
One of the most powerful parts of Django is the admin interface. Here you can access and manipulate data from a user interface without the need for JSON and calling end points.

![Admin Portal](admin.png)

In order to access the portal use your superuser credentials from above to log in at <a href="http://localhost:8000/admin">localhost:8000/admin</a>.
<br><br>

## Testing
---
This project runs automated tests using tools provided by Python, Django, and Django Rest Framework. In ordedr to run the tests use the following command:

```
docker-compose run --rm app sh -c "python manage.py test"
```
<br>

## CI/CD
---
This project uses a few tools in order to assist with CI/CD which are not necessary for local development/testing but will be discussed here.

- ## Terraform 
    <a href="https://www.terraform.io/">Terraform</a> is an infastrcture as code platform that manages the cloud services this project uses for hosting, which is handled via Amazon Web Services. Defined in the deploy directory of this project, Terraform spins up everything needed to properly host the API via AWS during the CI/CD pipeline. It also provides the nevcessary tools to easily tear down the entire envitonment. In order to run Terraform locally you'll need to have:
    <br><br>
    - Access to the AWS account as an IAM user. Please contact scottakdev@gmail.com for more information.
    - Install <a href="https://github.com/99designs/aws-vault">AWS Vault</a> on your machine with the proper AWS credentials defined below.
        - AWS Vault is a tool to securely store and access AWS credentials in a development environment.
        - Once installed add your AWS username to the vault:
            ```
            aws-vault add <YOUR USERNAME>
            ```
            You'll be prompted to enter your Access key ID and Secret Key which can be found in the IAM portal of the AWS Console. Follow users > USERNAME > security credentials. You'll then be asked to enter a password to store your information.
        - Open the config file:
            ```
            vi ~/.aws/config
            ```
        - Underneath your username add these credentials:
            ```
            region=us-east-1
            mfa_serial=<Assigned MFA device>
            ```
            Your MFA serial can be found in the smae location as your Access key ID.
        - Start a new session
            ```
            aws-vault exec <YOUR USERNAME>
            ```
            On windows machines run:
             ```
            aws-vault exec <YOUR USERNAME> -- cmd.exe
            ```           
            You'll be prompted to enter in your MFA token and your password.
            <br><br>

    With AWS Vault configured you can now initialize Terrform:
    
    - Make sure you have your AWS Vault session running on the terminal you wish to run Terraform on: 
        ```
        aws-vault exec <YOUR USERNAME>
        ```
        Or for windows:
        ```
        aws-vault exec <YOUR USERNAME> --cmd.exe
        ```
    - Initialize Terraform
        ```
        docker-compose -f deploy/docker-compose.yml run --rm terraform init
        ```
    - Switch to the dev environment
        ```
        docker-compose -f deploy/docker-compose.yml run --rm terraform workspace select dev
        ```

    Now you can make changes to the terrform code and run these commands:
    - Format - formats the code to Terrform standard
        ```
        docker-compose -f deploy/docker-compose.yml run --rm terraform fmt
        ```
    - Validate - validates the code to make sure there are no errors
        ```
        docker-compose -f deploy/docker-compose.yml run --rm terraform validate
        ```
    - Plan - this will give you a full rundown of all the AWS services affected by your code
        ```
        docker-compose -f deploy/docker-compose.yml run --rm terraform plan
        ```

    There is no need to apply the Terraform code as that is taken care of in the CI/CD pipeline.
    <br><br>

- ## GitLab

    This project encorporates GitLab Pipelines in order to automate the CI/CD process.
    <br><br>
    - <a href="https://gitlab.com/sakirschner/slb-api/-/pipelines">GitLab Pipelines for this project</a>. For access to the piplines please contact scottakdev@gmail.com.
    <br><br>

    The code for this can be found in ```.gitlab-ci.yml``` in the root directory. When the code is pushed to the ```dev``` branch the pipeline will be initiated to update the dev environment, and when it is pushed to the ```production``` branch the pipeline will be initiated to update the production environment. This of course is assuming all tehe steps in the pipeline pass.
<br><br>

## Proxy
---
The official <a href="https://www.djangoproject.com/">Django documentation</a> reccomends using a proxy server in front of applications in order to serve static files due to Django not being efficient in doing so. 

The proxy server for this application is built using <a href="https://www.nginx.com/">NGINX</a> specifically designed to serve static files and is served with <a href="https://uwsgi-docs.readthedocs.io/en/latest/">uWSGI</a>. 
<br><br>
<a href="https://gitlab.com/sakirschner/student-leader-board-api-proxy">The source code for the proxy server can be found here</a>.

- ## Run the app using the proxy in the uWSGI mode locally
    In order to test the proxy deployment locally this project is set up with a docker-compose file to do just that. This allows you to switch the API to use the proxy in the uWSGI mode instead of using the Django development server which is defined in the main Dockerfile. There are of course some dependencies.

    - Clone the proxy
        
        You must have the proxy installed on your machine before you can continue with the rest of the steps. You can clone the repo <a href="https://gitlab.com/sakirschner/student-leader-board-api-proxy">here</a>.
    - Build and tag the docker image
        
        In the root of the proxy directory run this command:
        ```
        docker build -t proxy .
        ```
        This will ensure the correct dependency for running the application behind the proxy is set up locally.
    - Run the app behind the proxy
        ```
        docker-compose -f docker-compose-proxy.yml up
        ```
<br>

## Questions?
---
Please contact Scott Kirschner 

Email: scottakdev@gmail.com
<br>
Website: scottakirschner.com