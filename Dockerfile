FROM python:3

# set a directory for the app
WORKDIR /usr/src/cs491-devops-testing-final

# copy all the files to the container
COPY . .

# define the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "./blackjack.py"]