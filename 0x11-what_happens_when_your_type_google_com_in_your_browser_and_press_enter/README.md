this is  project on what happen when something is searched on google.com
# What Happens When You Type "google.com" and Press Enter

This document explains the steps that occur when you type "google.com" into your browser's address bar and press Enter. The process involves several key components and protocols to deliver the Google homepage to your browser.

## DNS Request

1. **URL Parsing:**
   - The browser parses the URL to extract the domain name "google.com."

2. **DNS Resolution:**
   - The browser checks its cache for the IP address of "google.com."
   - If not found, it queries the operating system's DNS resolver cache.
   - If still not found, a DNS query is sent to the configured DNS server.
   - The DNS server resolves "google.com" to an IP address (e.g., 172.217.15.110).

## TCP/IP

3. **TCP Connection:**
   - Using the resolved IP address, the browser initiates a TCP connection to the Google server.
   - This involves a three-way handshake:
     - The browser sends a SYN (synchronize) packet.
     - The server responds with a SYN-ACK (synchronize-acknowledge) packet.
     - The browser sends an ACK (acknowledge) packet.

## Firewall

4. **Firewall Checks:**
   - Both client-side and serv


