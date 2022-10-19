import subprocess

import yaml

from logger import logger


def get_command_from_data(data: dict):
    server = data["server"]
    user = data["user"]
    password = data["password"]
    forwards = data["forwards"]
    command_forward_part = [
        '-R {server_port}:{local_ip}:{local_port}'.format(
            server_port=forward["server-port"],
            local_ip=forward["local-ip"],
            local_port=forward["local-port"],
        ) for forward in forwards
    ]
    command = ["sshpass", "-p", password,
               "ssh", "-o StrictHostKeyChecking=no"] + command_forward_part + ["-N", f"{user}@{server}"]
    return command


def forward_ports(data: dict):
    while True:
        logger.info("Connecting to server...")
        process = subprocess.Popen(get_command_from_data(data),
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   universal_newlines=True,
                                   bufsize=0)
        with process.stderr:
            logger.error(f"Process error: {process.stderr.read().rstrip()}")
        with process.stdout:
            logger.info(f"Process output: {process.stdout.read().rstrip()}")


def main():
    logger.info("Starting app...")
    stream = open("config.yaml", 'r')
    data = yaml.safe_load(stream)
    logger.info("Read config")
    forward_ports(data)


if __name__ == '__main__':
    main()
