from os import path, getcwd
import subprocess
import re

import yaml

COMMAND_NAME = "flake8"
TEST_FILE_NAME = "test_script.py"
SAVE_FILE_NAME = "output"
TEST_FILE_PATH = path.join(getcwd(), TEST_FILE_NAME)


def save_yaml_file(file_name, data):
    with open(f'{file_name}.yaml', 'w') as f:
        yaml.dump(data, f)


if __name__ == '__main__':
    statistics_output = subprocess.run(f'{COMMAND_NAME} {TEST_FILE_PATH}', shell=True, stdout=subprocess.PIPE)
    statistics = statistics_output.stdout.decode("utf-8").splitlines()[:-1]  # remove StdOut color code as last element
    statistics = [message.split(' ', maxsplit=1)[1] for message in statistics]
    statistics = sorted([message.split(' ', maxsplit=1) for message in statistics],
                        key=lambda message: message[0])
    statistics = map(lambda message: [re.findall("[a-zA-Z]+", message[0])[0], message[0], message[1]],
                     statistics)
    last_message_code = None
    output_dict = dict()
    current_message_type_group = []
    for index, message in enumerate(statistics):
        if message[0] != last_message_code and len(current_message_type_group) != 0:
            output_dict[last_message_code] = current_message_type_group
            current_message_type_group = []
        print(f"{index}\t{message[1]}\t{message[2]}")
        current_message_type_group.append({message[1]: message[2]})
        last_message_code = message[0]
    output_dict[last_message_code] = current_message_type_group
    save_yaml_file(SAVE_FILE_NAME, output_dict)
