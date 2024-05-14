from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import AddRecordForm
from .models import Record
import bleach

ALLOWED_TAGS = ['a', 'code', 'i', 'strong']
ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title']
}


def add_record(request):
    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            parent_comment_id = request.GET.get('parent_comment_id', None)

            cleaned_text = bleach.clean(
                form.cleaned_data['text'],
                tags=ALLOWED_TAGS,
                attributes=ALLOWED_ATTRIBUTES,
                strip=True
            )

            try:
                bleach.clean(cleaned_text, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES, strip=False)
            except ValueError as e:
                form.add_error('text', 'HTML content is not valid: {}'.format(e))
                return render(request, 'add_record.html', {'form': form})

            Record.objects.create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                homepage=form.cleaned_data['homepage'],
                text=cleaned_text,
                parent_comment_id=parent_comment_id
            )
            return redirect('read_comments')
    else:
        form = AddRecordForm(initial={'username': '', 'email': '', 'homepage': '', 'text': ''})
    return render(request, 'add_record.html', {'form': form})


def read_comments(request):
    main_comments = Record.objects.filter(parent_comment=None)

    sort_by = request.GET.get('sort_by')
    if sort_by in ['username', 'email', 'created_at']:
        main_comments = main_comments.order_by(sort_by)
    else:
        sort_by = 'created_at'
        main_comments = main_comments.order_by(f'-{sort_by}')

    if request.GET.get('sort_direction') == 'desc':
        main_comments = main_comments.order_by(sort_by)
    else:
        main_comments = main_comments.order_by(f'-{sort_by}')

    paginator = Paginator(main_comments, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'read_comments.html', {'page_obj': page_obj})

