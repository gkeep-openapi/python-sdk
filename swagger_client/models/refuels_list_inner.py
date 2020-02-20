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


class RefuelsListInner(object):
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
        'latitude': 'str',
        'longitude': 'str',
        'created_at': 'int',
        'fuel_cost': 'int',
        'fuel_level_on_raise_start': 'float',
        'fuel_level': 'float',
        'filled_fuel_volume': 'float',
        'capacity': 'float',
        'distance': 'int'
    }

    attribute_map = {
        'latitude': 'latitude',
        'longitude': 'longitude',
        'created_at': 'created_at',
        'fuel_cost': 'fuel_cost',
        'fuel_level_on_raise_start': 'fuel_level_on_raise_start',
        'fuel_level': 'fuel_level',
        'filled_fuel_volume': 'filled_fuel_volume',
        'capacity': 'capacity',
        'distance': 'distance'
    }

    def __init__(self, latitude=None, longitude=None, created_at=None, fuel_cost=None, fuel_level_on_raise_start=None, fuel_level=None, filled_fuel_volume=None, capacity=None, distance=None):  # noqa: E501
        """RefuelsListInner - a model defined in Swagger"""  # noqa: E501
        self._latitude = None
        self._longitude = None
        self._created_at = None
        self._fuel_cost = None
        self._fuel_level_on_raise_start = None
        self._fuel_level = None
        self._filled_fuel_volume = None
        self._capacity = None
        self._distance = None
        self.discriminator = None
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if created_at is not None:
            self.created_at = created_at
        if fuel_cost is not None:
            self.fuel_cost = fuel_cost
        if fuel_level_on_raise_start is not None:
            self.fuel_level_on_raise_start = fuel_level_on_raise_start
        if fuel_level is not None:
            self.fuel_level = fuel_level
        if filled_fuel_volume is not None:
            self.filled_fuel_volume = filled_fuel_volume
        if capacity is not None:
            self.capacity = capacity
        if distance is not None:
            self.distance = distance

    @property
    def latitude(self):
        """Gets the latitude of this RefuelsListInner.  # noqa: E501


        :return: The latitude of this RefuelsListInner.  # noqa: E501
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this RefuelsListInner.


        :param latitude: The latitude of this RefuelsListInner.  # noqa: E501
        :type: str
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this RefuelsListInner.  # noqa: E501


        :return: The longitude of this RefuelsListInner.  # noqa: E501
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this RefuelsListInner.


        :param longitude: The longitude of this RefuelsListInner.  # noqa: E501
        :type: str
        """

        self._longitude = longitude

    @property
    def created_at(self):
        """Gets the created_at of this RefuelsListInner.  # noqa: E501


        :return: The created_at of this RefuelsListInner.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RefuelsListInner.


        :param created_at: The created_at of this RefuelsListInner.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def fuel_cost(self):
        """Gets the fuel_cost of this RefuelsListInner.  # noqa: E501


        :return: The fuel_cost of this RefuelsListInner.  # noqa: E501
        :rtype: int
        """
        return self._fuel_cost

    @fuel_cost.setter
    def fuel_cost(self, fuel_cost):
        """Sets the fuel_cost of this RefuelsListInner.


        :param fuel_cost: The fuel_cost of this RefuelsListInner.  # noqa: E501
        :type: int
        """

        self._fuel_cost = fuel_cost

    @property
    def fuel_level_on_raise_start(self):
        """Gets the fuel_level_on_raise_start of this RefuelsListInner.  # noqa: E501


        :return: The fuel_level_on_raise_start of this RefuelsListInner.  # noqa: E501
        :rtype: float
        """
        return self._fuel_level_on_raise_start

    @fuel_level_on_raise_start.setter
    def fuel_level_on_raise_start(self, fuel_level_on_raise_start):
        """Sets the fuel_level_on_raise_start of this RefuelsListInner.


        :param fuel_level_on_raise_start: The fuel_level_on_raise_start of this RefuelsListInner.  # noqa: E501
        :type: float
        """

        self._fuel_level_on_raise_start = fuel_level_on_raise_start

    @property
    def fuel_level(self):
        """Gets the fuel_level of this RefuelsListInner.  # noqa: E501


        :return: The fuel_level of this RefuelsListInner.  # noqa: E501
        :rtype: float
        """
        return self._fuel_level

    @fuel_level.setter
    def fuel_level(self, fuel_level):
        """Sets the fuel_level of this RefuelsListInner.


        :param fuel_level: The fuel_level of this RefuelsListInner.  # noqa: E501
        :type: float
        """

        self._fuel_level = fuel_level

    @property
    def filled_fuel_volume(self):
        """Gets the filled_fuel_volume of this RefuelsListInner.  # noqa: E501


        :return: The filled_fuel_volume of this RefuelsListInner.  # noqa: E501
        :rtype: float
        """
        return self._filled_fuel_volume

    @filled_fuel_volume.setter
    def filled_fuel_volume(self, filled_fuel_volume):
        """Sets the filled_fuel_volume of this RefuelsListInner.


        :param filled_fuel_volume: The filled_fuel_volume of this RefuelsListInner.  # noqa: E501
        :type: float
        """

        self._filled_fuel_volume = filled_fuel_volume

    @property
    def capacity(self):
        """Gets the capacity of this RefuelsListInner.  # noqa: E501


        :return: The capacity of this RefuelsListInner.  # noqa: E501
        :rtype: float
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this RefuelsListInner.


        :param capacity: The capacity of this RefuelsListInner.  # noqa: E501
        :type: float
        """

        self._capacity = capacity

    @property
    def distance(self):
        """Gets the distance of this RefuelsListInner.  # noqa: E501


        :return: The distance of this RefuelsListInner.  # noqa: E501
        :rtype: int
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this RefuelsListInner.


        :param distance: The distance of this RefuelsListInner.  # noqa: E501
        :type: int
        """

        self._distance = distance

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
        if issubclass(RefuelsListInner, dict):
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
        if not isinstance(other, RefuelsListInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other