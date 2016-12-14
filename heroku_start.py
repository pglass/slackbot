import os
import sys

from rtmbot import RtmBot
import yaml


def env_config():
    result = {}
    if 'SLACK_TOKEN' in os.environ:
        result['SLACK_TOKEN'] = os.environ['SLACK_TOKEN']
    return result


def file_config():
    return yaml.load(open('rtmbot.conf', 'r'))


def main():
    # environment values take precendence over values in the config file
    config = file_config()
    config.update(env_config())

    bot = RtmBot(config)
    try:
        bot.start()
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    main()
