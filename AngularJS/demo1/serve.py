# encoding: utf8
import os
import logging
logging.basicConfig(level=logging.INFO)
import json
from datetime import datetime, date

import yaml
import requests
from flask import make_response, jsonify, render_template, escape
from flask import url_for, abort, redirect
from flask import Flask, request, session, Response


conf = yaml.load(open('conf.yaml').read())
app = Flask('AngularJS')


@app.route('/')
def index():
    return app.send_static_file('demo.html')


@app.route('/table/prev')
def table_prev():
    page_no = int(request.args.get('page_no', '1')) - 1
    data = [{'index': i + 1, 'data': i ** i} for i in range(page_no)]
    return jsonify({'data': data})


@app.route('/table/next')
def table_next():
    page_no = int(request.args.get('page_no', '1')) + 1
    data = [{'index': i + 1, 'data': i ** i} for i in range(page_no)]
    return jsonify({'data': data})


if __name__ == "__main__":
    logging.info('server on port %s' % conf['port'])
    app.run(host='0.0.0.0', port=conf['port'], debug=conf['debug'])
