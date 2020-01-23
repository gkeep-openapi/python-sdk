# swagger_client.V2Api

All URIs are relative to *https://staging-transport.smart-gamma.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alert_list**](V2Api.md#get_alert_list) | **GET** /api/v2/alerts | 
[**get_alerts_status**](V2Api.md#get_alerts_status) | **GET** /api/v2/alerts/status | 
[**get_fleet_status**](V2Api.md#get_fleet_status) | **GET** /api/v2/fleet/status | 
[**get_user_profile**](V2Api.md#get_user_profile) | **GET** /api/v2/user-profiles | 
[**get_vehicle_status**](V2Api.md#get_vehicle_status) | **GET** /api/v2/vehicles/{vehicleId}/status | 
[**get_vehicles**](V2Api.md#get_vehicles) | **GET** /api/v2/vehicles | 
[**get_vehicles_daily_stats**](V2Api.md#get_vehicles_daily_stats) | **GET** /api/v2/vehicles/{vehicleId}/daily-statistics | 

# **get_alert_list**
> AlertList get_alert_list(filter_created_date_start=filter_created_date_start, filter_created_date_end=filter_created_date_end, filter_code_special=filter_code_special)



Get alerts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V2Api(swagger_client.ApiClient(configuration))
filter_created_date_start = 'filter_created_date_start_example' # str | Start date of query selection (optional)
filter_created_date_end = 'filter_created_date_end_example' # str | End date of query selection (optional)
filter_code_special = 56 # int | Alert code id:  * `2` - fuel_is_missing  * `3` - no_alimentation  * `4` - keeper_not_connected  * `8` - safety_battery_level_under_30  * `9` - fuel_level_rise  (optional)

try:
    api_response = api_instance.get_alert_list(filter_created_date_start=filter_created_date_start, filter_created_date_end=filter_created_date_end, filter_code_special=filter_code_special)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_alert_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_created_date_start** | **str**| Start date of query selection | [optional] 
 **filter_created_date_end** | **str**| End date of query selection | [optional] 
 **filter_code_special** | **int**| Alert code id:  * &#x60;2&#x60; - fuel_is_missing  * &#x60;3&#x60; - no_alimentation  * &#x60;4&#x60; - keeper_not_connected  * &#x60;8&#x60; - safety_battery_level_under_30  * &#x60;9&#x60; - fuel_level_rise  | [optional] 

### Return type

[**AlertList**](AlertList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts_status**
> AlertsStatus get_alerts_status()



Get alerts status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V2Api(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_alerts_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_alerts_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AlertsStatus**](AlertsStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fleet_status**
> FleetStatus get_fleet_status()



Get fleet status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V2Api(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_fleet_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_fleet_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FleetStatus**](FleetStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_profile**
> UserProfile get_user_profile()



Get user-profiles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V2Api(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_user_profile()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_user_profile: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserProfile**](UserProfile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_status**
> VehicleStatus get_vehicle_status(vehicle_id)



Get vehicle status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V2Api(swagger_client.ApiClient(configuration))
vehicle_id = 56 # int | vehicle identifier

try:
    api_response = api_instance.get_vehicle_status(vehicle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_vehicle_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| vehicle identifier | 

### Return type

[**VehicleStatus**](VehicleStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicles**
> VehicleList get_vehicles()



Get vehicles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V2Api(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_vehicles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_vehicles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VehicleList**](VehicleList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicles_daily_stats**
> VehicleDailyStats get_vehicles_daily_stats(vehicle_id)



Get vehicles daily

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V2Api(swagger_client.ApiClient(configuration))
vehicle_id = 56 # int | vehicle identifier

try:
    api_response = api_instance.get_vehicles_daily_stats(vehicle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_vehicles_daily_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| vehicle identifier | 

### Return type

[**VehicleDailyStats**](VehicleDailyStats.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

