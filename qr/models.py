from django.db import models


class OperatorCertification(models.Model):
    tac_number = models.CharField(max_length=20, unique=True)
    operator = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=50, unique=True)
    issued_date = models.DateField()
    expiry_date = models.DateField()
    company = models.CharField(max_length=100)
    project = models.CharField(max_length=100, blank=True, null=True)
    trainer = models.CharField(max_length=100)
    approver = models.CharField(max_length=100)
    enr_number = models.CharField(max_length=50, unique=True)
    level_categories = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Added profile pic field

    def __str__(self):
        return f"{self.name} - {self.tac_number}"
