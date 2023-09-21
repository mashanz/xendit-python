"""
    Payment Requests

    This API is used for Payment Requests  # noqa: E501

    The version of the OpenAPI document: 1.44.0
"""

import re  # noqa: F401
import sys  # noqa: F401

from xendit.api_client import ApiClient, Endpoint as _Endpoint
from xendit.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)

from xendit.payment_request.model import *  # noqa: F401,E501

class PaymentRequestApi(object):
    """NOTE: This class is auto generated by the OpenAPI Generator.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.authorize_payment_request_endpoint = _Endpoint(
            settings={
                'response_type': (PaymentRequest,),
                'auth': [],
                'endpoint_path': '/payment_requests/{paymentRequestId}/auth',
                'operation_id': 'authorize_payment_request',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_request_id',
                    'payment_request_auth_parameters',
                ],
                'required': [
                    'payment_request_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'payment_request_id':
                        (str,),
                    'payment_request_auth_parameters':
                        (PaymentRequestAuthParameters,),
                },
                'attribute_map': {
                    'payment_request_id': 'paymentRequestId',
                },
                'location_map': {
                    'payment_request_id': 'path',
                    'payment_request_auth_parameters': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.capture_payment_request_endpoint = _Endpoint(
            settings={
                'response_type': (Capture,),
                'auth': [],
                'endpoint_path': '/payment_requests/{paymentRequestId}/captures',
                'operation_id': 'capture_payment_request',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_request_id',
                    'capture_parameters',
                ],
                'required': [
                    'payment_request_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'payment_request_id':
                        (str,),
                    'capture_parameters':
                        (CaptureParameters,),
                },
                'attribute_map': {
                    'payment_request_id': 'paymentRequestId',
                },
                'location_map': {
                    'payment_request_id': 'path',
                    'capture_parameters': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.create_payment_request_endpoint = _Endpoint(
            settings={
                'response_type': (PaymentRequest,),
                'auth': [],
                'endpoint_path': '/payment_requests',
                'operation_id': 'create_payment_request',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'idempotency_key',
                    'payment_request_parameters',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'idempotency_key':
                        (str,),
                    'payment_request_parameters':
                        (PaymentRequestParameters,),
                },
                'attribute_map': {
                    'idempotency_key': 'idempotency-key',
                },
                'location_map': {
                    'idempotency_key': 'header',
                    'payment_request_parameters': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.get_all_payment_requests_endpoint = _Endpoint(
            settings={
                'response_type': (PaymentRequestListResponse,),
                'auth': [],
                'endpoint_path': '/payment_requests',
                'operation_id': 'get_all_payment_requests',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'reference_id',
                    'id',
                    'customer_id',
                    'limit',
                    'before_id',
                    'after_id',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'reference_id':
                        ([str],),
                    'id':
                        ([str],),
                    'customer_id':
                        ([str],),
                    'limit':
                        (int,),
                    'before_id':
                        (str,),
                    'after_id':
                        (str,),
                },
                'attribute_map': {
                    'reference_id': 'reference_id',
                    'id': 'id',
                    'customer_id': 'customer_id',
                    'limit': 'limit',
                    'before_id': 'before_id',
                    'after_id': 'after_id',
                },
                'location_map': {
                    'reference_id': 'query',
                    'id': 'query',
                    'customer_id': 'query',
                    'limit': 'query',
                    'before_id': 'query',
                    'after_id': 'query',
                },
                'collection_format_map': {
                    'reference_id': 'multi',
                    'id': 'multi',
                    'customer_id': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_payment_request_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (PaymentRequest,),
                'auth': [],
                'endpoint_path': '/payment_requests/{paymentRequestId}',
                'operation_id': 'get_payment_request_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_request_id',
                ],
                'required': [
                    'payment_request_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'payment_request_id':
                        (str,),
                },
                'attribute_map': {
                    'payment_request_id': 'paymentRequestId',
                },
                'location_map': {
                    'payment_request_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_payment_request_captures_endpoint = _Endpoint(
            settings={
                'response_type': (CaptureListResponse,),
                'auth': [],
                'endpoint_path': '/payment_requests/{paymentRequestId}/captures',
                'operation_id': 'get_payment_request_captures',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_request_id',
                    'limit',
                    'after_id',
                    'before_id',
                ],
                'required': [
                    'payment_request_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'payment_request_id':
                        (str,),
                    'limit':
                        (int,),
                    'after_id':
                        (str,),
                    'before_id':
                        (str,),
                },
                'attribute_map': {
                    'payment_request_id': 'paymentRequestId',
                    'limit': 'limit',
                    'after_id': 'after_id',
                    'before_id': 'before_id',
                },
                'location_map': {
                    'payment_request_id': 'path',
                    'limit': 'query',
                    'after_id': 'query',
                    'before_id': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.resend_payment_request_auth_endpoint = _Endpoint(
            settings={
                'response_type': (PaymentRequest,),
                'auth': [],
                'endpoint_path': '/payment_requests/{paymentRequestId}/auth/resend',
                'operation_id': 'resend_payment_request_auth',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_request_id',
                ],
                'required': [
                    'payment_request_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'payment_request_id':
                        (str,),
                },
                'attribute_map': {
                    'payment_request_id': 'paymentRequestId',
                },
                'location_map': {
                    'payment_request_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def authorize_payment_request(
        self,
        payment_request_id,
        **kwargs
    ):
        """Payment Request Authorize  # noqa: E501

        Payment Request Authorize  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.authorize_payment_request(payment_request_id, async_req=True)
        >>> result = thread.get()

        Args:
            payment_request_id (str):

        Keyword Args:
            payment_request_auth_parameters (PaymentRequestAuthParameters): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            PaymentRequest
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['payment_request_id'] = \
            payment_request_id
        return self.authorize_payment_request_endpoint.call_with_http_info(**kwargs)

    def capture_payment_request(
        self,
        payment_request_id,
        **kwargs
    ):
        """Payment Request Capture  # noqa: E501

        Payment Request Capture  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.capture_payment_request(payment_request_id, async_req=True)
        >>> result = thread.get()

        Args:
            payment_request_id (str):

        Keyword Args:
            capture_parameters (CaptureParameters): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Capture
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['payment_request_id'] = \
            payment_request_id
        return self.capture_payment_request_endpoint.call_with_http_info(**kwargs)

    def create_payment_request(
        self,
        **kwargs
    ):
        """Create Payment Request  # noqa: E501

        Create Payment Request  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_payment_request(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            idempotency_key (str): [optional]
            payment_request_parameters (PaymentRequestParameters): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            PaymentRequest
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.create_payment_request_endpoint.call_with_http_info(**kwargs)

    def get_all_payment_requests(
        self,
        **kwargs
    ):
        """Get all payment requests by filter  # noqa: E501

        Get all payment requests by filter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_all_payment_requests(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            reference_id ([str]): [optional]
            id ([str]): [optional]
            customer_id ([str]): [optional]
            limit (int): [optional]
            before_id (str): [optional]
            after_id (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            PaymentRequestListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.get_all_payment_requests_endpoint.call_with_http_info(**kwargs)

    def get_payment_request_by_id(
        self,
        payment_request_id,
        **kwargs
    ):
        """Get payment request by ID  # noqa: E501

        Get payment request by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_payment_request_by_id(payment_request_id, async_req=True)
        >>> result = thread.get()

        Args:
            payment_request_id (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            PaymentRequest
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['payment_request_id'] = \
            payment_request_id
        return self.get_payment_request_by_id_endpoint.call_with_http_info(**kwargs)

    def get_payment_request_captures(
        self,
        payment_request_id,
        **kwargs
    ):
        """Get Payment Request Capture  # noqa: E501

        Get Payment Request Capture  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_payment_request_captures(payment_request_id, async_req=True)
        >>> result = thread.get()

        Args:
            payment_request_id (str):

        Keyword Args:
            limit (int): [optional]
            after_id (str): [optional]
            before_id (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CaptureListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['payment_request_id'] = \
            payment_request_id
        return self.get_payment_request_captures_endpoint.call_with_http_info(**kwargs)

    def resend_payment_request_auth(
        self,
        payment_request_id,
        **kwargs
    ):
        """Payment Request Resend Auth  # noqa: E501

        Payment Request Resend Auth  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.resend_payment_request_auth(payment_request_id, async_req=True)
        >>> result = thread.get()

        Args:
            payment_request_id (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            PaymentRequest
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['payment_request_id'] = \
            payment_request_id
        return self.resend_payment_request_auth_endpoint.call_with_http_info(**kwargs)

