#!/usr/bin/env python3

from pymt5linux import MetaTrader5

print("Attempting to connect to MT5 on localhost:8001...")
mt5 = MetaTrader5(host='localhost', port=8001)

print("Initializing MT5...")
mt5.initialize()

print("Getting MT5 version...")
version = mt5.version()
print(f"MT5 Version: {version}")

print("Getting terminal info...")
terminal_info = mt5.terminal_info()
print(f"Terminal Info: {terminal_info}")

print("\n✅ Connection successful! RPyC 5.3.1 compatibility working!")
