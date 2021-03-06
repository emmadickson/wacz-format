import hashlib, datetime

WACZ_VERSION = "1.0.0"


def support_hash_file(data):
    """Hashes the passed content using sha256"""
    return hashlib.sha256(data).hexdigest()


def now():
    return tuple(datetime.datetime.utcnow().timetuple()[:6])
