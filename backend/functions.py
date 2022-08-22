from .models import Post, Comment


def make_birthday_date(year, month, day):
    match month:
        case 'January':
            month = '01'
        case 'February':
            month = '02'
        case 'March':
            month = '03'
        case 'April':
            month = '04'
        case 'May':
            month = '05'
        case 'June':
            month = '06'
        case 'July':
            month = '07'
        case 'August':
            month = '08'
        case 'September':
            month = '09'
        case 'October':
            month = '10'
        case 'November':
            month = '11'
        case 'December':
            month = '12'

    if int(day) < 10:
        day = '0' + str(day)

    return f'{year}-{month}-{day}'


def get_number_of_comments():
    posts = Post.objects.all()

    for post in posts:
        number_of_comments = Comment.objects.filter(post=post).count()
        if post.number_of_comments != number_of_comments:
            post.number_of_comments = number_of_comments
            post.save()


def update_user_parameters(user, profile_picture, last_name, first_name, gender, birthday):
    user.profile_img = profile_picture
    user.lastname = last_name
    user.firstname = first_name
    user.gender = gender
    user.birthday = birthday
    user.save()


def update_profile_parameters(profile, bio, location):
    profile.about = bio
    profile.location = location
    profile.save()