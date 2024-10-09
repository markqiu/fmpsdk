from dynaconf import Dynaconf

settings = Dynaconf(
    root_path="/Users/qiucheng/PycharmProjects/fmpsdk",
    settings_files=["settings.toml"],
)

# `envvar_prefix` = export envvars with `export FMPCONF_FOO=bar`.
# `settings_files` = Load these files in the order.
