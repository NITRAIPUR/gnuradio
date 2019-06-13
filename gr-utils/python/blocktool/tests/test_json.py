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
""" testing the JSON files generated by gr-blocktool """

from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import os
import sys
import json
import jsonschema

from jsonschema import validate


# Schema to be strictly followed be every output json file
JSON_SCHEME = {
    "title": "JSON SCHEMA TO BE FOLLOWED BY BLOCK HEADER PARSING TOOL",
    "description": "Schema designed for the header file json output",
    "type": "object",
    "properties": {
        "namespace": {
            "description": "List of nested namspaces",
            "type": "array",
            "minItems": 1,
            "uniqueItems": True,
            "items": {
                "type": "string",
                "minLength": 1
            }
        },
        "class": {
            "description": "Class name",
            "type": "string",
            "minLength": 1
        },
        "io_signature": {
            "description": "I/O signature",
            "type": "object",
            "properties": {
                "in_port": {
                    "description": "Input ports",
                    "type": "object"
                },
                "out_port": {
                    "description": "Output ports",
                    "type": "object"
                }
            }
        },
        "make": {
            "description": "Make function",
            "type": "object",
            "properties": {
                "arguments": {
                    "description": "Arguments of make function",
                    "type": "array",
                    "minItems": 1,
                    "uniqueItems": True,
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "minLength": 1
                            },
                            "dtype": {
                                "type": "string",
                                "minLength": 1
                            },
                            "default": {
                                "type": "string"
                            }
                        },
                        "required": ["name"],
                        "dependencies": {
                            "name": [
                                "dtype",
                                "default"
                            ]
                        }
                    }
                }
            }
        },
        "properties": {
            "description": "Getters",
            "type": "array",
            "uniqueItems": True,
            "items": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "minLength": 1
                    },
                    "dtype": {
                        "type": "string",
                        "minLength": 1
                    },
                    "read_only": {
                        "type": "boolean"
                    }
                },
                "required": ["name"],
                "dependencies": {
                    "name": [
                        "dtype",
                        "read_only"
                    ]
                }
            }
        },
        "methods": {
            "description": "Setters",
            "type": "array",
            "minItems": 0,
            "items": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "minLength": 1
                    },
                    "arguments_type": {
                        "type": "array",
                        "uniqueItems": True,
                        "properties": {
                            "name": {
                                "type": "string",
                                "minLength": 1
                            },
                            "dtype": {
                                "type": "string",
                                "minLength": 1
                            }
                        },
                        "required": ["name"],
                        "dependencies": {
                            "name": ["dtype"]
                        }
                    }
                },
                "required": ["name"]
            }
        }
    },
    "required": [
        "namespace",
        "class",
        "io_signature",
        "make",
        "properties",
        "methods"
    ]
}


def is_valid():
    """ Validate json file """
    filename = sys.argv[1]
    if(filename.split(".")[-1] != "json"):
        raise Exception("Please input file with json format only")
    else:
        with open(filename, 'r') as f:
            data = json.load(f)
        try:
            print("Validating...")
            jsonschema.validate(data, JSON_SCHEME)
        except jsonschema.ValidationError as ve:
            print("Record JSON file # {}: NOT OK".format(filename))
            raise Exception(ve+"\n")
        else:
            print("Record JSON file # {}: OK".format(filename))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        is_valid()
    else:
        raise Exception('Please input only one json file')
