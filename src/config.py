import yaml


def load_config():
    """
    Load configuration from config/config.yaml
    """

    with open("config/config.yaml", "r") as file:
        config = yaml.safe_load(file)

    return config