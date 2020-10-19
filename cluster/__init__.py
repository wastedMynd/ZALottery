# read cluster setup properties
import os
import yaml
from __init__ import Logging

logger = Logging().get_logger()


@Logging
def get_cluster_properties(cluster_properties_file_yaml=None):
    if cluster_properties_file_yaml is None:

        docker_path = os.environ.get("APP_MONGO_DB_PATH")
        print(f"{docker_path=}")

        base_path = "/home/sizwe/PycharmProjects/ZALotteryPythonProject/cluster/"
        print(f"{base_path=}")

        cluster_properties_file_yaml = os.path.join(
            base_path if docker_path is None else docker_path,
            'cluster_properties.yaml'
        )
        print(f"{cluster_properties_file_yaml=}")

    if not os.path.exists(cluster_properties_file_yaml):
        logger.critical(f"Settings yaml file {cluster_properties_file_yaml} does not exist!!!")
        return None

    try:
        with open(cluster_properties_file_yaml, 'r') as yaml_stream:
            return yaml.load(yaml_stream, Loader=yaml.SafeLoader)
    except:
        logger.critical(f"Cannot read yaml config file {cluster_properties_file_yaml}, check formatting.")
        return None


@Logging
def get_cluster_url(cluster_properties_file_yaml=None) -> str:
    # get cluster properties
    properties = get_cluster_properties(cluster_properties_file_yaml)
    url = str(properties.get("cluster")["url"]).format(
        properties.get("user")["name"],
        properties.get("user")["password"],
        properties.get("cluster")["database_draw"]
    )
    print(f"{url=}")
    return url


if __name__ == '__main__':
    print(get_cluster_url())
