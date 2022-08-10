# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Configuration(Model):
    """The configuration for Iot Hub device and module twins.

    :param id: The unique identifier of the configuration.
    :type id: str
    :param schema_version: The schema version of the configuration.
    :type schema_version: str
    :param labels: The key-value pairs used to describe the configuration.
    :type labels: dict[str, str]
    :param content: The content of the configuration.
    :type content: ~protocol.models.ConfigurationContent
    :param target_condition: The query used to define the targeted devices or
     modules. The query is based on twin tags and/or reported properties.
    :type target_condition: str
    :param created_time_utc: The creation date and time of the configuration.
    :type created_time_utc: datetime
    :param last_updated_time_utc: The update date and time of the
     configuration.
    :type last_updated_time_utc: datetime
    :param priority: The priority number assigned to the configuration.
    :type priority: int
    :param system_metrics: The system metrics computed by the IoT Hub that
     cannot be customized.
    :type system_metrics: ~protocol.models.ConfigurationMetrics
    :param metrics: The custom metrics specified by the developer as queries
     against twin reported properties.
    :type metrics: ~protocol.models.ConfigurationMetrics
    :param etag: The ETag of the configuration.
    :type etag: str
    """

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "schema_version": {"key": "schemaVersion", "type": "str"},
        "labels": {"key": "labels", "type": "{str}"},
        "content": {"key": "content", "type": "ConfigurationContent"},
        "target_condition": {"key": "targetCondition", "type": "str"},
        "created_time_utc": {"key": "createdTimeUtc", "type": "iso-8601"},
        "last_updated_time_utc": {"key": "lastUpdatedTimeUtc", "type": "iso-8601"},
        "priority": {"key": "priority", "type": "int"},
        "system_metrics": {"key": "systemMetrics", "type": "ConfigurationMetrics"},
        "metrics": {"key": "metrics", "type": "ConfigurationMetrics"},
        "etag": {"key": "etag", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(Configuration, self).__init__(**kwargs)
        self.id = kwargs.get("id", None)
        self.schema_version = kwargs.get("schema_version", None)
        self.labels = kwargs.get("labels", None)
        self.content = kwargs.get("content", None)
        self.target_condition = kwargs.get("target_condition", None)
        self.created_time_utc = kwargs.get("created_time_utc", None)
        self.last_updated_time_utc = kwargs.get("last_updated_time_utc", None)
        self.priority = kwargs.get("priority", None)
        self.system_metrics = kwargs.get("system_metrics", None)
        self.metrics = kwargs.get("metrics", None)
        self.etag = kwargs.get("etag", None)