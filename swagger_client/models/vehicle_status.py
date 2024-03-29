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


class VehicleStatus(object):
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
        'fuel_level': 'float',
        'smoothed_fuel_level': 'float',
        'fuel_level_on_raise_start': 'float',
        'created_at': 'int',
        'is_vehicle_stop': 'bool',
        'is_engine_stop': 'bool',
        'battery_level': 'int',
        'longitude': 'int',
        'latitude': 'int',
        'vehicle': 'VehicleStatusVehicle',
        'tanks': 'list[VehicleStatusTanks]'
    }

    attribute_map = {
        'fuel_level': 'fuel_level',
        'smoothed_fuel_level': 'smoothed_fuel_level',
        'fuel_level_on_raise_start': 'fuel_level_on_raise_start',
        'created_at': 'created_at',
        'is_vehicle_stop': 'is_vehicle_stop',
        'is_engine_stop': 'is_engine_stop',
        'battery_level': 'battery_level',
        'longitude': 'longitude',
        'latitude': 'latitude',
        'vehicle': 'vehicle',
        'tanks': 'tanks'
    }

    def __init__(self, fuel_level=None, smoothed_fuel_level=None, fuel_level_on_raise_start=None, created_at=None, is_vehicle_stop=None, is_engine_stop=None, battery_level=None, longitude=None, latitude=None, vehicle=None, tanks=None):  # noqa: E501
        """VehicleStatus - a model defined in Swagger"""  # noqa: E501
        self._fuel_level = None
        self._smoothed_fuel_level = None
        self._fuel_level_on_raise_start = None
        self._created_at = None
        self._is_vehicle_stop = None
        self._is_engine_stop = None
        self._battery_level = None
        self._longitude = None
        self._latitude = None
        self._vehicle = None
        self._tanks = None
        self.discriminator = None
        if fuel_level is not None:
            self.fuel_level = fuel_level
        if smoothed_fuel_level is not None:
            self.smoothed_fuel_level = smoothed_fuel_level
        if fuel_level_on_raise_start is not None:
            self.fuel_level_on_raise_start = fuel_level_on_raise_start
        if created_at is not None:
            self.created_at = created_at
        if is_vehicle_stop is not None:
            self.is_vehicle_stop = is_vehicle_stop
        if is_engine_stop is not None:
            self.is_engine_stop = is_engine_stop
        if battery_level is not None:
            self.battery_level = battery_level
        if longitude is not None:
            self.longitude = longitude
        if latitude is not None:
            self.latitude = latitude
        if vehicle is not None:
            self.vehicle = vehicle
        if tanks is not None:
            self.tanks = tanks

    @property
    def fuel_level(self):
        """Gets the fuel_level of this VehicleStatus.  # noqa: E501


        :return: The fuel_level of this VehicleStatus.  # noqa: E501
        :rtype: float
        """
        return self._fuel_level

    @fuel_level.setter
    def fuel_level(self, fuel_level):
        """Sets the fuel_level of this VehicleStatus.


        :param fuel_level: The fuel_level of this VehicleStatus.  # noqa: E501
        :type: float
        """

        self._fuel_level = fuel_level

    @property
    def smoothed_fuel_level(self):
        """Gets the smoothed_fuel_level of this VehicleStatus.  # noqa: E501


        :return: The smoothed_fuel_level of this VehicleStatus.  # noqa: E501
        :rtype: float
        """
        return self._smoothed_fuel_level

    @smoothed_fuel_level.setter
    def smoothed_fuel_level(self, smoothed_fuel_level):
        """Sets the smoothed_fuel_level of this VehicleStatus.


        :param smoothed_fuel_level: The smoothed_fuel_level of this VehicleStatus.  # noqa: E501
        :type: float
        """

        self._smoothed_fuel_level = smoothed_fuel_level

    @property
    def fuel_level_on_raise_start(self):
        """Gets the fuel_level_on_raise_start of this VehicleStatus.  # noqa: E501


        :return: The fuel_level_on_raise_start of this VehicleStatus.  # noqa: E501
        :rtype: float
        """
        return self._fuel_level_on_raise_start

    @fuel_level_on_raise_start.setter
    def fuel_level_on_raise_start(self, fuel_level_on_raise_start):
        """Sets the fuel_level_on_raise_start of this VehicleStatus.


        :param fuel_level_on_raise_start: The fuel_level_on_raise_start of this VehicleStatus.  # noqa: E501
        :type: float
        """

        self._fuel_level_on_raise_start = fuel_level_on_raise_start

    @property
    def created_at(self):
        """Gets the created_at of this VehicleStatus.  # noqa: E501


        :return: The created_at of this VehicleStatus.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VehicleStatus.


        :param created_at: The created_at of this VehicleStatus.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def is_vehicle_stop(self):
        """Gets the is_vehicle_stop of this VehicleStatus.  # noqa: E501


        :return: The is_vehicle_stop of this VehicleStatus.  # noqa: E501
        :rtype: bool
        """
        return self._is_vehicle_stop

    @is_vehicle_stop.setter
    def is_vehicle_stop(self, is_vehicle_stop):
        """Sets the is_vehicle_stop of this VehicleStatus.


        :param is_vehicle_stop: The is_vehicle_stop of this VehicleStatus.  # noqa: E501
        :type: bool
        """

        self._is_vehicle_stop = is_vehicle_stop

    @property
    def is_engine_stop(self):
        """Gets the is_engine_stop of this VehicleStatus.  # noqa: E501


        :return: The is_engine_stop of this VehicleStatus.  # noqa: E501
        :rtype: bool
        """
        return self._is_engine_stop

    @is_engine_stop.setter
    def is_engine_stop(self, is_engine_stop):
        """Sets the is_engine_stop of this VehicleStatus.


        :param is_engine_stop: The is_engine_stop of this VehicleStatus.  # noqa: E501
        :type: bool
        """

        self._is_engine_stop = is_engine_stop

    @property
    def battery_level(self):
        """Gets the battery_level of this VehicleStatus.  # noqa: E501


        :return: The battery_level of this VehicleStatus.  # noqa: E501
        :rtype: int
        """
        return self._battery_level

    @battery_level.setter
    def battery_level(self, battery_level):
        """Sets the battery_level of this VehicleStatus.


        :param battery_level: The battery_level of this VehicleStatus.  # noqa: E501
        :type: int
        """

        self._battery_level = battery_level

    @property
    def longitude(self):
        """Gets the longitude of this VehicleStatus.  # noqa: E501


        :return: The longitude of this VehicleStatus.  # noqa: E501
        :rtype: int
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this VehicleStatus.


        :param longitude: The longitude of this VehicleStatus.  # noqa: E501
        :type: int
        """

        self._longitude = longitude

    @property
    def latitude(self):
        """Gets the latitude of this VehicleStatus.  # noqa: E501


        :return: The latitude of this VehicleStatus.  # noqa: E501
        :rtype: int
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this VehicleStatus.


        :param latitude: The latitude of this VehicleStatus.  # noqa: E501
        :type: int
        """

        self._latitude = latitude

    @property
    def vehicle(self):
        """Gets the vehicle of this VehicleStatus.  # noqa: E501


        :return: The vehicle of this VehicleStatus.  # noqa: E501
        :rtype: VehicleStatusVehicle
        """
        return self._vehicle

    @vehicle.setter
    def vehicle(self, vehicle):
        """Sets the vehicle of this VehicleStatus.


        :param vehicle: The vehicle of this VehicleStatus.  # noqa: E501
        :type: VehicleStatusVehicle
        """

        self._vehicle = vehicle

    @property
    def tanks(self):
        """Gets the tanks of this VehicleStatus.  # noqa: E501


        :return: The tanks of this VehicleStatus.  # noqa: E501
        :rtype: list[VehicleStatusTanks]
        """
        return self._tanks

    @tanks.setter
    def tanks(self, tanks):
        """Sets the tanks of this VehicleStatus.


        :param tanks: The tanks of this VehicleStatus.  # noqa: E501
        :type: list[VehicleStatusTanks]
        """

        self._tanks = tanks

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
        if issubclass(VehicleStatus, dict):
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
        if not isinstance(other, VehicleStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
