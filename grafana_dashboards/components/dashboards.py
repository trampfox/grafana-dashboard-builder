# -*- coding: utf-8 -*-
# Copyright 2015 grafana-dashboard-builder contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from grafana_dashboards.components.base import JsonGenerator, get_component_type
from grafana_dashboards.components.rows import Rows
from grafana_dashboards.components.templates import Templates

__author__ = 'Jakub Plichta <jakub.plichta@gmail.com>'


class Dashboard(JsonGenerator):
    def gen_json_from_data(self, data, context):
        nav = {
            'type': 'timepicker'
        }
        json_data = {
            'title': data.get('title', self.name),
            'nav': [
                nav
            ]
        }
        if 'time' in data:
            json_data['time'] = {
                'from': data['time']['from'],
                'to': data['time']['to']
            }
        if 'tags' in data:
            json_data['tags'] = data.get('tags')
        if 'time_options' in data:
            nav['time_options'] = data.get('time_options', [])
        if 'refresh_intervals' in data:
            nav['refresh_intervals'] = data.get('refresh_intervals', [])
        if get_component_type(Rows) in data:
            json_data['rows'] = Rows(data, self.registry).gen_json()
        if get_component_type(Templates) in data:
            json_data['templating'] = {
                'list': Templates(data, self.registry).gen_json(),
                'enable': True
            }
        return json_data