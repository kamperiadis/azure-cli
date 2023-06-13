# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import os

DOTNET_TARGET_FRAMEWORK_REGEX = r"^net\d+\.\d+$"
NETCORE_RUNTIME_NAME = "dotnetcore"
ASPDOTNET_RUNTIME_NAME = "aspnet"
DOTNET_RUNTIME_NAME = "dotnet"
NODE_RUNTIME_NAME = "node"
PYTHON_RUNTIME_NAME = "python"
OS_DEFAULT = "Windows"
LINUX_OS_NAME = "linux"
WINDOWS_OS_NAME = "windows"
STATIC_RUNTIME_NAME = "static"  # not an official supported runtime but used for CLI logic
LINUX_SKU_DEFAULT = "P1V2"
FUNCTIONS_VERSIONS = ['2', '3', '4']
FUNCTIONS_LINUX_RUNTIME_VERSION_REGEX = r"^.*\|(.*)$"
FUNCTIONS_WINDOWS_RUNTIME_VERSION_REGEX = r"^~(.*)$"
FUNCTIONS_NO_V2_REGIONS = {
    "USNat West",
    "USNat East",
    "USSec West",
    "USSec East"
}
GITHUB_OAUTH_CLIENT_ID = "8d8e1f6000648c575489"
GITHUB_OAUTH_SCOPES = [
    "admin:repo_hook",
    "repo",
    "workflow"
]
LOGICAPP_KIND = "workflowapp"
FUNCTIONAPP_KIND = "functionapp"
DOTNET_REFERENCES_DIR_IN_ZIP = ".az-references"


class FUNCTIONS_STACKS_API_KEYS():
    # pylint:disable=too-few-public-methods,too-many-instance-attributes
    def __init__(self):
        self.NAME = 'name'
        self.VALUE = 'value'
        self.DISPLAY = 'display'
        self.PROPERTIES = 'properties'
        self.MAJOR_VERSIONS = 'majorVersions'
        self.DISPLAY_VERSION = 'displayVersion'
        self.RUNTIME_VERSION = 'runtimeVersion'
        self.IS_HIDDEN = 'isHidden'
        self.IS_PREVIEW = 'isPreview'
        self.IS_DEPRECATED = 'isDeprecated'
        self.IS_DEFAULT = 'isDefault'
        self.SITE_CONFIG_DICT = 'siteConfigPropertiesDictionary'
        self.APP_SETTINGS_DICT = 'appSettingsDictionary'
        self.LINUX_FX_VERSION = 'linuxFxVersion'
        self.APPLICATION_INSIGHTS = 'applicationInsights'
        self.SUPPORTED_EXTENSION_VERSIONS = 'supportedFunctionsExtensionVersions'
        self.USE_32_BIT_WORKER_PROC = 'use32BitWorkerProcess'
        self.FUNCTIONS_WORKER_RUNTIME = 'FUNCTIONS_WORKER_RUNTIME'
        self.GIT_HUB_ACTION_SETTINGS = 'git_hub_action_settings'


GENERATE_RANDOM_APP_NAMES = os.path.abspath(os.path.join(os.path.abspath(__file__),
                                                         '../resources/GenerateRandomAppNames.json'))

PUBLIC_CLOUD = "AzureCloud"

LINUX_GITHUB_ACTIONS_WORKFLOW_TEMPLATE_PATH = {
    'node': 'AppService/linux/nodejs-webapp-on-azure.yml',
    'python': 'AppService/linux/python-webapp-on-azure.yml',
    'dotnetcore': 'AppService/linux/aspnet-core-webapp-on-azure.yml',
    'java': 'AppService/linux/java-jar-webapp-on-azure.yml',
    'tomcat': 'AppService/linux/java-war-webapp-on-azure.yml'
}

WINDOWS_GITHUB_ACTIONS_WORKFLOW_TEMPLATE_PATH = {
    'node': 'AppService/windows/nodejs-webapp-on-azure.yml',
    'python': 'AppService/windows/python-webapp-on-azure.yml',
    'dotnetcore': 'AppService/windows/aspnet-core-webapp-on-azure.yml',
    'java': 'AppService/windows/java-jar-webapp-on-azure.yml',
    'tomcat': 'AppService/windows/java-war-webapp-on-azure.yml'
}

LINUX_FUNCTIONAPP_GITHUB_ACTIONS_WORKFLOW_TEMPLATE_PATH = {
    'node': 'FunctionApp/linux-node.js-functionapp-on-azure.yml',
    'python': 'FunctionApp/linux-python-functionapp-on-azure.yml',
    'dotnet': 'FunctionApp/linux-dotnet-functionapp-on-azure.yml',
    'java': 'FunctionApp/linux-java-functionapp-on-azure.yml',
    'powershell': 'FunctionApp/linux-powershell-functionapp-on-azure.yml',
}

WINDOWS_FUNCTIONAPP_GITHUB_ACTIONS_WORKFLOW_TEMPLATE_PATH = {
    'node': 'FunctionApp/windows-node.js-functionapp-on-azure.yml',
    'dotnet': 'FunctionApp/windows-dotnet-functionapp-on-azure.yml',
    'java': 'FunctionApp/windows-java-functionapp-on-azure.yml',
    'powershell': 'FunctionApp/windows-powershell-functionapp-on-azure.yml',
}

DEFAULT_CENTAURI_IMAGE = 'mcr.microsoft.com/azure-functions/dotnet7-quickstart-demo:1.0'
ACR_IMAGE_SUFFIX = ".azurecr.io"

FLEX_RUNTIMES = [
    {
        'runtime': 'dotnet',
        'version': '6',
        'site_config': {
            'use32_bit_worker_process': True,
            'linux_fx_version': 'DOTNET|6.0',
        },
        'app_settings': {
            'FUNCTIONS_WORKER_RUNTIME': 'dotnet'
        }
    },
    {
        'runtime': 'java',
        'version': '17.0',
        'site_config': {
            'use32_bit_worker_process': False,
            'linux_fx_version': 'Java|17',
        },
        'app_settings': {
            'FUNCTIONS_WORKER_RUNTIME': 'java'
        }
    },
    {
        'runtime': 'node',
        'version': '18',
        'site_config': {
            'use32_bit_worker_process': False,
            'linux_fx_version': 'Node|18'
        },
        'app_settings': {
            'FUNCTIONS_WORKER_RUNTIME': 'node'
        }
    },
    {
        'runtime': 'python',
        'version': '3.10',
        'site_config': {
            'use32_bit_worker_process': False,
            'linux_fx_version': 'Python|3.10'
        },
        'app_settings': {
            'FUNCTIONS_WORKER_RUNTIME': 'python'
        }
    },
    {
        'runtime': 'powershell',
        'version': '7.2',
        'site_config': {
            'use32_bit_worker_process': False,
            'linux_fx_version': 'PowerShell|7.2'
        },
        'app_settings': {
            'FUNCTIONS_WORKER_RUNTIME': 'powershell'
        }
    }
]

STAMP_NAME = 'kc11geo.eastus.cloudapp.azure.com'
