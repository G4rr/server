import query_builder
import os
import json

users_db = {
    "id": None,
    "username": None,
    "hash_password": None,
    "isAdmin": None
}

scanner_appliences_db = {
    "id": None,
    "provider": None,
    "access_key": None,
    "secret_key": None,
    "region": None,
    "instance_type": None,
    "vpc": None,
    "sg": None
}

scan_reports_db = {
    "id": None,
    "Date": None,
    "Report name": None,
    "Owner": None,
    "Type": None,
    "Path": None,
}

#
class Login:
    def __init__(self, username, password, isAdmin):
        self._username = username
        self._password = password
        self._isAdmin = isAdmin

    @property
    def get_username(self):
        return self._username

    def authentication():
        return True

    def registration():
        pass

from Crypto.PublicKey import RSA
class Keys:
    def __init__(self):
        key = RSA.generate(2048)
        self.__privateKey = (key.export_key())
        self.__publicKey = (key.publickey().export_key())

    def get_private_key(self):
        return str(self.privateKey)

    def get_public_key(self):
        return str(self.publicKey)


class Infrastructure:
    def __init__(self, sa_name=None, provider="aws", access_key=None, secret_key=None, region="eu-central-1", instance_type="t3.micro", vpc=None, sg_name=None):
        self.keys = Keys()
        self.sa_name = sa_name
        self.region = region
        self.provider = provider
        self.access_key=access_key
        self.secret_key=secret_key
        self.instance_type = instance_type
        self.vpc = vpc
        self.sg_name = sg_name

    def get_sa_name(self):
        return self.sa_name

    @property
    def get_provider(self):
        return self.provider

    @property
    def get_eak(self):
        return self.access_key

    @property
    def get_esk(self):
        return self.secret_key

    def get_region(self):
        return self.region

    def get_ec2_type(self):
        return self.instance_type

    def get_keys(self):
        return self.keys

    def get_vpc(self):
        return self.vpc

    def get_sg(self):
        return self.sg_name

    def build_iac():
        return True

    def destroy_iac():
        return True

class Scanners:
    def __init__(self, title=None, level="High", sa_name=None, url=None, scanners=None):
        self.title = title,
        self.level = level,
        self.sa_name = sa_name,
        self.url = url,
        self.scanners = scanners

    def scans(self):
        return True

    def get_filename(self):
        return self.title[0] + ".json"


public_instance_ip=""
