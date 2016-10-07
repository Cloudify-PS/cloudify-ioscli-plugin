# Copyright (c) 2016 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from setuptools import setup

setup(
    name='cloudify-ioscli-plugin',
    version='0.1',
    description='support ioncli',
    author='Denis Pauk',
    author_email='pauk.denis@gmail.com',
    license='LICENSE',
    packages=['cloudify_ioscli'],
    install_requires=[
        'cloudify-plugins-common>=3.3',
        'paramiko',  # for ssh connection
    ],
)
