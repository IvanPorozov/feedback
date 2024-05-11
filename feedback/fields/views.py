from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import AddRecordForm
from .models import Record


def add_record(request):
    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            parent_comment_id = request.GET.get('parent_comment_id', None)
            Record.objects.create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                homepage=form.cleaned_data['homepage'],
                text=form.cleaned_data['text'],
                parent_comment_id=parent_comment_id
            )
            return read_comments(request)
    else:
        form = AddRecordForm(initial={'username': '', 'email': '', 'homepage': '', 'text': ''})
    return render(request, 'add_record.html', {'form': form})


def read_comments(request):
    main_comments = Record.objects.filter(parent_comment=None)

    sort_by = request.GET.get('sort_by')
    if sort_by in ['username', 'email', 'created_at']:
        main_comments = main_comments.order_by(sort_by)

    if request.GET.get('sort_direction') == 'desc':
        main_comments = main_comments.order_by(f'-{sort_by}')
    else:
        main_comments = main_comments.order_by(sort_by)

    paginator = Paginator(main_comments, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'read_comments.html', {'page_obj': page_obj})

