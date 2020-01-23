# coding: utf-8

"""
    Gkeep API

    Gkeep API  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class UserProfileGeoLocalizationSettings(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'service': 'str',
        'app_id': 'str',
        'api_key': 'str',
        'login': 'str',
        'password': 'str'
    }

    attribute_map = {
        'id': 'id',
        'service': 'service',
        'app_id': 'app_id',
        'api_key': 'api_key',
        'login': 'login',
        'password': 'password'
    }

    def __init__(self, id=None, service=None, app_id=None, api_key=None, login=None, password=None):  # noqa: E501
        """UserProfileGeoLocalizationSettings - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._service = None
        self._app_id = None
        self._api_key = None
        self._login = None
        self._password = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if service is not None:
            self.service = service
        if app_id is not None:
            self.app_id = app_id
        if api_key is not None:
            self.api_key = api_key
        if login is not None:
            self.login = login
        if password is not None:
            self.password = password

    @property
    def id(self):
        """Gets the id of this UserProfileGeoLocalizationSettings.  # noqa: E501


        :return: The id of this UserProfileGeoLocalizationSettings.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserProfileGeoLocalizationSettings.


        :param id: The id of this UserProfileGeoLocalizationSettings.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def service(self):
        """Gets the service of this UserProfileGeoLocalizationSettings.  # noqa: E501


        :return: The service of this UserProfileGeoLocalizationSettings.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this UserProfileGeoLocalizationSettings.


        :param service: The service of this UserProfileGeoLocalizationSettings.  # noqa: E501
        :type: str
        """

        self._service = service

    @property
    def app_id(self):
        """Gets the app_id of this UserProfileGeoLocalizationSettings.  # noqa: E501


        :return: The app_id of this UserProfileGeoLocalizationSettings.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this UserProfileGeoLocalizationSettings.


        :param app_id: The app_id of this UserProfileGeoLocalizationSettings.  # noqa: E501
        :type: str
        """

        self._app_id = app_id

    @property
    def api_key(self):
        """Gets the api_key of this UserProfileGeoLocalizationSettings.  # noqa: E501


        :return: The api_key of this UserProfileGeoLocalizationSettings.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this UserProfileGeoLocalizationSettings.


        :param api_key: The api_key of this UserProfileGeoLocalizationSettings.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def login(self):
        """Gets the login of this UserProfileGeoLocalizationSettings.  # noqa: E501


        :return: The login of this UserProfileGeoLocalizationSettings.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this UserProfileGeoLocalizationSettings.


        :param login: The login of this UserProfileGeoLocalizationSettings.  # noqa: E501
        :type: str
        """

        self._login = login

    @property
    def password(self):
        """Gets the password of this UserProfileGeoLocalizationSettings.  # noqa: E501


        :return: The password of this UserProfileGeoLocalizationSettings.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserProfileGeoLocalizationSettings.


        :param password: The password of this UserProfileGeoLocalizationSettings.  # noqa: E501
        :type: str
        """

        self._password = password

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UserProfileGeoLocalizationSettings, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserProfileGeoLocalizationSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
