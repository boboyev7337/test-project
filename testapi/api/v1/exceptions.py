from rest_framework.exceptions import APIException


class ImageException(APIException):
    status_code = 400
    default_detail = 'Rasmni joyi katta'
    default_code = 'rasmni_joyi_katta'
