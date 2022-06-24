# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._key_vault_client_operations import build_backup_secret_request, build_delete_secret_request, build_get_deleted_secret_request, build_get_deleted_secrets_request, build_get_secret_request, build_get_secret_versions_request, build_get_secrets_request, build_purge_deleted_secret_request, build_recover_deleted_secret_request, build_restore_secret_request, build_set_secret_request, build_update_secret_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class KeyVaultClientOperationsMixin:

    @distributed_trace_async
    async def set_secret(
        self,
        vault_base_url: str,
        secret_name: str,
        parameters: "_models.SecretSetParameters",
        **kwargs: Any
    ) -> "_models.SecretBundle":
        """Sets a secret in a specified key vault.

        The SET operation adds a secret to the Azure Key Vault. If the named secret already exists,
        Azure Key Vault creates a new version of that secret. This operation requires the secrets/set
        permission.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param secret_name: The name of the secret.
        :type secret_name: str
        :param parameters: The parameters for setting the secret.
        :type parameters: ~azure.keyvault.v7_3.models.SecretSetParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecretBundle, or the result of cls(response)
        :rtype: ~azure.keyvault.v7_3.models.SecretBundle
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SecretBundle"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "7.3")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'SecretSetParameters')

        request = build_set_secret_request(
            secret_name=secret_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.set_secret.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SecretBundle', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    set_secret.metadata = {'url': "/secrets/{secret-name}"}  # type: ignore


    @distributed_trace_async
    async def delete_secret(
        self,
        vault_base_url: str,
        secret_name: str,
        **kwargs: Any
    ) -> "_models.DeletedSecretBundle":
        """Deletes a secret from a specified key vault.

        The DELETE operation applies to any secret stored in Azure Key Vault. DELETE cannot be applied
        to an individual version of a secret. This operation requires the secrets/delete permission.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param secret_name: The name of the secret.
        :type secret_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DeletedSecretBundle, or the result of cls(response)
        :rtype: ~azure.keyvault.v7_3.models.DeletedSecretBundle
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DeletedSecretBundle"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "7.3")  # type: str

        
        request = build_delete_secret_request(
            secret_name=secret_name,
            api_version=api_version,
            template_url=self.delete_secret.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('DeletedSecretBundle', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    delete_secret.metadata = {'url': "/secrets/{secret-name}"}  # type: ignore


    @distributed_trace_async
    async def update_secret(
        self,
        vault_base_url: str,
        secret_name: str,
        secret_version: str,
        parameters: "_models.SecretUpdateParameters",
        **kwargs: Any
    ) -> "_models.SecretBundle":
        """Updates the attributes associated with a specified secret in a given key vault.

        The UPDATE operation changes specified attributes of an existing stored secret. Attributes that
        are not specified in the request are left unchanged. The value of a secret itself cannot be
        changed. This operation requires the secrets/set permission.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param secret_name: The name of the secret.
        :type secret_name: str
        :param secret_version: The version of the secret.
        :type secret_version: str
        :param parameters: The parameters for update secret operation.
        :type parameters: ~azure.keyvault.v7_3.models.SecretUpdateParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecretBundle, or the result of cls(response)
        :rtype: ~azure.keyvault.v7_3.models.SecretBundle
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SecretBundle"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "7.3")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'SecretUpdateParameters')

        request = build_update_secret_request(
            secret_name=secret_name,
            secret_version=secret_version,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.update_secret.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SecretBundle', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update_secret.metadata = {'url': "/secrets/{secret-name}/{secret-version}"}  # type: ignore


    @distributed_trace_async
    async def get_secret(
        self,
        vault_base_url: str,
        secret_name: str,
        secret_version: str,
        **kwargs: Any
    ) -> "_models.SecretBundle":
        """Get a specified secret from a given key vault.

        The GET operation is applicable to any secret stored in Azure Key Vault. This operation
        requires the secrets/get permission.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param secret_name: The name of the secret.
        :type secret_name: str
        :param secret_version: The version of the secret. This URI fragment is optional. If not
         specified, the latest version of the secret is returned.
        :type secret_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecretBundle, or the result of cls(response)
        :rtype: ~azure.keyvault.v7_3.models.SecretBundle
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SecretBundle"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "7.3")  # type: str

        
        request = build_get_secret_request(
            secret_name=secret_name,
            secret_version=secret_version,
            api_version=api_version,
            template_url=self.get_secret.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SecretBundle', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_secret.metadata = {'url': "/secrets/{secret-name}/{secret-version}"}  # type: ignore


    @distributed_trace
    def get_secrets(
        self,
        vault_base_url: str,
        maxresults: Optional[int] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.SecretListResult"]:
        """List secrets in a specified key vault.

        The Get Secrets operation is applicable to the entire vault. However, only the base secret
        identifier and its attributes are provided in the response. Individual secret versions are not
        listed in the response. This operation requires the secrets/list permission.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param maxresults: Maximum number of results to return in a page. If not specified, the service
         will return up to 25 results. Default value is None.
        :type maxresults: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SecretListResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.keyvault.v7_3.models.SecretListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "7.3")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SecretListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_get_secrets_request(
                    api_version=api_version,
                    maxresults=maxresults,
                    template_url=self.get_secrets.metadata['url'],
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

            else:
                
                request = build_get_secrets_request(
                    api_version=api_version,
                    maxresults=maxresults,
                    template_url=next_link,
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

                path_format_arguments = {
                    "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
                }
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("SecretListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    get_secrets.metadata = {'url': "/secrets"}  # type: ignore

    @distributed_trace
    def get_secret_versions(
        self,
        vault_base_url: str,
        secret_name: str,
        maxresults: Optional[int] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.SecretListResult"]:
        """List all versions of the specified secret.

        The full secret identifier and attributes are provided in the response. No values are returned
        for the secrets. This operations requires the secrets/list permission.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param secret_name: The name of the secret.
        :type secret_name: str
        :param maxresults: Maximum number of results to return in a page. If not specified, the service
         will return up to 25 results. Default value is None.
        :type maxresults: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SecretListResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.keyvault.v7_3.models.SecretListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "7.3")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SecretListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_get_secret_versions_request(
                    secret_name=secret_name,
                    api_version=api_version,
                    maxresults=maxresults,
                    template_url=self.get_secret_versions.metadata['url'],
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

            else:
                
                request = build_get_secret_versions_request(
                    secret_name=secret_name,
                    api_version=api_version,
                    maxresults=maxresults,
                    template_url=next_link,
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

                path_format_arguments = {
                    "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
                }
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("SecretListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    get_secret_versions.metadata = {'url': "/secrets/{secret-name}/versions"}  # type: ignore

    @distributed_trace
    def get_deleted_secrets(
        self,
        vault_base_url: str,
        maxresults: Optional[int] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.DeletedSecretListResult"]:
        """Lists deleted secrets for the specified vault.

        The Get Deleted Secrets operation returns the secrets that have been deleted for a vault
        enabled for soft-delete. This operation requires the secrets/list permission.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param maxresults: Maximum number of results to return in a page. If not specified the service
         will return up to 25 results. Default value is None.
        :type maxresults: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either DeletedSecretListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.keyvault.v7_3.models.DeletedSecretListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "7.3")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DeletedSecretListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_get_deleted_secrets_request(
                    api_version=api_version,
                    maxresults=maxresults,
                    template_url=self.get_deleted_secrets.metadata['url'],
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

            else:
                
                request = build_get_deleted_secrets_request(
                    api_version=api_version,
                    maxresults=maxresults,
                    template_url=next_link,
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

                path_format_arguments = {
                    "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
                }
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("DeletedSecretListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    get_deleted_secrets.metadata = {'url': "/deletedsecrets"}  # type: ignore

    @distributed_trace_async
    async def get_deleted_secret(
        self,
        vault_base_url: str,
        secret_name: str,
        **kwargs: Any
    ) -> "_models.DeletedSecretBundle":
        """Gets the specified deleted secret.

        The Get Deleted Secret operation returns the specified deleted secret along with its
        attributes. This operation requires the secrets/get permission.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param secret_name: The name of the secret.
        :type secret_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DeletedSecretBundle, or the result of cls(response)
        :rtype: ~azure.keyvault.v7_3.models.DeletedSecretBundle
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DeletedSecretBundle"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "7.3")  # type: str

        
        request = build_get_deleted_secret_request(
            secret_name=secret_name,
            api_version=api_version,
            template_url=self.get_deleted_secret.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('DeletedSecretBundle', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_deleted_secret.metadata = {'url': "/deletedsecrets/{secret-name}"}  # type: ignore


    @distributed_trace_async
    async def purge_deleted_secret(  # pylint: disable=inconsistent-return-statements
        self,
        vault_base_url: str,
        secret_name: str,
        **kwargs: Any
    ) -> None:
        """Permanently deletes the specified secret.

        The purge deleted secret operation removes the secret permanently, without the possibility of
        recovery. This operation can only be enabled on a soft-delete enabled vault. This operation
        requires the secrets/purge permission.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param secret_name: The name of the secret.
        :type secret_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "7.3")  # type: str

        
        request = build_purge_deleted_secret_request(
            secret_name=secret_name,
            api_version=api_version,
            template_url=self.purge_deleted_secret.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    purge_deleted_secret.metadata = {'url': "/deletedsecrets/{secret-name}"}  # type: ignore


    @distributed_trace_async
    async def recover_deleted_secret(
        self,
        vault_base_url: str,
        secret_name: str,
        **kwargs: Any
    ) -> "_models.SecretBundle":
        """Recovers the deleted secret to the latest version.

        Recovers the deleted secret in the specified vault. This operation can only be performed on a
        soft-delete enabled vault. This operation requires the secrets/recover permission.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param secret_name: The name of the deleted secret.
        :type secret_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecretBundle, or the result of cls(response)
        :rtype: ~azure.keyvault.v7_3.models.SecretBundle
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SecretBundle"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "7.3")  # type: str

        
        request = build_recover_deleted_secret_request(
            secret_name=secret_name,
            api_version=api_version,
            template_url=self.recover_deleted_secret.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SecretBundle', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    recover_deleted_secret.metadata = {'url': "/deletedsecrets/{secret-name}/recover"}  # type: ignore


    @distributed_trace_async
    async def backup_secret(
        self,
        vault_base_url: str,
        secret_name: str,
        **kwargs: Any
    ) -> "_models.BackupSecretResult":
        """Backs up the specified secret.

        Requests that a backup of the specified secret be downloaded to the client. All versions of the
        secret will be downloaded. This operation requires the secrets/backup permission.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param secret_name: The name of the secret.
        :type secret_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BackupSecretResult, or the result of cls(response)
        :rtype: ~azure.keyvault.v7_3.models.BackupSecretResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.BackupSecretResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "7.3")  # type: str

        
        request = build_backup_secret_request(
            secret_name=secret_name,
            api_version=api_version,
            template_url=self.backup_secret.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('BackupSecretResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    backup_secret.metadata = {'url': "/secrets/{secret-name}/backup"}  # type: ignore


    @distributed_trace_async
    async def restore_secret(
        self,
        vault_base_url: str,
        parameters: "_models.SecretRestoreParameters",
        **kwargs: Any
    ) -> "_models.SecretBundle":
        """Restores a backed up secret to a vault.

        Restores a backed up secret, and all its versions, to a vault. This operation requires the
        secrets/restore permission.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param parameters: The parameters to restore the secret.
        :type parameters: ~azure.keyvault.v7_3.models.SecretRestoreParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecretBundle, or the result of cls(response)
        :rtype: ~azure.keyvault.v7_3.models.SecretBundle
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SecretBundle"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "7.3")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'SecretRestoreParameters')

        request = build_restore_secret_request(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.restore_secret.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SecretBundle', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    restore_secret.metadata = {'url': "/secrets/restore"}  # type: ignore

