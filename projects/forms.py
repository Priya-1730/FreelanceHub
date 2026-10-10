from django import forms
from .models import Project, Proposal
from .models import Project, Proposal, WorkSubmission


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        fields = [
            'category',
            'title',
            'description',
            'budget',
            'deadline',
        ]


class ProposalForm(forms.ModelForm):

    class Meta:
        model = Proposal

        fields = [
            'cover_letter',
            'proposed_budget',
            'proposed_deadline',
        ]
class WorkSubmissionForm(forms.ModelForm):

    class Meta:
        model = WorkSubmission

        fields = [
            'delivery_message',
            'github_url',
            'live_url',
        ]

        widgets = {
            'delivery_message': forms.Textarea(
                attrs={
                    'rows': 5,
                    'placeholder': 'Describe the completed work...'
                }
            ),

            'github_url': forms.URLInput(
                attrs={
                    'placeholder': 'https://github.com/...'
                }
            ),

            'live_url': forms.URLInput(
                attrs={
                    'placeholder': 'https://...'
                }
            ),
        }