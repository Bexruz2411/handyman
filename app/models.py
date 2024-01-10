from django.db import models

class Header(models.Model):
    title = models.CharField(max_length=255)

class Body(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=255)

class Card(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=255)

class Leader(models.Model):
    title = models.CharField(max_length=255)

class LeaderCards(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=255)

class Testimonials(models.Model):
    text = models.TextField(max_length=255)
    username = models.CharField(max_length=255)
    job = models.CharField(max_length=255)

class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(max_length=255)
    admin = models.CharField(max_length=255)
    text = models.TextField(max_length=255)


class AboutPage(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=255)

class AboutPageCompany(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=255)

class ServicesPage(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=255)

class Blogpage(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=255)
