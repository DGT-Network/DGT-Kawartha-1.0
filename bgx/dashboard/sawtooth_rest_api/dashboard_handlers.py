# Copyright 2016, 2017 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------

import asyncio
import re
import logging
import json
import base64
import hashlib
import random
import os
from aiohttp import web

# pylint: disable=no-name-in-module,import-error
# needed for the google.protobuf imports to pass pylint
from google.protobuf.json_format import MessageToDict
from google.protobuf.message import DecodeError

from sawtooth_rest_api.protobuf.validator_pb2 import Message

import sawtooth_rest_api.exceptions as errors
from sawtooth_rest_api import error_handlers
from sawtooth_rest_api.messaging import DisconnectError
from sawtooth_rest_api.messaging import SendBackoffTimeoutError
from sawtooth_rest_api.protobuf import client_transaction_pb2
from sawtooth_rest_api.protobuf import client_list_control_pb2
from sawtooth_rest_api.protobuf import client_batch_submit_pb2
from sawtooth_rest_api.protobuf import client_state_pb2
from sawtooth_rest_api.protobuf import client_block_pb2
from sawtooth_rest_api.protobuf import client_batch_pb2
from sawtooth_rest_api.protobuf import client_receipt_pb2
from sawtooth_rest_api.protobuf import client_peers_pb2
from sawtooth_rest_api.protobuf import client_status_pb2
from sawtooth_rest_api.protobuf.block_pb2 import BlockHeader
from sawtooth_rest_api.protobuf.batch_pb2 import Batch,BatchHeader,BatchList
from sawtooth_rest_api.protobuf.transaction_pb2 import Transaction,TransactionHeader

from sawtooth_rest_api.route_handlers import RouteHandler,DEFAULT_TIMEOUT

#from sawtooth_signing.secp256k1 import Secp256k1PrivateKey, Secp256k1PublicKey, Secp256k1Context
#from sawtooth_signing import CryptoFactory,create_context


LOGGER = logging.getLogger(__name__)
ROOT = os.path.dirname(__file__)

class DashboardRouteHandler(RouteHandler):
    """Contains a number of aiohttp handlers for endpoints in the Rest Api.

    Args:
        connection (:obj: messaging.Connection): The object that communicates
            with the validator.
        timeout (int, optional): The time in seconds before the Api should
            cancel a request and report that the validator is unavailable.
    """

    def __init__(self, loop, connection,timeout=DEFAULT_TIMEOUT, metrics_registry=None):

        super().__init__(loop,connection,timeout,metrics_registry)
        # Dashboard init
        LOGGER.debug('DashboardRouteHandler: _done')

    async def index(self,request):
        LOGGER.debug('DashboardRouteHandler: index')
        content = open(os.path.join(ROOT, 'app/html/index.html'), 'r').read()
        return web.Response(content_type='text/html', text=content)

    async def javascript(self,request):
        LOGGER.debug('DashboardRouteHandler: javascript=%s',request.path)
        content = open(os.path.join(ROOT,'app/js/'+request.path[1:]), 'r', encoding='utf-8').read()
        return web.Response(content_type='application/javascript', text=content)