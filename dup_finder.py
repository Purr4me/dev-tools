#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Duplicate masterlist entry finder.
# Finds plugins which have more than one entry in the masterlist. Entries do
# not need to be identical.

#   LOOT
#
#   A load order optimisation tool for Oblivion, Skyrim, Fallout 3 and
#   Fallout: New Vegas.
#
#   Copyright (C) 2014    WrinklyNinja
#
#   This file is part of LOOT.
#
#   LOOT is free software: you can redistribute
#   it and/or modify it under the terms of the GNU General Public License
#   as published by the Free Software Foundation, either version 3 of
#   the License, or (at your option) any later version.
#
#   LOOT is distributed in the hope that it will
#   be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with LOOT.  If not, see
#   <http://www.gnu.org/licenses/>.

import os
import codecs

mlist_parent_path = u'../../falloutnv'

with codecs.open(os.path.join(mlist_parent_path, u'masterlist.yaml'), 'r', encoding='utf-8') as mlist:
    name_set = set()
    dups = set()
    for line in mlist:
        if line.startswith(u'  - name: '):
            if line in name_set:
                dups.add(line)
            else:
                name_set.add(line)
    for name in dups:
        print name
