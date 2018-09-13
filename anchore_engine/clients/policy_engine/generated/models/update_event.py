# coding: utf-8

"""
    anchore_engine.services.policy_engine

    This is a policy evaluation service. It receives push-events from external systems for data updates and provides an api for requesting image policy checks  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: zach@anchore.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UpdateEvent(object):
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
        'event_type': 'str',
        'event_content': 'object'
    }

    attribute_map = {
        'event_type': 'event_type',
        'event_content': 'event_content'
    }

    def __init__(self, event_type=None, event_content=None):  # noqa: E501
        """UpdateEvent - a model defined in Swagger"""  # noqa: E501

        self._event_type = None
        self._event_content = None
        self.discriminator = None

        if event_type is not None:
            self.event_type = event_type
        if event_content is not None:
            self.event_content = event_content

    @property
    def event_type(self):
        """Gets the event_type of this UpdateEvent.  # noqa: E501

        Type identifier for the event content section for parsing  # noqa: E501

        :return: The event_type of this UpdateEvent.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this UpdateEvent.

        Type identifier for the event content section for parsing  # noqa: E501

        :param event_type: The event_type of this UpdateEvent.  # noqa: E501
        :type: str
        """

        self._event_type = event_type

    @property
    def event_content(self):
        """Gets the event_content of this UpdateEvent.  # noqa: E501


        :return: The event_content of this UpdateEvent.  # noqa: E501
        :rtype: object
        """
        return self._event_content

    @event_content.setter
    def event_content(self, event_content):
        """Sets the event_content of this UpdateEvent.


        :param event_content: The event_content of this UpdateEvent.  # noqa: E501
        :type: object
        """

        self._event_content = event_content

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
