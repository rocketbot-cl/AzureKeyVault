# Azure Key Vault
  
This module allows you to safeguard, create or retrieve cryptographic keys and other secrets used by cloud apps and services.  

*Read this in other languages: [English](Manual_AzureKeyVault.md), [Português](Manual_AzureKeyVault.pr.md), [Español](Manual_AzureKeyVault.es.md)*
  
![banner](imgs/Banner_AzureKeyVault.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Connect key vault
  
With this command you can connect to the Azure key vault
|Parameters|Description|example|
| --- | --- | --- |
|url of your key vault|Key vault url obtained from Azure key vault service|https://rocketbot.vault.azure.net/|
|Tenant ID|Directory ID that you can get from the home page of your application.|468fab45-2d6c-4164-a97d-52b88c1ee45c|
|Client ID|Application ID (client) obtained from the home page of the application created in azure|e827a5a7-ec88-45b2-89c9-0641289ef14b|
|Secret client value|Value of the secret obtained in the menu, certificates and application secrets|_d18Q~ceU4Pbcxy4TAbnMm1p6ArcidqegYSAFaYJ|
|Name of the variable where to assign the result |Variable where the result of the connection will be saved|variable|

### Get secret
  
With this command you can get a secret from Azure Key Vault
|Parameters|Description|example|
| --- | --- | --- |
|Write the name of your secret|Name of the secret you want to obtain|Secret1|
|Name of the variable where to assign the result ||variable|

### Create or update secret
  
With this command you can create or modify a secret in Azure Key Vault
|Parameters|Description|example|
| --- | --- | --- |
|Write the name of your secret|If the name exists, it will update it, if it does not exist, it will create it.|Secret1|
|Secret value|The value of the secret|12345|

### Update property of secret
  
With this command you can update the property of the secret (content type, enabled/disabled)
|Parameters|Description|example|
| --- | --- | --- |
|Write the name of your secret|Name of the secret whose properties you want to update|Secret1|
|Enable/Disable|Enable or disable the secret||
|Type of secret content (Optional) |Type of content you want your secret to have (example text/plain)|Text/plain|

### Delete secret
  
With this command you can delete a secret.
|Parameters|Description|example|
| --- | --- | --- |
|Type the name of the secret you want to delete|Name of the secret whose properties you want to update|Secret1|
