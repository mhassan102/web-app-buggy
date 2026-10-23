from flask import request


class Directory:
    def search(self, filterstr):
        return filterstr


directory = Directory()


def ldap_lookup():
    username = request.args.get("user", "")
    return directory.search(f"(uid={username})")  # BUG: ldap_injection — user is interpolated into the LDAP filter
