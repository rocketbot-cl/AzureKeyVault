# Azure Key Vault
  
Este modulo permite que você proteja, crie ou recupere chaves criptográficas e outros segredos usados por aplicativos e serviços em nuvem.  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Overview


1. Conectar cofre de chaves  
Com este comando, você pode se conectar ao chaveiro Azure.

2. Obter segredo  
Com este comando você pode obter um segredo do Cofre de Chaves Azure

3. Criar ou modificar o segredo  
Com este comando, você pode criar ou modificar um segredo no Cofre de Chaves Azure.

4. Atualizar propiedade do segredo  
Com este comando você pode atualizar a propriedade secreta (como o tipo, habilitado/desabilitado).

5. Retirar o segredo  
Com este comando você pode apagar um segredo.  




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**azure-keyvault-secrets**](https://pypi.org/project/azure-keyvault-secrets/)- [**azure-identity**](https://pypi.org/project/azure-identity/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)