# swagger_client.V1Api

All URIs are relative to *https://staging-transport.smart-gamma.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_countries_list**](V1Api.md#get_countries_list) | **GET** /api/v1/countries/by | 
[**get_tank_type_list**](V1Api.md#get_tank_type_list) | **GET** /api/v1/tank/types/by | 
[**get_user_group_list**](V1Api.md#get_user_group_list) | **GET** /api/v1/user/allowed/groups | 
[**get_vehicle_brand_list**](V1Api.md#get_vehicle_brand_list) | **GET** /api/v1/vehicle/brands | 
[**get_vehicle_fuel_types_list**](V1Api.md#get_vehicle_fuel_types_list) | **GET** /api/v1/vehicle/fuel-types | 
[**get_vehicle_model_list**](V1Api.md#get_vehicle_model_list) | **GET** /api/v1/vehicle/models | 
[**get_vehicle_national_type_list**](V1Api.md#get_vehicle_national_type_list) | **GET** /api/v1/vehicle/national-types | 
[**get_vehicle_properties_list**](V1Api.md#get_vehicle_properties_list) | **GET** /api/v1/vehicle/properties | 
[**get_vehicle_type_list**](V1Api.md#get_vehicle_type_list) | **GET** /api/v1/vehicle/types | 
[**get_vehicle_version_list**](V1Api.md#get_vehicle_version_list) | **GET** /api/v1/vehicle/versions | 

# **get_countries_list**
> CountryList get_countries_list()



Get countries

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V1Api(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_countries_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1Api->get_countries_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CountryList**](CountryList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tank_type_list**
> TankTypeList get_tank_type_list()



Get tank types

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V1Api(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_tank_type_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1Api->get_tank_type_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TankTypeList**](TankTypeList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_group_list**
> UserGroupList get_user_group_list()



Get user allowed groups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V1Api(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_user_group_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1Api->get_user_group_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserGroupList**](UserGroupList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_brand_list**
> VehicleBrandList get_vehicle_brand_list()



Get vehicle brands

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V1Api(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_vehicle_brand_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1Api->get_vehicle_brand_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VehicleBrandList**](VehicleBrandList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_fuel_types_list**
> VehicleFuelTypeList get_vehicle_fuel_types_list()



Get vehicle fuel-types

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V1Api(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_vehicle_fuel_types_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1Api->get_vehicle_fuel_types_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VehicleFuelTypeList**](VehicleFuelTypeList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_model_list**
> VehicleModelList get_vehicle_model_list(page=page, per_page=per_page)



Get vehicle models

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V1Api(swagger_client.ApiClient(configuration))
page = 'page_example' # str | page (optional)
per_page = 'per_page_example' # str | per_page (optional)

try:
    api_response = api_instance.get_vehicle_model_list(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1Api->get_vehicle_model_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| page | [optional] 
 **per_page** | **str**| per_page | [optional] 

### Return type

[**VehicleModelList**](VehicleModelList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_national_type_list**
> VehicleNationalTypeList get_vehicle_national_type_list()



Get vehicle national-types

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V1Api(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_vehicle_national_type_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1Api->get_vehicle_national_type_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VehicleNationalTypeList**](VehicleNationalTypeList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_properties_list**
> VehiclePropertyList get_vehicle_properties_list()



Get vehicle properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V1Api(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_vehicle_properties_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1Api->get_vehicle_properties_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VehiclePropertyList**](VehiclePropertyList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_type_list**
> VehicleTypeList get_vehicle_type_list()



Get vehicle types

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V1Api(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_vehicle_type_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1Api->get_vehicle_type_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VehicleTypeList**](VehicleTypeList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_version_list**
> VehicleVersionList get_vehicle_version_list(page=page, per_page=per_page)



Get vehicle versions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.V1Api(swagger_client.ApiClient(configuration))
page = 'page_example' # str | page (optional)
per_page = 'per_page_example' # str | per_page (optional)

try:
    api_response = api_instance.get_vehicle_version_list(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1Api->get_vehicle_version_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| page | [optional] 
 **per_page** | **str**| per_page | [optional] 

### Return type

[**VehicleVersionList**](VehicleVersionList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

