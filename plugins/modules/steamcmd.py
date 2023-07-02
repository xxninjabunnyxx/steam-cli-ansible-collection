from ansible.module_utils.basic import AnsibleModule
import subprocess
import os

os_override = {
    "windows": "windows",
    "linux": "linux",
    "macos": "macos",
}

def run_steam_cmd(module):
    cmd = ['steamcmd']

    if module.params['os_override'] != os_override["windows"] and module.params['os_override'] != os_override["linux"] and module.params['os_override'] != os_override["macos"]:
        return "Invalid os_override value"

    if module.params['os_override'] == os_override["windows"]:
        cmd.append(f"+@sSteamCmdForcePlatformType windows")

    if module.params['os_override'] == os_override["linux"]:
        cmd.append(f"+@sSteamCmdForcePlatformType linux")

    if module.params['os_override'] == os_override["macos"]:
        cmd.append(f"+@sSteamCmdForcePlatformType macos")

    if module.params['os_override'] != os_override["windows"] and module.params['server'] == False:
        return "SteamCMD can only be used to install non server applications on Windows"
    elif module.params['server'] == True:
        cmd.append(f"+force_install_dir {os.path.join(module.params['directory'], module.params['folder_name'])}")
    else:
        cmd.append(f"+force_install_dir {os.path.join(module.params['directory'], 'steamapps', 'common', module.params['folder_name'])}")

    cmd.append(f"+login {module.params['username']}")

    if module.params['present'] == True:
        cmd.append(f"+app_update {module.params['id']}")
        cmd.append(f"validate")
    else:
        cmd.append(f"+app_uninstall {module.params['id']}")

    cmd.append(f"+quit")

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    return stdout.decode()


def main():
    playbook_args = {
        "id": {"type": "str", "required": True},
        "directory": {"type": "str", "required": True},
        "username": {"type": "str", "required": True},
        "folder_name": {"type": "str", "required": True},
        "os_override": {"type": "str", "required": False, "default": os_override["windows"]},
        "present": {"type": "bool", "required": False, "default": True},
        "server": {"type": "bool", "required": False, "default": False},
    }

    module = AnsibleModule(argument_spec=playbook_args)

    stdout = run_steam_cmd(module)

    module.exit_json(changed=True, stdout=stdout)


if __name__ == '__main__':
    main()
