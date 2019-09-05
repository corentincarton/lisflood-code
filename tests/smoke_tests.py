"""

Copyright 2019 European Union

Licensed under the EUPL, Version 1.2 or as soon they will be approved by the European Commission  subsequent versions of the EUPL (the "Licence");

You may not use this work except in compliance with the Licence.
You may obtain a copy of the Licence at:

https://joinup.ec.europa.eu/sites/default/files/inline-files/EUPL%20v1_2%20EN(1).txt

Unless required by applicable law or agreed to in writing, software distributed under the Licence is distributed on an "AS IS" basis,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the Licence for the specific language governing permissions and limitations under the Licence.

"""
from __future__ import absolute_import, print_function, division

import os

from tests import TestLis

current_dir = os.path.dirname(os.path.abspath(__file__))


class TestCatch1(TestLis):
    settings_path = os.path.join(current_dir, 'data/TestCatchment1/settings/cold_day_base.xml')

    def test_dis(self):
        return self.listest('dis_1')


class TestCatch2(TestLis):
    settings_path = os.path.join(current_dir, 'data/TestCatchment2/settings/prerun.xml')

    def test_dis(self):
        return self.listest('dis_2')
