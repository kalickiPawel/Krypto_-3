import logging.config
import logging
import yaml

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger_setup = logging.getLogger(__name__)
