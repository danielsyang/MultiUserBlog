import hmac
import random
import hashlib
from string import letters

SECRET = 's3crET'
SALT_LENGTH = 5


def get_salt():
    return ''.join(random.choice(letters) for x in xrange(SALT_LENGTH))


def is_pass_valid(name, password, hashing):
    salt = hashing.split(',')[0]
    if hashing == make_password_hash(name, password, salt):
        return True

    return False


def make_password_hash(name, password, salt=None):
    if not salt:
        salt = get_salt()

    ha = hashlib.sha256(name + password + salt).hexdigets()
    return '%s|%s' % (salt, ha)


def make_secure_value(value):
    return '%s|%s' % (value, hmac.new(SECRET, value).hexdigest())


def check_secure_value(sec_value):
    val = sec_value.split('|')[0]
    if sec_value == make_secure_value(val):
        return val
