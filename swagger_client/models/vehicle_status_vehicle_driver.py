# coding: utf-8

"""
    Gkeep API

    Gkeep API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class VehicleStatusVehicleDriver(object):
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
        'firstname': 'str',
        'lastname': 'str',
        'id': 'int'
    }

    attribute_map = {
        'firstname': 'firstname',
        'lastname': 'lastname',
        'id': 'id'
    }

    def __init__(self, firstname=None, lastname=None, id=None):  # noqa: E501
        """VehicleStatusVehicleDriver - a model defined in Swagger"""  # noqa: E501
        self._firstname = None
        self._lastname = None
        self._id = None
        self.discriminator = None
        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname
        if id is not None:
            self.id = id

    @property
    def firstname(self):
        """Gets the firstname of this VehicleStatusVehicleDriver.  # noqa: E501


        :return: The firstname of this VehicleStatusVehicleDriver.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this VehicleStatusVehicleDriver.


        :param firstname: The firstname of this VehicleStatusVehicleDriver.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this VehicleStatusVehicleDriver.  # noqa: E501


        :return: The lastname of this VehicleStatusVehicleDriver.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this VehicleStatusVehicleDriver.


        :param lastname: The lastname of this VehicleStatusVehicleDriver.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def id(self):
        """Gets the id of this VehicleStatusVehicleDriver.  # noqa: E501


        :return: The id of this VehicleStatusVehicleDriver.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VehicleStatusVehicleDriver.


        :param id: The id of this VehicleStatusVehicleDriver.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(VehicleStatusVehicleDriver, dict):
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
        if not isinstance(other, VehicleStatusVehicleDriver):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
