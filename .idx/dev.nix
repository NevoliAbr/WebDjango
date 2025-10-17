{ pkgs, ... }: {
  # Let Nix handle Python, Poetry, and their dependencies
  # For more details, see https://developer.hashicorp.com/waypoint/tutorials/nix/nix-language
  packages = [
    pkgs.python3
    pkgs.python3Packages.venvShellHook
  ];
  env = {
    FLASK_APP = "app.py";
    FLASK_DEBUG = "1";
    LC_ALL = "C.UTF-8";
    LANG = "C.UTF-8";
  };

  # The Go, Node.js, and Python language servers are currently builtin.
  # See https://www.jetpack.io/devbox/docs/ide_configuration/
  languages.python.enable = true;

  # To run a command whenever the environment is created or updated, use the
  # 'scripts.update.exec' attribute.
  # For more details, see https://www.jetpack.io/devbox/docs/configuration/
  scripts.update.exec = "python -m venv .venv && .venv/bin/pip install -r requirements.txt";

  # To run a command when the project is first created, use the
  # 'scripts.create.exec' attribute.
  # For more details, see https://www.jetpack.io/devbox/docs/configuration/
  scripts.create.exec = "echo 'Hello, World!'";

  # Service to start MongoDB on workspace open is now disabled
  # services.mongodb.enable = true;
}
