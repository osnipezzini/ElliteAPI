import datetime
import random

from django.db import models


# Create your models here.

class Key(models.Model):
    key = models.CharField(max_length=50, null=True)
    valid_date = models.DateField(default=datetime.datetime.today() + datetime.timedelta(days=365))
    machine = models.CharField(max_length=50, null=True)

    def verify(self, key):
        score = 0
        check_digit = key[0]
        check_digit_count = 0
        chunks = key.split('-')
        for chunk in chunks:
            if len(chunk) != 4:
                return False
            for char in chunk:
                if char == check_digit:
                    check_digit_count += 1
                score += ord(char)
        if score == 1772 and check_digit_count == 5:
            return True
        return False

    def generate(self):
        key = ''
        chunk = ''
        alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'
        while True:
            while len(key) < 25:
                char = random.choice(alphabet)
                key += char
                chunk += char
                if len(chunk) == 4:
                    key += '-'
                    chunk = ''
            key = key[:-1]
            if self.verify(key):
                return key.upper()
            else:
                key = ''

    def __str__(self):
        return self.key

    def save(self, *args, **kwargs):
        if not self.key or not self.verify(self.key):
            self.key = self.generate()
        super(Key, self).save(*args, **kwargs)
