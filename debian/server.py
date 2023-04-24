# -*- coding: utf-8 -*-

import netaddr
from flask import Flask, request, render_template


app = Flask(__name__, template_folder='./')


@app.route('/<host>/<ip>')
@app.route('/<host>/<ip>/<prefix>')
def index(host, ip, prefix=24):
  addr = netaddr.IPNetwork(f'{ip}/{prefix}')
  params = {
    'host': host,
    'addr': addr,
    'gateway': addr.network+1,
  }
  return render_template('preseed.txt', **params), 200, {'Content-Type': 'text/plain; charset=utf-8'}


if __name__ == '__main__':
  app.run(debug=True, host='::', port=9090)
