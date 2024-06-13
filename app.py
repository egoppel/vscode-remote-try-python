#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved. ( ff code aanpassen vor versie 4)
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")
