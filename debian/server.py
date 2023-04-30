# -*- coding: utf-8 -*-

import netaddr
from flask import Flask, request, render_template, redirect

app = Flask(__name__, template_folder='./')

packages = [
  'qemu-guest-agent',
  'openssh-server',
  'ca-certificates', 'bash-completion',
  'file', 'sudo', 'rsync', 'ncdu', 'htop', 'iptables', 'xfsprogs', 'psmisc', 'sysstat', 'apparmor', 'apparmor-utils', 'bsdmainutils', 'fuse',
  'vim', 'wget', 'curl', 'unzip', 'netcat', 'net-tools',
  'git', 'git-extras',
  'ethtool', 'telnet', 'traceroute', 'tcpdump', 'iputils-ping',
  'build-essential', 'python3-dev', 'python3-venv', 'python3-pip',
  'dnsutils', 'openvpn', 'cifs-utils', 'nfs-common', 'gnupg',
]

@app.route('/favicon.ico')
def favicon():
  return redirect('https://www.debian.org/favicon.ico', code=302)

@app.route('/<host>/<ip>')
@app.route('/<host>/<ip>/<prefix>')
def index(host, ip, prefix=24):
  addr = netaddr.IPNetwork(f'{ip}/{prefix}')
  params = {
    'host': host,
    'addr': addr,
    'gateway': addr.network+1,
    'packages': ' '.join(packages),
  }
  return render_template('preseed.txt', **params), 200, {'Content-Type': 'text/plain; charset=utf-8'}


if __name__ == '__main__':
  app.run(debug=True, host='::', port=9090)
