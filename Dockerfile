FROM python:3
ADD blackjack.py/ card.py/ deck.py/ hand.py
EXPOSE 5000
CMD ["python3", "./blackjack.py"]