# swagger_client.V2Api

All URIs are relative to *https://staging-transport.smart-gamma.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_profile**](V2Api.md#create_user_profile) | **POST** /api/v2/user-profiles | 
[**create_vehicle_category**](V2Api.md#create_vehicle_category) | **POST** /api/v2/vehicles/categories | 
[**delete_user_profile**](V2Api.md#delete_user_profile) | **DELETE** /api/v2/user-profiles/{profileId} | 
[**delete_vehicle_category**](V2Api.md#delete_vehicle_category) | **DELETE** /api/v2/vehicles/categories/{categoryId} | 
[**enable_vehicle_maintenance**](V2Api.md#enable_vehicle_maintenance) | **PUT** /api/v2/vehicles/maintenance/{vehicleId} | 
[**get_alert_list**](V2Api.md#get_alert_list) | **GET** /api/v2/alerts | 
[**get_alerts_status**](V2Api.md#get_alerts_status) | **GET** /api/v2/alerts/status | 
[**get_current_user_profile**](V2Api.md#get_current_user_profile) | **GET** /api/v2/user-profiles | 
[**get_fleet_status**](V2Api.md#get_fleet_status) | **GET** /api/v2/fleet/status | 
[**get_notification_settings**](V2Api.md#get_notification_settings) | **GET** /api/v2/user-profiles/notification-settings | 
[**get_related_user_profiles**](V2Api.md#get_related_user_profiles) | **GET** /api/v2/user-profiles/{levelName} | 
[**get_user_profile**](V2Api.md#get_user_profile) | **GET** /api/v2/user-profiles/{profileId} | 
[**get_vehicle_category**](V2Api.md#get_vehicle_category) | **GET** /api/v2/vehicles/categories/{categoryId} | 
[**get_vehicle_category_list**](V2Api.md#get_vehicle_category_list) | **GET** /api/v2/vehicles/categories | 
[**get_vehicle_status**](V2Api.md#get_vehicle_status) | **GET** /api/v2/vehicles/{vehicleId}/status | 
[**get_vehicles**](V2Api.md#get_vehicles) | **GET** /api/v2/vehicles | 
[**get_vehicles_daily_stats**](V2Api.md#get_vehicles_daily_stats) | **GET** /api/v2/vehicles/{vehicleId}/daily-statistics | 
[**get_vehicles_frame_history**](V2Api.md#get_vehicles_frame_history) | **GET** /api/v2/vehicles/{vehicleId}/frame-history | 
[**get_vehicles_refuels**](V2Api.md#get_vehicles_refuels) | **GET** /api/v2/vehicles/{vehicleId}/refuels | 
[**get_vehicles_stopped_consumptions**](V2Api.md#get_vehicles_stopped_consumptions) | **GET** /api/v2/vehicles/{vehicleId}/stopped-consumptions | 
[**refresh_api_token**](V2Api.md#refresh_api_token) | **PUT** /api/v2/user-profiles/tokens/refresh | 
[**update_notification_settings**](V2Api.md#update_notification_settings) | **PUT** /api/v2/user-profiles/notification-settings | 
[**update_user_profile**](V2Api.md#update_user_profile) | **PUT** /api/v2/user-profiles/{profileId} | 
[**update_vehicle**](V2Api.md#update_vehicle) | **PUT** /api/v2/vehicles/{vehicleId} | 
[**update_vehicle_category**](V2Api.md#update_vehicle_category) | **PUT** /api/v2/vehicles/categories/{categoryId} | 

# **create_user_profile**
> UserProfile create_user_profile(body=body)



Create user profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V2Api(swagger_client.ApiClient(configuration))
body = swagger_client.CreateProfile() # CreateProfile |  (optional)

try:
    api_response = api_instance.create_user_profile(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateProfile**](CreateProfile.md)|  | [optional] 

### Return type

[**UserProfile**](UserProfile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vehicle_category**
> VehicleCategory create_vehicle_category(body=body)



Create vehicle category

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V2Api(swagger_client.ApiClient(configuration))
body = swagger_client.CreateVehicleCategory() # CreateVehicleCategory |  (optional)

try:
    api_response = api_instance.create_vehicle_category(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_vehicle_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateVehicleCategory**](CreateVehicleCategory.md)|  | [optional] 

### Return type

[**VehicleCategory**](VehicleCategory.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_profile**
> delete_user_profile(profile_id)



Delete user profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V2Api(swagger_client.ApiClient(configuration))
profile_id = 56 # int | ID

try:
    api_instance.delete_user_profile(profile_id)
except ApiException as e:
    print("Exception when calling V2Api->delete_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**| ID | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vehicle_category**
> delete_vehicle_category(category_id)



Delete vehicle category

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V2Api(swagger_client.ApiClient(configuration))
category_id = 56 # int | ID

try:
    api_instance.delete_vehicle_category(category_id)
except ApiException as e:
    print("Exception when calling V2Api->delete_vehicle_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| ID | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_vehicle_maintenance**
> Vehicle enable_vehicle_maintenance(vehicle_id, body=body)



Enable vehicle maintenance mode

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V2Api(swagger_client.ApiClient(configuration))
vehicle_id = 56 # int | Vehicle ID
body = swagger_client.VehicleMaintenance() # VehicleMaintenance |  (optional)

try:
    api_response = api_instance.enable_vehicle_maintenance(vehicle_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->enable_vehicle_maintenance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| Vehicle ID | 
 **body** | [**VehicleMaintenance**](VehicleMaintenance.md)|  | [optional] 

### Return type

[**Vehicle**](Vehicle.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **get_current_user_profile**
> UserProfile get_current_user_profile()



Get current user profile

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
    api_response = api_instance.get_current_user_profile()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_current_user_profile: %s\n" % e)
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

# **get_notification_settings**
> NotificationSettings get_notification_settings()



Get notification settings

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
    api_response = api_instance.get_notification_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_notification_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NotificationSettings**](NotificationSettings.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_related_user_profiles**
> UserProfileList get_related_user_profiles(level_name, page=page, per_page=per_page)



Get related user-profiles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V2Api(swagger_client.ApiClient(configuration))
level_name = swagger_client.UserLevel() # UserLevel | User Level
page = 'page_example' # str | page (optional)
per_page = 'per_page_example' # str | per_page (optional)

try:
    api_response = api_instance.get_related_user_profiles(level_name, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_related_user_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level_name** | [**UserLevel**](.md)| User Level | 
 **page** | **str**| page | [optional] 
 **per_page** | **str**| per_page | [optional] 

### Return type

[**UserProfileList**](UserProfileList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_profile**
> UserProfile get_user_profile(profile_id)



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
profile_id = 56 # int | ID

try:
    api_response = api_instance.get_user_profile(profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**| ID | 

### Return type

[**UserProfile**](UserProfile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_category**
> VehicleCategory get_vehicle_category(category_id)



Get vehicle category

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V2Api(swagger_client.ApiClient(configuration))
category_id = 56 # int | ID

try:
    api_response = api_instance.get_vehicle_category(category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_vehicle_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| ID | 

### Return type

[**VehicleCategory**](VehicleCategory.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_category_list**
> VehicleCategoryList get_vehicle_category_list(page=page, per_page=per_page)



Get vehicle category list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V2Api(swagger_client.ApiClient(configuration))
page = 'page_example' # str | page (optional)
per_page = 'per_page_example' # str | per_page (optional)

try:
    api_response = api_instance.get_vehicle_category_list(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_vehicle_category_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| page | [optional] 
 **per_page** | **str**| per_page | [optional] 

### Return type

[**VehicleCategoryList**](VehicleCategoryList.md)

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
> VehicleDailyStats get_vehicles_daily_stats(vehicle_id, filters_started_at=filters_started_at, filters_ended_at=filters_ended_at)



Get vehicles daily statistics

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
filters_started_at = 'filters_started_at_example' # str | filters[started_at] (optional)
filters_ended_at = 'filters_ended_at_example' # str | filters[ended_at] (optional)

try:
    api_response = api_instance.get_vehicles_daily_stats(vehicle_id, filters_started_at=filters_started_at, filters_ended_at=filters_ended_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_vehicles_daily_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| vehicle identifier | 
 **filters_started_at** | **str**| filters[started_at] | [optional] 
 **filters_ended_at** | **str**| filters[ended_at] | [optional] 

### Return type

[**VehicleDailyStats**](VehicleDailyStats.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicles_frame_history**
> FrameHistory get_vehicles_frame_history(vehicle_id, filters_started_at=filters_started_at, filters_ended_at=filters_ended_at, page=page, per_page=per_page)



Get vehicles frame-history

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
filters_started_at = 'filters_started_at_example' # str | filters[started_at] (optional)
filters_ended_at = 'filters_ended_at_example' # str | filters[ended_at] (optional)
page = 'page_example' # str | page (optional)
per_page = 'per_page_example' # str | per_page (optional)

try:
    api_response = api_instance.get_vehicles_frame_history(vehicle_id, filters_started_at=filters_started_at, filters_ended_at=filters_ended_at, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_vehicles_frame_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| vehicle identifier | 
 **filters_started_at** | **str**| filters[started_at] | [optional] 
 **filters_ended_at** | **str**| filters[ended_at] | [optional] 
 **page** | **str**| page | [optional] 
 **per_page** | **str**| per_page | [optional] 

### Return type

[**FrameHistory**](FrameHistory.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicles_refuels**
> RefuelsList get_vehicles_refuels(vehicle_id, filters_started_at=filters_started_at, filters_ended_at=filters_ended_at)



Get vehicles refuels

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
filters_started_at = 'filters_started_at_example' # str | filters[started_at] (optional)
filters_ended_at = 'filters_ended_at_example' # str | filters[ended_at] (optional)

try:
    api_response = api_instance.get_vehicles_refuels(vehicle_id, filters_started_at=filters_started_at, filters_ended_at=filters_ended_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_vehicles_refuels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| vehicle identifier | 
 **filters_started_at** | **str**| filters[started_at] | [optional] 
 **filters_ended_at** | **str**| filters[ended_at] | [optional] 

### Return type

[**RefuelsList**](RefuelsList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicles_stopped_consumptions**
> StopppedConsumptionList get_vehicles_stopped_consumptions(vehicle_id, filters_started_at=filters_started_at, filters_ended_at=filters_ended_at, page=page, per_page=per_page)



Get vehicles stopped-consumptions

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
filters_started_at = 'filters_started_at_example' # str | filters[started_at] (optional)
filters_ended_at = 'filters_ended_at_example' # str | filters[ended_at] (optional)
page = 'page_example' # str | page (optional)
per_page = 'per_page_example' # str | per_page (optional)

try:
    api_response = api_instance.get_vehicles_stopped_consumptions(vehicle_id, filters_started_at=filters_started_at, filters_ended_at=filters_ended_at, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_vehicles_stopped_consumptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| vehicle identifier | 
 **filters_started_at** | **str**| filters[started_at] | [optional] 
 **filters_ended_at** | **str**| filters[ended_at] | [optional] 
 **page** | **str**| page | [optional] 
 **per_page** | **str**| per_page | [optional] 

### Return type

[**StopppedConsumptionList**](StopppedConsumptionList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_api_token**
> UserProfile refresh_api_token()



Refresh api token

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
    api_response = api_instance.refresh_api_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->refresh_api_token: %s\n" % e)
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

# **update_notification_settings**
> NotificationSettings update_notification_settings(body=body)



Update notification settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V2Api(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateNotificationSettings() # UpdateNotificationSettings |  (optional)

try:
    api_response = api_instance.update_notification_settings(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->update_notification_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateNotificationSettings**](UpdateNotificationSettings.md)|  | [optional] 

### Return type

[**NotificationSettings**](NotificationSettings.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_profile**
> UserProfile update_user_profile(profile_id, body=body)



Update user profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V2Api(swagger_client.ApiClient(configuration))
profile_id = 56 # int | ID
body = swagger_client.UpdateProfile() # UpdateProfile |  (optional)

try:
    api_response = api_instance.update_user_profile(profile_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->update_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**| ID | 
 **body** | [**UpdateProfile**](UpdateProfile.md)|  | [optional] 

### Return type

[**UserProfile**](UserProfile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vehicle**
> Vehicle update_vehicle(vehicle_id, body=body)



Update vehicle

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V2Api(swagger_client.ApiClient(configuration))
vehicle_id = 56 # int | ID
body = swagger_client.UpdateVehicle() # UpdateVehicle |  (optional)

try:
    api_response = api_instance.update_vehicle(vehicle_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->update_vehicle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| ID | 
 **body** | [**UpdateVehicle**](UpdateVehicle.md)|  | [optional] 

### Return type

[**Vehicle**](Vehicle.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vehicle_category**
> VehicleCategory update_vehicle_category(category_id, body=body)



Update vehicle category

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V2Api(swagger_client.ApiClient(configuration))
category_id = 56 # int | ID
body = swagger_client.UpdateVehicleCategory() # UpdateVehicleCategory |  (optional)

try:
    api_response = api_instance.update_vehicle_category(category_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2Api->update_vehicle_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| ID | 
 **body** | [**UpdateVehicleCategory**](UpdateVehicleCategory.md)|  | [optional] 

### Return type

[**VehicleCategory**](VehicleCategory.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

