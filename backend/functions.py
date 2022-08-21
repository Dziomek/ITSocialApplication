from .models import Post, Comment

def make_birthday_date(year, month, day):
    match month:
        case 'January':
            month = '1'
        case 'February':
            month = '2'
        case 'March':
            month = '3'
        case 'April':
            month = '4'
        case 'May':
            month = '5'
        case 'June':
            month = '6'
        case 'July':
            month = '7'
        case 'August':
            month = '8'
        case 'September':
            month = '9'
        case 'October':
            month = '10'
        case 'November':
            month = '11'
        case 'December':
            month = '12'

    return f'{year}-{month}-{day}'


def get_number_of_comments():
    posts = Post.objects.all()

    for post in posts:
        number_of_comments = Comment.objects.filter(post=post).count()
        post.number_of_comments = number_of_comments
        post.save()