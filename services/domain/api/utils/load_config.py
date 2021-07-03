import os
import yaml
import re


def load_config(config_path=None, tag="!ENV"):
    # pattern for global vars: look for ${word}
    pattern = re.compile(".*?\\${(\\w+)}.*?")
    loader = yaml.SafeLoader

    # the tag will be used to mark where to start searching for the pattern
    # e.g. somekey: !ENV somestring${MYENVVAR}blah blah blah
    loader.add_implicit_resolver(tag, pattern, None)

    def constructor_env_variables(loader, node):
        value = loader.construct_scalar(node)
        match = pattern.findall(value)  # to find all env variables in line
        if match:
            full_value = value
            for g in match:
                full_value = full_value.replace(f"${{{g}}}", os.environ.get(g, ""))
            return full_value
        return value

    loader.add_constructor(tag, constructor_env_variables)

    if config_path:
        with open(config_path) as config_data:
            return yaml.load(config_data, Loader=loader)
    else:
        raise ValueError("Either a path or data should be defined as input")
