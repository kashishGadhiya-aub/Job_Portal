from django.db import models
from company.models import Company

# Job model
class Job(models.Model):
    """
    Represents a job posting with details about the role.
    Attributes:
        - company: The company that posted the job.
        - title: The job title.
        - description: Details about the job.
        - location: Where the job is located.
        - salary_range: The salary range for the job.
        - tags: Optional tags to categorize the job.
    """

    # Link to the company posting the job
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    
    title = models.CharField(max_length=255)
    description = models.TextField() 
    location = models.CharField(max_length=255)

    salary_range = models.CharField(max_length=50)  
    tags = models.CharField(max_length=255, blank=True)  

    def __str__(self):
       
        return self.title
