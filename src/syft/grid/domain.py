"""The purpose of this application is to allow us to dev and test PySyft
functionality on an actual local network. This is NOT meant to be run in
production (that's the *actual* grid's job)."""

import binascii
import pickle

from flask import Flask, request

from syft.core.common.message import (
    ImmediateSyftMessageWithoutReply,
    ImmediateSyftMessageWithReply,
)
from syft.core.node.domain.domain import Domain

app = Flask(__name__)


domain = Domain(name="ucsf")


@app.route("/")
def get_client():

    client_metadata = domain.get_metadata_for_client()
    return pickle.dumps(client_metadata).hex()


@app.route("/recv", methods=["POST"])
def recv():
    hex_msg = request.get_json()["data"]
    msg = pickle.loads(binascii.unhexlify(hex_msg))  # nosec # TODO make less insecure
    reply = None
    print(str(msg))
    if isinstance(msg, ImmediateSyftMessageWithReply):
        reply = domain.recv_immediate_msg_with_reply(msg=msg)
        return {"data": pickle.dumps(reply).hex()}
    elif isinstance(msg, ImmediateSyftMessageWithoutReply):
        domain.recv_immediate_msg_without_reply(msg=msg)
    else:
        domain.recv_eventual_msg_without_reply(msg=msg)

    return str(msg)


def run():
    app.run()
