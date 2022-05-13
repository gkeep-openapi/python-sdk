# swagger_client.UserAuthorizationApi

All URIs are relative to *https://staging-transport.smart-gamma.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize**](UserAuthorizationApi.md#authorize) | **POST** /api/login_check | 

# **authorize**
> AuthorizedUser authorize(body)



User authorization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAuthorizationApi()
body = swagger_client.UserCredentials() # UserCredentials | A JSON object containing user credentials info

try:
    api_response = api_instance.authorize(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAuthorizationApi->authorize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCredentials**](UserCredentials.md)| A JSON object containing user credentials info | 

### Return type

[**AuthorizedUser**](AuthorizedUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

