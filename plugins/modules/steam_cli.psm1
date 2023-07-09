#Requires -Module Ansible.ModuleUtils.Legacy
#AnsibleRequires -OSVersion 6.2
#AnsibleRequires -CSharpUtil Ansible.Basic

$spec = @{
    options = @{
        id = @{ "type" = "str"; "required" = $True }
        directory = @{ "type" = "str"; "required" = $True }
        present = @{ "type" = "bool"; "required" = $False; "default" = $True }
    }
}

$module = [Ansible.Basic.AnsibleModule]::Create($args, $spec)

if ($module.Params.present -eq $True) {
    Start-Process -FilePath "$($module.Params.directory)\steam.exe" -ArgumentList "+app_install $($module.Params.id)"
} else {
    Start-Process -FilePath "$($module.Params.directory)\steam.exe" -ArgumentList "+app_uninstall $($module.Params.id)"
}

$module.ExitJson()
