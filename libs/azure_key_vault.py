from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential


class AzureKeyVault:
    def __init__(self, tenant_id, client_id, client_secret):
        """Authenticates as a service principal using a client secret.

    :param str tenant_id: ID of the service principal's tenant. Also called its "directory" ID.
    :param str client_id: the service principal's client ID
    :param str client_secret: one of the service principal's client secrets

    Util resources:
    - https://azuresdkdocs.blob.core.windows.net/$web/python/azure-identity/latest/azure.identity.html#azure.identity.ClientSecretCredential
    - https://azuresdkdocs.blob.core.windows.net/$web/python/azure-keyvault-secrets/latest/azure.keyvault.secrets.html#azure.keyvault.secrets.SecretClient
    - https://docs.microsoft.com/es-ES/python/api/overview/azure/keyvault-secrets-readme?view=azure-python#retrieve-a-secret
    - Asignar una directiva de acceso al almacen de claves : https://docs.microsoft.com/en-us/azure/key-vault/general/assign-access-policy?tabs=azure-portal
    - Autentificacion de Azure Key Vault : https://docs.microsoft.com/es-mx/azure/key-vault/general/authentication
    """
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.credential = ClientSecretCredential(tenant_id, client_id, client_secret)


    def connect_key_vault(self, vault_url):
        self.secret = SecretClient(vault_url, self.credential)
        return self.secret

    def get_secret(self, name_secret):
        result = self.secret.get_secret(name_secret)
        return result.value

    def set_secret(self, secret_name, secret_value):
        return self.secret.set_secret(secret_name, secret_value)
    
    def update_property_secret(self, secret_name:str, content_type=None, enable=None):
        update_secret_properties = self.secret.update_secret_properties(secret_name, content_type=content_type, enabled=enable)
        return update_secret_properties

    def delete_secret(self, secret_name:str):
        delete = self.secret.begin_delete_secret(secret_name).result()
        return delete
    
    def list_secrets(self):
        secrets = []
        secret_properties = self.secret.list_properties_of_secrets()
        for secret_property in secret_properties:
            secrets.append(secret_property.name)
        return secrets
    

if __name__ == "__main__":
    pass

   





