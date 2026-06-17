import argparse
from azure.identity import InteractiveBrowserCredential, AzureCliCredential
from fabric_cicd import FabricWorkspace, publish_all_items

parser = argparse.ArgumentParser(description="Deploy PBIP to Fabric")
parser.add_argument("--workspace_name", type=str, required=False, help="Target workspace name", default="PBIP Fabric CICD Dev")
parser.add_argument("--environment", type=str, default="dev", help="Environment name")
parser.add_argument("--spn-auth", action="store_true", help="Use SPN authentication via Azure CLI")
args = parser.parse_args()

if not args.spn_auth:
    credential = InteractiveBrowserCredential()
else:
    credential = AzureCliCredential()

workspace_params = {
    "workspace_name": args.workspace_name,
    "environment": args.environment,
    "repository_directory": ".",
    "item_type_in_scope": ["SemanticModel", "Report"],
    "token_credential": credential,
}

target_workspace = FabricWorkspace(**workspace_params)
publish_all_items(target_workspace)