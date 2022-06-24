# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(id)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
   sudo pip install <package> -t .

"""
GetParams=GetParams #type:ignore
SetVar=SetVar#type:ignore

import os
import sys
import traceback

base_path= tmp_global_obj["basepath"] #type:ignore
libs_path = os.path.join(base_path, "modules", "AzureKeyVault", "libs")
if libs_path not in sys.path:
    sys.path.append(libs_path)


try:
    from azure_key_vault import AzureKeyVault #type:ignore

    global mod_azure_key_vault

    command = GetParams("module")
    if command == "connect":     #"connect" es el valor de "module" del comando del archivo package.json
        url = GetParams("url")    #"url" es el id del input del comando del archivo package.json
        tenant_id = GetParams("tenant-id")
        client_id= GetParams("client-id")
        client_secret= GetParams("client-secret")
        variable= GetParams("variable")
        
        mod_azure_key_vault = AzureKeyVault(tenant_id, client_id, client_secret)
        secrets_vault = mod_azure_key_vault.connect_key_vault(url)

        
        
        try:
            mod_azure_key_vault.list_secrets()
            SetVar(variable, True)
        except:
            SetVar(variable, False)
    
        

    if command == "get-secret":
        secret_name = GetParams("secret-name")
        variable = GetParams("variable")
        
        secrets = mod_azure_key_vault.get_secret(secret_name)
        SetVar(variable, secrets)   #con SetVar modifico una variable en Rocketbot para guardar el valor

    if command == "set-secret":
        secret_name = GetParams("secret-name")
        secret_value = GetParams("secret-value")

        set_secret = mod_azure_key_vault.set_secret(secret_name, secret_value)

    if command == "update-property-secret":
        secret_name = GetParams("secret-name")
        enable = GetParams("enable") or "None"
        content_type = GetParams("content-type")
        
        enable = eval(enable)
        args = {}
        if enable is not None:
            args["enable"] = enable
            
        if content_type is not None:
            args["content_type"] = content_type
        
        update = mod_azure_key_vault.update_property_secret(secret_name, **args)


    if command == "delete-secret":
        secret_name = GetParams("secret-name")

        delete = mod_azure_key_vault.delete_secret(secret_name)


except Exception as e:
    PrintException()#type:ignore
    print(traceback.format_exc())
    raise e