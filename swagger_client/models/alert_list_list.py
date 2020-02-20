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


class AlertListList(object):
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
        'fuel_level_on_raise_start': 'float',
        'action_status': 'int',
        'id': 'int',
        'nav_system_object_uid': 'str',
        'created_at': 'int',
        'is_closed': 'bool',
        'description': 'str',
        'vehicle': 'AlertListVehicle',
        'code': 'AlertListCode',
        'driver': 'AlertListDriver',
        'level': 'AlertListLevel',
        'status': 'int',
        'is_maintenance_enabled': 'bool'
    }

    attribute_map = {
        'fuel_level': 'fuel_level',
        'fuel_level_on_raise_start': 'fuel_level_on_raise_start',
        'action_status': 'action_status',
        'id': 'id',
        'nav_system_object_uid': 'nav_system_object_uid',
        'created_at': 'created_at',
        'is_closed': 'is_closed',
        'description': 'description',
        'vehicle': 'vehicle',
        'code': 'code',
        'driver': 'driver',
        'level': 'level',
        'status': 'status',
        'is_maintenance_enabled': 'is_maintenance_enabled'
    }

    def __init__(self, fuel_level=None, fuel_level_on_raise_start=None, action_status=None, id=None, nav_system_object_uid=None, created_at=None, is_closed=None, description=None, vehicle=None, code=None, driver=None, level=None, status=None, is_maintenance_enabled=None):  # noqa: E501
        """AlertListList - a model defined in Swagger"""  # noqa: E501
        self._fuel_level = None
        self._fuel_level_on_raise_start = None
        self._action_status = None
        self._id = None
        self._nav_system_object_uid = None
        self._created_at = None
        self._is_closed = None
        self._description = None
        self._vehicle = None
        self._code = None
        self._driver = None
        self._level = None
        self._status = None
        self._is_maintenance_enabled = None
        self.discriminator = None
        if fuel_level is not None:
            self.fuel_level = fuel_level
        if fuel_level_on_raise_start is not None:
            self.fuel_level_on_raise_start = fuel_level_on_raise_start
        if action_status is not None:
            self.action_status = action_status
        if id is not None:
            self.id = id
        if nav_system_object_uid is not None:
            self.nav_system_object_uid = nav_system_object_uid
        if created_at is not None:
            self.created_at = created_at
        if is_closed is not None:
            self.is_closed = is_closed
        if description is not None:
            self.description = description
        if vehicle is not None:
            self.vehicle = vehicle
        if code is not None:
            self.code = code
        if driver is not None:
            self.driver = driver
        if level is not None:
            self.level = level
        if status is not None:
            self.status = status
        if is_maintenance_enabled is not None:
            self.is_maintenance_enabled = is_maintenance_enabled

    @property
    def fuel_level(self):
        """Gets the fuel_level of this AlertListList.  # noqa: E501


        :return: The fuel_level of this AlertListList.  # noqa: E501
        :rtype: float
        """
        return self._fuel_level

    @fuel_level.setter
    def fuel_level(self, fuel_level):
        """Sets the fuel_level of this AlertListList.


        :param fuel_level: The fuel_level of this AlertListList.  # noqa: E501
        :type: float
        """

        self._fuel_level = fuel_level

    @property
    def fuel_level_on_raise_start(self):
        """Gets the fuel_level_on_raise_start of this AlertListList.  # noqa: E501


        :return: The fuel_level_on_raise_start of this AlertListList.  # noqa: E501
        :rtype: float
        """
        return self._fuel_level_on_raise_start

    @fuel_level_on_raise_start.setter
    def fuel_level_on_raise_start(self, fuel_level_on_raise_start):
        """Sets the fuel_level_on_raise_start of this AlertListList.


        :param fuel_level_on_raise_start: The fuel_level_on_raise_start of this AlertListList.  # noqa: E501
        :type: float
        """

        self._fuel_level_on_raise_start = fuel_level_on_raise_start

    @property
    def action_status(self):
        """Gets the action_status of this AlertListList.  # noqa: E501


        :return: The action_status of this AlertListList.  # noqa: E501
        :rtype: int
        """
        return self._action_status

    @action_status.setter
    def action_status(self, action_status):
        """Sets the action_status of this AlertListList.


        :param action_status: The action_status of this AlertListList.  # noqa: E501
        :type: int
        """

        self._action_status = action_status

    @property
    def id(self):
        """Gets the id of this AlertListList.  # noqa: E501


        :return: The id of this AlertListList.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertListList.


        :param id: The id of this AlertListList.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def nav_system_object_uid(self):
        """Gets the nav_system_object_uid of this AlertListList.  # noqa: E501


        :return: The nav_system_object_uid of this AlertListList.  # noqa: E501
        :rtype: str
        """
        return self._nav_system_object_uid

    @nav_system_object_uid.setter
    def nav_system_object_uid(self, nav_system_object_uid):
        """Sets the nav_system_object_uid of this AlertListList.


        :param nav_system_object_uid: The nav_system_object_uid of this AlertListList.  # noqa: E501
        :type: str
        """

        self._nav_system_object_uid = nav_system_object_uid

    @property
    def created_at(self):
        """Gets the created_at of this AlertListList.  # noqa: E501


        :return: The created_at of this AlertListList.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AlertListList.


        :param created_at: The created_at of this AlertListList.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def is_closed(self):
        """Gets the is_closed of this AlertListList.  # noqa: E501


        :return: The is_closed of this AlertListList.  # noqa: E501
        :rtype: bool
        """
        return self._is_closed

    @is_closed.setter
    def is_closed(self, is_closed):
        """Sets the is_closed of this AlertListList.


        :param is_closed: The is_closed of this AlertListList.  # noqa: E501
        :type: bool
        """

        self._is_closed = is_closed

    @property
    def description(self):
        """Gets the description of this AlertListList.  # noqa: E501


        :return: The description of this AlertListList.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AlertListList.


        :param description: The description of this AlertListList.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def vehicle(self):
        """Gets the vehicle of this AlertListList.  # noqa: E501


        :return: The vehicle of this AlertListList.  # noqa: E501
        :rtype: AlertListVehicle
        """
        return self._vehicle

    @vehicle.setter
    def vehicle(self, vehicle):
        """Sets the vehicle of this AlertListList.


        :param vehicle: The vehicle of this AlertListList.  # noqa: E501
        :type: AlertListVehicle
        """

        self._vehicle = vehicle

    @property
    def code(self):
        """Gets the code of this AlertListList.  # noqa: E501


        :return: The code of this AlertListList.  # noqa: E501
        :rtype: AlertListCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AlertListList.


        :param code: The code of this AlertListList.  # noqa: E501
        :type: AlertListCode
        """

        self._code = code

    @property
    def driver(self):
        """Gets the driver of this AlertListList.  # noqa: E501


        :return: The driver of this AlertListList.  # noqa: E501
        :rtype: AlertListDriver
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this AlertListList.


        :param driver: The driver of this AlertListList.  # noqa: E501
        :type: AlertListDriver
        """

        self._driver = driver

    @property
    def level(self):
        """Gets the level of this AlertListList.  # noqa: E501


        :return: The level of this AlertListList.  # noqa: E501
        :rtype: AlertListLevel
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this AlertListList.


        :param level: The level of this AlertListList.  # noqa: E501
        :type: AlertListLevel
        """

        self._level = level

    @property
    def status(self):
        """Gets the status of this AlertListList.  # noqa: E501


        :return: The status of this AlertListList.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AlertListList.


        :param status: The status of this AlertListList.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def is_maintenance_enabled(self):
        """Gets the is_maintenance_enabled of this AlertListList.  # noqa: E501


        :return: The is_maintenance_enabled of this AlertListList.  # noqa: E501
        :rtype: bool
        """
        return self._is_maintenance_enabled

    @is_maintenance_enabled.setter
    def is_maintenance_enabled(self, is_maintenance_enabled):
        """Sets the is_maintenance_enabled of this AlertListList.


        :param is_maintenance_enabled: The is_maintenance_enabled of this AlertListList.  # noqa: E501
        :type: bool
        """

        self._is_maintenance_enabled = is_maintenance_enabled

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
        if issubclass(AlertListList, dict):
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
        if not isinstance(other, AlertListList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
