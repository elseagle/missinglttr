import random
import string
def code_generator(size=6, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    newClass = instance
    code_exists_in_db = newClass.objects.filter(shortcode=new_code).exists()
    if code_exists_in_db:
        return create_shortcode(size=size)
    return new_code

