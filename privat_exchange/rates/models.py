from django.db import models

# Create your models here.

class Currency:
    id: int
    name: str
    buy: float
    sale: float