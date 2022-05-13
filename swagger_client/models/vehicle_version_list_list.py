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


class VehicleVersionListList(object):
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
        'name': 'str',
        'brand': 'VehicleBrandListInner',
        'model': 'VehicleModelListList',
        'started_at': 'int',
        'ended_at': 'str',
        'tonnage': 'int',
        'power': 'int',
        'power_cv': 'int',
        'axes': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'brand': 'brand',
        'model': 'model',
        'started_at': 'started_at',
        'ended_at': 'ended_at',
        'tonnage': 'tonnage',
        'power': 'power',
        'power_cv': 'power_cv',
        'axes': 'axes'
    }

    def __init__(self, id=None, name=None, brand=None, model=None, started_at=None, ended_at=None, tonnage=None, power=None, power_cv=None, axes=None):  # noqa: E501
        """VehicleVersionListList - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._brand = None
        self._model = None
        self._started_at = None
        self._ended_at = None
        self._tonnage = None
        self._power = None
        self._power_cv = None
        self._axes = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if brand is not None:
            self.brand = brand
        if model is not None:
            self.model = model
        if started_at is not None:
            self.started_at = started_at
        if ended_at is not None:
            self.ended_at = ended_at
        if tonnage is not None:
            self.tonnage = tonnage
        if power is not None:
            self.power = power
        if power_cv is not None:
            self.power_cv = power_cv
        if axes is not None:
            self.axes = axes

    @property
    def id(self):
        """Gets the id of this VehicleVersionListList.  # noqa: E501


        :return: The id of this VehicleVersionListList.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VehicleVersionListList.


        :param id: The id of this VehicleVersionListList.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this VehicleVersionListList.  # noqa: E501


        :return: The name of this VehicleVersionListList.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VehicleVersionListList.


        :param name: The name of this VehicleVersionListList.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def brand(self):
        """Gets the brand of this VehicleVersionListList.  # noqa: E501


        :return: The brand of this VehicleVersionListList.  # noqa: E501
        :rtype: VehicleBrandListInner
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this VehicleVersionListList.


        :param brand: The brand of this VehicleVersionListList.  # noqa: E501
        :type: VehicleBrandListInner
        """

        self._brand = brand

    @property
    def model(self):
        """Gets the model of this VehicleVersionListList.  # noqa: E501


        :return: The model of this VehicleVersionListList.  # noqa: E501
        :rtype: VehicleModelListList
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this VehicleVersionListList.


        :param model: The model of this VehicleVersionListList.  # noqa: E501
        :type: VehicleModelListList
        """

        self._model = model

    @property
    def started_at(self):
        """Gets the started_at of this VehicleVersionListList.  # noqa: E501


        :return: The started_at of this VehicleVersionListList.  # noqa: E501
        :rtype: int
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this VehicleVersionListList.


        :param started_at: The started_at of this VehicleVersionListList.  # noqa: E501
        :type: int
        """

        self._started_at = started_at

    @property
    def ended_at(self):
        """Gets the ended_at of this VehicleVersionListList.  # noqa: E501


        :return: The ended_at of this VehicleVersionListList.  # noqa: E501
        :rtype: str
        """
        return self._ended_at

    @ended_at.setter
    def ended_at(self, ended_at):
        """Sets the ended_at of this VehicleVersionListList.


        :param ended_at: The ended_at of this VehicleVersionListList.  # noqa: E501
        :type: str
        """

        self._ended_at = ended_at

    @property
    def tonnage(self):
        """Gets the tonnage of this VehicleVersionListList.  # noqa: E501


        :return: The tonnage of this VehicleVersionListList.  # noqa: E501
        :rtype: int
        """
        return self._tonnage

    @tonnage.setter
    def tonnage(self, tonnage):
        """Sets the tonnage of this VehicleVersionListList.


        :param tonnage: The tonnage of this VehicleVersionListList.  # noqa: E501
        :type: int
        """

        self._tonnage = tonnage

    @property
    def power(self):
        """Gets the power of this VehicleVersionListList.  # noqa: E501


        :return: The power of this VehicleVersionListList.  # noqa: E501
        :rtype: int
        """
        return self._power

    @power.setter
    def power(self, power):
        """Sets the power of this VehicleVersionListList.


        :param power: The power of this VehicleVersionListList.  # noqa: E501
        :type: int
        """

        self._power = power

    @property
    def power_cv(self):
        """Gets the power_cv of this VehicleVersionListList.  # noqa: E501


        :return: The power_cv of this VehicleVersionListList.  # noqa: E501
        :rtype: int
        """
        return self._power_cv

    @power_cv.setter
    def power_cv(self, power_cv):
        """Sets the power_cv of this VehicleVersionListList.


        :param power_cv: The power_cv of this VehicleVersionListList.  # noqa: E501
        :type: int
        """

        self._power_cv = power_cv

    @property
    def axes(self):
        """Gets the axes of this VehicleVersionListList.  # noqa: E501


        :return: The axes of this VehicleVersionListList.  # noqa: E501
        :rtype: str
        """
        return self._axes

    @axes.setter
    def axes(self, axes):
        """Sets the axes of this VehicleVersionListList.


        :param axes: The axes of this VehicleVersionListList.  # noqa: E501
        :type: str
        """

        self._axes = axes

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
        if issubclass(VehicleVersionListList, dict):
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
        if not isinstance(other, VehicleVersionListList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
