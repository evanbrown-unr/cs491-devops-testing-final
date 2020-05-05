FROM python:3

# set a directory for the app
WORKDIR /usr/src/cs491-devops-testing-final

# copy all the files to the container
COPY . .

# run the command
CMD ["python", "./blackjack.py"]