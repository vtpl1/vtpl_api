# EngineTask

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**capbilities_type** | [**Capability**](Capability.md) |  | [optional] 
**event_type** | [**EventType**](EventType.md) |  | [optional] 
**engine_machine_id** | **str** |  | [optional] 
**is_expired** | **bool** | Explanations: * true &#x3D; Engines will NEVER execute this task * false &#x3D; Engines will execute this task | [optional] [default to False]
**time_to_live** | **int** | Time in milliseconds of expiry or the task. Engines will not execute an expired task. Explanations: * -1 &#x3D; Never expires * -2 &#x3D; Expired *  0 &#x3D; Will expire in 0 milliseconds * &gt;0 &#x3D; milliseconds till expiry | [optional] [default to -1]
**source** | [**SourceEndPoint**](SourceEndPoint.md) |  | [optional] 
**destination** | [**DestinationEndPoint**](DestinationEndPoint.md) |  | [optional] 
**zone_setting** | [**EngineTaskZoneSetting**](EngineTaskZoneSetting.md) |  | [optional] 
**line_setting** | [**EngineTaskLineSetting**](EngineTaskLineSetting.md) |  | [optional] 
**config** | [**list[Config]**](Config.md) |  | [optional] 
**updated** | **datetime** |  | [optional] 
**created** | **datetime** |  | [optional] 
**etag** | **str** |  | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


