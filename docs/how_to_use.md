## How to use this module
Before using this module, you need to sign up to the Azure portal https://portal.azure.com and create your “Key Vault”:

1. **Access the Azure portal**

2. **Create a new Key Vault:**
In the search bar, type “Key Vault” and select “Azure Key Vault”, click Create.

3. **Configure the Key Vault details:**
  - Subscription: Select the subscription in which you want to create the Key Vault.
  - Resource Group:
    Choose an existing resource group or create a new one.
  - Key Vault Name:
    Enter a unique name for the Key Vault (must be globally unique).
  - Region:
    Select the region where the Key Vault will be stored.
  - Network Options:
    Choose whether you want access to be public or restricted to private networks.

4. **Review and create**

# Steps to log in to Azure and connect to the Key Vault:

1. **Create an Azure AD Application (Service Principal) | Application Registration**
  - Get client_id, tenant_id, and client_secret
  - Client ID: Found in the summary section of your application.
  - Tenant ID: Also found in your application summary.
  - Client Secret:
    - Go to “Certificates & Secrets” in the application registration.
    - Create a new client secret and make sure to copy and save the value as you won’t be able to see it again.

2. **Assign Application Access in Key Vault**
  - Go to your Key Vault in the portal.
  - Select “Access Policies” from the side menu.
  - Click “Add Access Policy.”
  - Assign permissions as needed, for example:
    - Secret Permissions: Get, List, Set.
    - Key Permissions: Get, List, Create, Import.
    - Certificate Permissions: Get, List, Manage
  - Select the registered application (Service Principal) under Principal.
  - Save changes.

---

## Como usar este módulo

Antes de usar este módulo, es necesario registrarse en el portal de Azure https://portal.azure.com y crear tu “Key Vault”:

1.	**Accede al portal de Azure**

2.	**Crea un nuevo Key Vault:**
    En la barra de búsqueda, escribe "Key Vault" y selecciona "Azure Key Vault", haz clic en Crear.

3.	**Configura los detalles del Key Vault:**
    -	Suscripción: Selecciona la suscripción en la que deseas crear el Key Vault.
    -	Grupo de recursos:
      Elige un grupo de recursos existente o crea uno nuevo.
    -	Nombre del Key Vault:
      Escribe un nombre único para el Key Vault (debe ser globalmente único).
    -	Región:
      Selecciona la región donde se almacenará el Key Vault.
    -	Opciones de red:
      Elige si deseas que el acceso sea público o restringido a redes privadas.

4. **Revisa y crea**

# Pasos para ingresar a Azure y conectarse al baúl de llaves:

1. **Crear una Aplicación de Azure AD (Service Principal) | registro de aplicaciones**
    - Obtener client_id, tenant_id y client_secret
    - Client ID (ID de la aplicación): Se encuentra en la sección de resumen de tu aplicación.
    - Tenant ID (ID del directorio): También está en el resumen de tu aplicación.
    - Client Secret (secreto del cliente):
      -	Ve a "Certificados y secretos" en el registro de la aplicación.
      -	Crea un nuevo secreto de cliente  y asegúrate de copiar y guarda el valor, ya que no podrás verlo nuevamente.

2.	**Asignar Acceso a la Aplicación en el Key Vault**
    - Ve a tu Key Vault en el portal.
    - Selecciona "Políticas de acceso" en el menú lateral.
    - Haz clic en "Agregar política de acceso".
    - Asigna permisos según las necesidades, por ejemplo:
      - Permisos de secreto: Obtener, enumerar, establecer.
      - Permisos de clave: Obtener, enumerar, crear, importar.
      - Permisos de certificado: Obtener, enumerar, administrar
    - Selecciona la aplicación registrada (Service Principal) bajo Principal.
    - Guarda los cambios.

---

## Como usar este módulo

Antes de utilizar este módulo, você precisa se cadastrar no portal Azure https://portal.azure.com e criar seu “Key Vault”:

1. **Acesse o portal do Azure**

2. **Crie um novo Cofre de Chaves:**
    Na barra de pesquisa, digite "Key Vault" e selecione "Azure Key Vault", clique em Criar.

3. **Configure os detalhes do Key Vault:**
    - Assinatura: selecione a assinatura na qual deseja criar o Key Vault.
    - Grupo de recursos:
        Escolha um grupo de recursos existente ou crie um novo.
    - Nome do Cofre de Chaves:
        Insira um nome exclusivo para o Key Vault (deve ser globalmente exclusivo).
    - Região:
        Selecione a região onde o Key Vault será armazenado.
    - Opções de rede:
        Escolha se deseja que o acesso seja público ou restrito a redes privadas.

4. **Revise e crie**

# Etapas para entrar no Azure e conectar-se ao cofre de chaves:

1. **Crie um aplicativo Azure AD (principal de serviço) | registro de inscrição**
    - Obtenha client_id, tenant_id e client_secret
    - ID do Cliente: Encontrado naseção de resumo do seu aplicativo.
    - ID do locatário: também está no resumo da sua inscrição.
    - Segredo do cliente:
      - Acesse “Certificados e segredos” no cadastro do aplicativo.
      - Crie um novo segredo do cliente e copie e salve o valor, pois você não poderá vê-lo novamente.

2. **Atribua acesso ao aplicativo no Key Vault**
    - Vá para o seu Key Vault no portal.
    - Selecione “Políticas de Acesso” no menu lateral.
    - Clique em “Adicionar política de acesso”.
    - Atribua permissões conforme necessário, por exemplo:
      - Permissões secretas: obter, listar, definir.
      -  Permissões principais: Obter, Listar, Criar, Importar.
      - Permissões de certificado: obter, listar, gerenciar
    - Selecione o aplicativo registrado (Principal de Serviço) em Principal.
    - Salve as alterações.
