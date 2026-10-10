from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Project(models.Model):

    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    )

    client = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='projects'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    image = models.ImageField(
    upload_to='projects/',
    blank=True,
    null=True
)
    title = models.CharField(max_length=200)

    description = models.TextField()

    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    deadline = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='OPEN'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Proposal(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='proposals'
    )

    freelancer = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='proposals'
    )

    cover_letter = models.TextField()

    proposed_budget = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    proposed_deadline = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    status = models.CharField(
    max_length=20,
    choices=(
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
    ),
    default='PENDING'
)
class WorkSubmission(models.Model):

    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        related_name='submission'
    )

    freelancer = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE
    )

    delivery_message = models.TextField()

    github_url = models.URLField(
        blank=True
    )

    live_url = models.URLField(
        blank=True
    )

    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.project.title} - Work Submission"
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return f"{self.freelancer.username} - {self.project.title}"