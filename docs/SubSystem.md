# SubSystem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**sub_system_id** | **str** | unique id of the system in the central system database | [optional] 
**capabilities** | [**list[Capability]**](Capability.md) |  | [optional] 
**is_syncing** | **bool** | If data sync process is ongoing from central to sub system | [optional] [default to False]
**last_synced** | **int** | Epoch timestamp when the sub system was last synced with central system | [optional] 
**updated** | **datetime** |  | [optional] 
**created** | **datetime** |  | [optional] 
**etag** | **str** |  | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


