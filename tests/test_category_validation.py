import pytest
from django.forms import modelform_factory

from blog.models import Post

pytestmark = pytest.mark.django_db


def test_post_form_requires_category():
    form_class = modelform_factory(Post, fields=('category',))
    form = form_class(data={'category': ''})
    assert not form.is_valid()
    assert form.errors.as_data()['category'][0].code == 'required'


def test_category_deletion_preserves_post(post_with_published_location):
    post = post_with_published_location
    post.category.delete()
    post.refresh_from_db()
    assert post.category_id is None
