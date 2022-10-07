from django import template

register = template.Library()


@register.filter(name='persian_int')
def persian_int(english_int):
    farsi_nums = ('۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹')
    number = str(english_int)
    return int(''.join(farsi_nums[int(digit)] for digit in number))
