## Ansible Collection: Steam CLI

This Ansible collection provides a set of tasks to interact with the Steam on Windows systems. It allows for the installation and uninstallation of Steam applications.

### Requirements

- Ansible 2.9 or later
- PowerShell 6.2 or later
- Ansible Basic module

### Installation

To install the requirements for an Ansible playbook, you can use the `ansible-galaxy` command with the `install` option. The `ansible-galaxy` command is a command-line tool that manages Ansible roles and collections.

Here are the steps to install the requirements for a playbook:

1. Create a file named `requirements.yml` in your playbook directory (if it doesn't already exist).
2. Inside the `requirements.yml` file, specify the dependencies of your playbook. For example, if your playbook depends on a specific Ansible role or collection, you can define it in the following format:

   ```yaml
   ---
   collections:
     - xxninjabunnyxx.steam_cli
   ```

3. Run the following command to install the requirements:

   ```shell
   ansible-galaxy install -r requirements.yml
   ```

   This command will read the `requirements.yml` file and install the specified collections and roles.

   If you have already installed some of the requirements, the command will skip those and only install the missing dependencies.

   By installing the requirements, you ensure that all the necessary roles and collections are available for your playbook to run successfully.

### Usage

#### Task Options

The Steam CLI collection provides a single task `windows` with the following options:

- `id` (required): The ID of the Steam application to install or uninstall.
- `directory` (required): The directory where the Steam CLI tool is located.
- `present` (optional, default: `true`): Determines whether to install (`true`) or uninstall (`false`) the specified Steam application.

#### Playbook Example

```yaml
- name: Test Steam CLI Collection
  hosts: win
  collections:
    - xxninjabunnyxx.steam_cli
  vars:
    steam_path: "C:\\Program Files (x86)\\Steam\\steamcmd.exe"
  tasks:
    - name: Install Windows Version of Blue Revolver
      windows:
        id: 439490
        directory: "{{ steam_path }}"
        present: true

    - name: Install Windows Version of DoDonPachi Resurrection
      windows:
        id: 464450
        directory: "{{ steam_path }}"
        present: true
```

This playbook demonstrates how to use the `windows` task to install two Steam applications, "Blue Revolver" and "DoDonPachi Resurrection", on Windows hosts. The `steam_path` variable specifies the directory where the Steam is located.

### License

This Ansible collection is licensed under the [MIT License](https://opensource.org/licenses/MIT).

### Support

For any issues or questions regarding this Ansible collection, please open an issue on the [GitHub repository](https://github.com/xxninjabunnyxx/steam-cli-ansible-collection/issues).

### Author

This Ansible collection was created by xxninjabunnyxx.