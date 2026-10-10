from django.urls import path
from . import views

urlpatterns = [

    path(
        'create/',
        views.create_project,
        name='create_project'
    ),

    path(
        'my-projects/',
        views.client_projects,
        name='client_projects'
    ),

    path(
        'list/',
        views.project_list,
        name='project_list'
    ),
    path(
    '<int:project_id>/submit-work/',
    views.submit_work,
    name='submit_work'
),

    path(
        '<int:project_id>/proposals/',
        views.project_proposals,
        name='project_proposals'
    ),

    path(
        'proposal/<int:proposal_id>/accept/',
        views.accept_proposal,
        name='accept_proposal'
    ),
    path(
    '<int:project_id>/submission/',
    views.review_submission,
    name='review_submission'
),
path(
    '<int:project_id>/complete/',
    views.complete_project,
    name='complete_project'
),

    path(
        '<int:project_id>/',
        views.project_detail,
        name='project_detail'
    ),

    path(
        '<int:project_id>/proposal/',
        views.submit_proposal,
        name='submit_proposal'
    ),
    path(
    'my-proposals/',
    views.my_proposals,
    name='my_proposals'
),
]