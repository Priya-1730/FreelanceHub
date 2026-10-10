from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ProjectForm, ProposalForm, WorkSubmissionForm
from .models import Project, Proposal, WorkSubmission

@login_required
def create_project(request):

    if request.user.role != 'CLIENT':
        return redirect('freelancer_dashboard')

    if request.method == 'POST':

        form = ProjectForm(request.POST)

        if form.is_valid():

            project = form.save(commit=False)

            project.client = request.user

            project.save()

            return redirect('client_dashboard')

    else:
        form = ProjectForm()

    return render(
        request,
        'projects/create_project.html',
        {'form': form}
    )


@login_required
def project_list(request):

    if request.user.role != 'FREELANCER':
        return redirect('client_dashboard')

    projects = Project.objects.filter(
        status='OPEN'
    ).order_by('-created_at')

    search = request.GET.get('search')

    if search:
        projects = projects.filter(
            title__icontains=search
        )

    return render(
        request,
        'projects/project_list.html',
        {
            'projects': projects,
            'search': search
        }
    )

@login_required
def project_detail(request, project_id):

    if request.user.role != 'FREELANCER':
        return redirect('client_dashboard')

    project = Project.objects.get(
        id=project_id
    )

    return render(
        request,
        'projects/project_detail.html',
        {'project': project}
    )


@login_required
def submit_proposal(request, project_id):

    if request.user.role != 'FREELANCER':
        return redirect('client_dashboard')

    project = Project.objects.get(
        id=project_id
    )

    if request.method == 'POST':

        form = ProposalForm(request.POST)

        if form.is_valid():

            proposal = form.save(commit=False)

            proposal.project = project
            proposal.freelancer = request.user

            proposal.save()

            return redirect('project_list')

    else:
        form = ProposalForm()

    return render(
        request,
        'projects/submit_proposal.html',
        {
            'form': form,
            'project': project
        }
    )
@login_required
def project_proposals(request, project_id):

    if request.user.role != 'CLIENT':
        return redirect('freelancer_dashboard')

    project = Project.objects.get(
        id=project_id,
        client=request.user
    )

    proposals = Proposal.objects.filter(
        project=project
    ).order_by('-created_at')

    return render(
        request,
        'projects/project_proposals.html',
        {
            'project': project,
            'proposals': proposals
        }
    )
@login_required
def project_proposals(request, project_id):

    if request.user.role != 'CLIENT':
        return redirect('freelancer_dashboard')

    project = Project.objects.get(
        id=project_id,
        client=request.user
    )

    proposals = Proposal.objects.filter(
        project=project
    ).order_by('-created_at')

    return render(
        request,
        'projects/project_proposals.html',
        {
            'project': project,
            'proposals': proposals
        }
    )
@login_required
def client_projects(request):

    if request.user.role != 'CLIENT':
        return redirect('freelancer_dashboard')

    projects = Project.objects.filter(
        client=request.user
    ).order_by('-created_at')

    return render(
        request,
        'projects/client_projects.html',
        {
            'projects': projects
        }
    )
@login_required
def accept_proposal(request, proposal_id):

    if request.user.role != 'CLIENT':
        return redirect('freelancer_dashboard')

    proposal = Proposal.objects.get(
        id=proposal_id,
        project__client=request.user
    )

    if request.method == 'POST':

        proposal.status = 'ACCEPTED'
        proposal.save()

        Project.objects.filter(
            id=proposal.project.id
        ).update(status='IN_PROGRESS')

        Proposal.objects.filter(
            project=proposal.project
        ).exclude(
            id=proposal.id
        ).update(status='REJECTED')

        return redirect(
            'project_proposals',
            project_id=proposal.project.id
        )

    return redirect(
        'project_proposals',
        project_id=proposal.project.id
    )
@login_required
def my_proposals(request):

    if request.user.role != 'FREELANCER':
        return redirect('client_dashboard')

    proposals = Proposal.objects.filter(
        freelancer=request.user
    ).select_related(
        'project'
    ).order_by('-created_at')

    return render(
        request,
        'projects/my_proposals.html',
        {
            'proposals': proposals
        }
    )
@login_required
def submit_work(request, project_id):

    if request.user.role != 'FREELANCER':
        return redirect('client_dashboard')

    project = Project.objects.get(
        id=project_id
    )

    if project.status != 'IN_PROGRESS':
        return redirect(
            'project_detail',
            project_id=project.id
        )

    # Check if work has already been submitted
    if WorkSubmission.objects.filter(
        project=project
    ).exists():

        return redirect(
            'my_proposals'
        )

    if request.method == 'POST':

        form = WorkSubmissionForm(request.POST)

        if form.is_valid():

            submission = form.save(commit=False)

            submission.project = project
            submission.freelancer = request.user

            submission.save()

            return redirect(
                'my_proposals'
            )

    else:

        form = WorkSubmissionForm()

    return render(
        request,
        'projects/submit_work.html',
        {
            'form': form,
            'project': project
        }
    )
@login_required
def review_submission(request, project_id):

    if request.user.role != 'CLIENT':
        return redirect('freelancer_dashboard')

    project = Project.objects.get(
        id=project_id,
        client=request.user
    )

    submission = WorkSubmission.objects.get(
        project=project
    )

    return render(
        request,
        'projects/review_submission.html',
        {
            'project': project,
            'submission': submission
        }
    )
@login_required
def complete_project(request, project_id):

    if request.user.role != 'CLIENT':
        return redirect('freelancer_dashboard')

    project = Project.objects.get(
        id=project_id,
        client=request.user
    )

    if request.method == 'POST':

        project.status = 'COMPLETED'
        project.save()

        return redirect(
            'client_projects'
        )

    return redirect(
        'review_submission',
        project_id=project.id
    )