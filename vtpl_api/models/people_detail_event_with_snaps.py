# coding: utf-8

"""
    Engine api

    Engine APIs  # noqa: E501

    The version of the OpenAPI document: 1.0.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PeopleDetailEventWithSnaps(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'event_details': 'EventDetails',
        'event_snaps': 'list[Snap]',
        'meta_people_detail_event': 'MetaPeopleDetailEvent',
        'updated': 'datetime',
        'created': 'datetime',
        'etag': 'str',
        'links': 'Links'
    }

    attribute_map = {
        'id': '_id',
        'event_details': 'eventDetails',
        'event_snaps': 'eventSnaps',
        'meta_people_detail_event': 'metaPeopleDetailEvent',
        'updated': 'updated',
        'created': 'created',
        'etag': 'etag',
        'links': 'links'
    }

    def __init__(self, id=None, event_details=None, event_snaps=None, meta_people_detail_event=None, updated=None, created=None, etag=None, links=None):  # noqa: E501
        """PeopleDetailEventWithSnaps - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._event_details = None
        self._event_snaps = None
        self._meta_people_detail_event = None
        self._updated = None
        self._created = None
        self._etag = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if event_details is not None:
            self.event_details = event_details
        if event_snaps is not None:
            self.event_snaps = event_snaps
        if meta_people_detail_event is not None:
            self.meta_people_detail_event = meta_people_detail_event
        if updated is not None:
            self.updated = updated
        if created is not None:
            self.created = created
        if etag is not None:
            self.etag = etag
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this PeopleDetailEventWithSnaps.  # noqa: E501


        :return: The id of this PeopleDetailEventWithSnaps.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PeopleDetailEventWithSnaps.


        :param id: The id of this PeopleDetailEventWithSnaps.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def event_details(self):
        """Gets the event_details of this PeopleDetailEventWithSnaps.  # noqa: E501


        :return: The event_details of this PeopleDetailEventWithSnaps.  # noqa: E501
        :rtype: EventDetails
        """
        return self._event_details

    @event_details.setter
    def event_details(self, event_details):
        """Sets the event_details of this PeopleDetailEventWithSnaps.


        :param event_details: The event_details of this PeopleDetailEventWithSnaps.  # noqa: E501
        :type: EventDetails
        """

        self._event_details = event_details

    @property
    def event_snaps(self):
        """Gets the event_snaps of this PeopleDetailEventWithSnaps.  # noqa: E501


        :return: The event_snaps of this PeopleDetailEventWithSnaps.  # noqa: E501
        :rtype: list[Snap]
        """
        return self._event_snaps

    @event_snaps.setter
    def event_snaps(self, event_snaps):
        """Sets the event_snaps of this PeopleDetailEventWithSnaps.


        :param event_snaps: The event_snaps of this PeopleDetailEventWithSnaps.  # noqa: E501
        :type: list[Snap]
        """

        self._event_snaps = event_snaps

    @property
    def meta_people_detail_event(self):
        """Gets the meta_people_detail_event of this PeopleDetailEventWithSnaps.  # noqa: E501


        :return: The meta_people_detail_event of this PeopleDetailEventWithSnaps.  # noqa: E501
        :rtype: MetaPeopleDetailEvent
        """
        return self._meta_people_detail_event

    @meta_people_detail_event.setter
    def meta_people_detail_event(self, meta_people_detail_event):
        """Sets the meta_people_detail_event of this PeopleDetailEventWithSnaps.


        :param meta_people_detail_event: The meta_people_detail_event of this PeopleDetailEventWithSnaps.  # noqa: E501
        :type: MetaPeopleDetailEvent
        """

        self._meta_people_detail_event = meta_people_detail_event

    @property
    def updated(self):
        """Gets the updated of this PeopleDetailEventWithSnaps.  # noqa: E501


        :return: The updated of this PeopleDetailEventWithSnaps.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this PeopleDetailEventWithSnaps.


        :param updated: The updated of this PeopleDetailEventWithSnaps.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def created(self):
        """Gets the created of this PeopleDetailEventWithSnaps.  # noqa: E501


        :return: The created of this PeopleDetailEventWithSnaps.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PeopleDetailEventWithSnaps.


        :param created: The created of this PeopleDetailEventWithSnaps.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def etag(self):
        """Gets the etag of this PeopleDetailEventWithSnaps.  # noqa: E501


        :return: The etag of this PeopleDetailEventWithSnaps.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this PeopleDetailEventWithSnaps.


        :param etag: The etag of this PeopleDetailEventWithSnaps.  # noqa: E501
        :type: str
        """

        self._etag = etag

    @property
    def links(self):
        """Gets the links of this PeopleDetailEventWithSnaps.  # noqa: E501


        :return: The links of this PeopleDetailEventWithSnaps.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PeopleDetailEventWithSnaps.


        :param links: The links of this PeopleDetailEventWithSnaps.  # noqa: E501
        :type: Links
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, PeopleDetailEventWithSnaps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other