#
#  Copyright (C) 2016 Codethink Limited
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	 See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library. If not, see <http://www.gnu.org/licenses/>.
#
#  Authors:
#        Tristan Van Berkom <tristan.vanberkom@codethink.co.uk>

"""
modulebuild - Perl Module::Build build element
==============================================
A :mod:`BuildElement <buildstream.buildelement>` implementation for using
the Perl Module::Build build system

The modulebuild default configuration:
  .. literalinclude:: ../../../buildstream/plugins/elements/modulebuild.yaml
     :language: yaml
"""

from buildstream import BuildElement


# Element implementation for the 'modulebuild' kind.
class ModuleBuildElement(BuildElement):
    pass


# Plugin entry point
def setup():
    return ModuleBuildElement
