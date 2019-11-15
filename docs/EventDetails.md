# EventDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | _id of camera #$ref: &#39;#/components/schemas/camera&#39; from project cameras | [optional] 
**engine_task_id** | **str** | _id of engineTasks #$ref: &#39;#/components/schemas/engineTasks&#39; | [optional] 
**zone_id** | **int** | the zoneId of the engineTask in zoneSetting, #$ref: &#39;#/components/schemas/zone&#39; | [optional] [default to 0]
**confidence** | **float** | match confidence predicted by engine during event detection | [optional] [default to 0]
**start_time_stamp** | **int** | Event start timestamp in Unix epoch milliseconds | [optional] 
**end_time_stamp** | **int** | Event end timestamp in Unix epoch milliseconds | [optional] 
**extras** | [**list[Extra]**](Extra.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


