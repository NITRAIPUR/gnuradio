#
# Copyright 2019 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#
""" Module to add new blocks """

from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import re
import click

from parser.core import ParserGenerateAst
from parser.cli import run, cli_input, ParserException

@click.command('generate_ast')
@click.option('--module_type', type=click.Choice(ParserGenerateAst.module_types),
              help="One of {}.".format(', '.join(ParserGenerateAst.module_types)))
def cli(**kwargs):
    """Select a GNU Radio Module."""
    kwargs['cli'] = True
    # self = ParserGenerateAst(**kwargs)

if __name__ == '__main__':
    cli()