import subprocess as ps
import re
import sys


def get_docker_image_table() -> str:
    images_table = ps.run(["sudo", "docker", "image", "ls"], capture_output=True)
    return images_table.stdout.decode()


def execute_docker_image_removal():
    ps.run(["echo", "stopping docker service"])
    ps.run("sudo service docker stop", shell=True)
    print()

    ps.run(["echo", "starting docker service"])
    ps.run(["sudo", "service", "docker", "start"])
    print()

    ps.run(["echo", "getting docker images"])
    print(docker_image_table := get_docker_image_table())
    print()

    ps.run(["echo", "initializing docker image removal process..."])
    rows = docker_image_table.split("\n")

    for index in range(1, len(rows)):
        row = rows[index].strip()

        data = re.split(r"\s+", row)

        try:
            # repository = data[0]
            # tag = data[1].strip()
            image_id = data[2].strip()
            # created = f"{data[3].strip()} {data[4].strip()} {data[5].strip()}"
            # size = data[6].strip()

            remove_image(image_id)
        except IndexError:
            sys.stderr.write(row)

    ps.run(["echo", "docker image removal, process is complete!"])
    print()

    ps.run(["echo", "remaining docker image(s)!"])
    print(get_docker_image_table())


def remove_image(image):
    ps.run(["sudo ", "docker ", "stop ", image])
    ps.run(["sudo ", "docker ", "rmi ", "-f ", image])


if __name__ == '__main__':
    execute_docker_image_removal()
