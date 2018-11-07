import pytest
from news.views import home
from django.contrib.auth.models import AnonymousUser, User

# test health check endpoint
def test_index_page(client):
    expected = 'Application news portal Started'
    result = client.get('/health').content.decode("utf-8")
    assert expected in result

#test home page is available with desired view
@pytest.mark.django_db
def test_home_page(client):
    expected_content = [
      '<title>News Portal</title>',
      '<a class="nav-link" href=/pages/signup>Signup</a>',
      '<a class="nav-link" href=/accounts/login/>Login</a>'
    ]

    result = client.get('/')
    content = result.content.decode("utf-8")
    #print(content)

    for value in expected_content:
      assert value in content
    assert result.status_code == 200

## test login page is available with desired view
@pytest.mark.django_db
def test_login_page(client):

    expected_content = [
      '<button type="submit">Login</button>',
      '<input type="password" name="password" required id="id_password">',
      '<input type="text" name="username" autofocus required id="id_username">'
    ]

    result = client.get('/accounts/login/')
    content = result.content.decode("utf-8")

    for value in expected_content:
      assert value in content
    assert result.status_code == 200

## test singup page is availabe with desired view
@pytest.mark.django_db
def test_signup_page(client):

    expected_content = [
      '<button type="submit">Sign up</button>',
      '<input type="password" name="password2" required id="id_password2">',
      '<input type="password" name="password1" required id="id_password1">',
      '<input type="text" name="username" maxlength="150" autofocus required id="id_username">'
    ]

    result = client.get('/pages/signup')
    content = result.content.decode("utf-8")
    #print(content)
    for value in expected_content:
      assert value in content
    assert result.status_code == 200

# public request for category content
@pytest.mark.django_db
def test_public_category(client, django_user_model):
  #django_user_model.objects.create_user(username=username, password=password)
  expected_content = [
    '<p class="card-text">The poetic thing about basketball is that, occasionally, it leaves you speechless. The Golden State Warriors, in particular, are a team that has the ability to do that.  We’ve seen it a lot in the pas</p>',
    '<h5 class="card-title">Sport News</h5>',
    '<a href="/pages/news/2" class="btn btn-primary">Read More</a>'
  ]
  result = client.get('/pages/news?cat=1')
  content = result.content.decode("utf-8")
  #print(content)
  for value in expected_content:
    assert value in content
  assert result.status_code == 200

# premium user ask for premium content
@pytest.mark.django_db
def test_premium_category(client, django_user_model):
  expected_content = [
    '<h5 class="card-title">Once upon a time</h5>',
    '<p class="card-text">A page in an Oliver Twist book Oliver Twist Parish Boy&#39;s Progress is a title-character novel, written in 1838. It was written by Charles Dickens.  Storyline &#39;Oliver Twist&#39; The Parish Boy&#39;s Progress is</p>',
    '<a href="/pages/news/1" class="btn btn-primary">Read More</a>'
  ]
  username = "admin"
  password = "123456"
  client.login(username=username, password=password)
  result = client.get('/pages/news?cat=4')
  content = result.content.decode("utf-8")
  #print(content)
  for value in expected_content:
    assert value in content
  assert result.status_code == 200

# when public user asks premium category, this test should fail
@pytest.mark.django_db
@pytest.mark.xfail
def test_authorized_premium_category(client, django_user_model):
  expected_content = [
    '<h5 class="card-title">Once upon a time</h5>',
    '<p class="card-text">A page in an Oliver Twist book Oliver Twist Parish Boy&#39;s Progress is a title-character novel, written in 1838. It was written by Charles Dickens.  Storyline &#39;Oliver Twist&#39; The Parish Boy&#39;s Progress is</p>',
    '<a href="/pages/news/1" class="btn btn-primary">Read More</a>'
  ]
  result = client.get('/pages/news?cat=4')
  content = result.content.decode("utf-8")
  #print(content)
  for value in expected_content:
    assert value in content
  assert result.status_code == 200


@pytest.mark.django_db
@pytest.mark.xfail
def test_unauthorized_premium_category(client, django_user_model):
  expected_content = [
    '<h5 class="card-title">Once upon a time</h5>',
    '<p class="card-text">A page in an Oliver Twist book Oliver Twist Parish Boy&#39;s Progress is a title-character novel, written in 1838. It was written by Charles Dickens.  Storyline &#39;Oliver Twist&#39; The Parish Boy&#39;s Progress is</p>',
    '<a href="/pages/news/1" class="btn btn-primary">Read More</a>'
  ]
  result = client.get('/pages/news?cat=4')
  content = result.content.decode("utf-8")
  #print(content)
  for value in expected_content:
    assert value in content
  assert result.status_code == 200

  

@pytest.mark.django_db
@pytest.mark.xfail
def test_unauthorized_premium_content(client, django_user_model):
  expected_content = [
    '<h5 class="card-title">Once upon a time</h5>',
    '<p class="card-text">A page in an Oliver Twist book Oliver Twist Parish Boy&#39;s Progress is a title-character novel, written in 1838. It was written by Charles Dickens.  Storyline &#39;Oliver Twist&#39; The Parish Boy&#39;s Progress is</p>',
    '<a href="/pages/news/1" class="btn btn-primary">Read More</a>'
  ]
  result = client.get('/pages/news/5')
  content = result.content.decode("utf-8")
  print(content)
  for value in expected_content:
    assert value in content
  assert result.status_code == 200

@pytest.mark.django_db
def test_unauthorized_premium_content_error_msg(client, django_user_model):
  expected_content = [
    'Signup to view news'
  ]
  result = client.get('/pages/news/5')
  content = result.content.decode("utf-8")
  print(content)
  for value in expected_content:
    assert value in content
  assert result.status_code == 200

@pytest.mark.django_db
def test_authorized_premium_content(client, django_user_model):
  expected_content = [
    '<h1>Article Title</h1>',
    'Science News for Premium Users'
  ]

  username = "admin"
  password = "123456"
  client.login(username=username, password=password)
  result = client.get('/pages/news/5')
  content = result.content.decode("utf-8")
  print(content)
  for value in expected_content:
    assert value in content
  assert result.status_code == 200