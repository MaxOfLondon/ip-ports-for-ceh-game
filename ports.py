ports = [
    ('tcp', 7, 'echo', ''),
    ('tcp', 9, 'discard', 'sink null'),
    ('tcp', 11, 'systat', 'Users'),
    ('tcp', 13, 'daytime', ''),
    ('tcp', 15, 'netstat', ''),
    ('tcp', 17, 'qotd', 'Quote'),
    ('tcp', 19, 'chargen', 'ttytst source'),
    ('tcp', 20, 'ftp-data', 'ftp data transfer'),
    ('tcp', 21, 'FTP', 'FTP command, like Telnet, is another insecure protocol which should die. Even with anonymous FTP (avoiding the authentication sniffing worry), data transfer is still subject to tampering.'),
    ('tcp', 22, 'SSH', 'Secure Shell, an encrypted replacement for Telnet (and, in some cases, FTP).'),
    ('tcp', 23, 'Telnet', 'Telnet lives on (particularly as an administration port on devices such as routers and smart switches) even though it is insecure (unencrypted).'),
    ('tcp', 25, 'SMTP', 'Simple Mail Transfer Protocol (also insecure).'),
    ('tcp', 37, 'time', 'Timeserver'),
    ('tcp', 43, 'nickname', 'who is'),
    ('tcp', 53, 'Domain', 'Domain Name System (DNS), an insecure system for conversion between host/domain names and IP addresses.'),
    ('tcp', 66, 'sql*net', 'Oracle SQL*net'),
    ('tcp', 67, 'bootps', 'bootp server. Dynamic Host Configuration Protocol Server (gives out IP addresses to clients when they join the network).'),
    ('tcp', 68, 'bootpc', 'bootp client. DHCP client port.'),
    ('tcp', 69, 'tftp', 'Trivial File Transfer Protocol.'),
    ('tcp', 70, 'gopher', 'gopher server'),
    ('tcp', 80, 'HTTP', 'Web server. This accounts for more than 14% of the open ports.'),
    ('tcp', 88, 'kerberos', 'Kerberos'),
    ('tcp', 109, 'pop2', 'Post Office Protocol version 2 for email retrieval (insecure).'),
    ('tcp', 110, 'POP3', 'Post Office Protocol version 3 for email retrieval (insecure).'),
    ('tcp', 111, 'RPCBind/sunrpc', 'Maps SunRPC program numbers to their current TCP or UDP port numbers.'),
    ('tcp', 113, 'auth/ident', 'authentication service'),
    ('tcp', 114, 'audionews', 'Audio News Multicast'),
    ('tcp', 119, 'nntp', 'Usanet Network News Transfer'),
    ('tcp', 123, 'ntp', 'Network Time Protocol.'),
    ('tcp', 135, 'MSRPC', 'Another common port for MS Windows services.'),
    ('tcp', 137, 'netbios-ns', 'NetBios Name Service.'),
    ('tcp', 138, 'netbios-dgm', 'NetBIOS Datagram Service.'),
    ('tcp', 139, 'NetBIOS-SSN', 'NetBIOS Session Service for communication with MS Windows services (such as file/printer sharing). This has been supported on Windows machines longer than 445 has.'),
    ('tcp', 143, 'IMAP', 'Internet Message Access Protocol version 2. An insecure email retrieval protocol.'),
    ('tcp', 150, 'sql-net', 'SQL-NET'),
    ('tcp', 156, 'sqlsrv', 'SQL Service'),
    ('tcp', 161, 'SNMP', 'Simple Network Management Protocol. (An SNMP agent typically uses 161 while an SNMP manager typically uses 162).'),
    ('tcp', 162, 'snmp-trap', 'Simple Network Management Protocol trap port (An SNMP agent typically uses 161 while an SNMP manager typically uses 162).'),
    ('tcp', 163, 'cmip-man', 'CMIP/TCP Manager'),
    ('tcp', 164, 'cmip-agent', 'CMIP/TCP Agent'),
    ('tcp', 194, 'irc', 'Internet Relay Chat'),
    ('tcp', 201, 'at-rtmp', 'AppleTalk Routing Maintennance'),
    ('tcp', 202, 'at-nbt', 'AppleTalk Name Binding'),
    ('tcp', 203, 'at-3', 'AppleTalk'),
    ('tcp', 204, 'at-echo', 'AppleTalk Echo'),
    ('tcp', 205, 'at-5', 'AppleTalk'),
    ('tcp', 206, 'at-zis', 'AppleTalk Zone Information'),
    ('tcp', 207, 'at-7', 'AppleTalk'),
    ('tcp', 208, 'at-8', 'AppleTalk'),
    ('tcp', 213, 'ipx', 'Novel'),
    ('tcp', 220, 'imap3', 'Interactive Mail Access Protocol v3.'),
    ('tcp', 387, 'aurp', 'AppleTalk Update-Based Routing.'),
    ('tcp', 396, 'netware-ip', 'Novell Netware Over IP'),
    ('tcp', 411, 'rmt', 'Remote mt'),
    ('tcp', 443, 'HTTPS', 'SSL-encrypted web servers use this port by default.'),
    ('tcp', 445, 'Microsoft-DS', 'For SMB communication over IP with MS Windows services (such as file/printer sharing).'),
    ('tcp', 510, 'fcp', 'First Class Server.'),
    ('tcp', 512, 'exec', 'BSD rexecd(8)'),
    ('tcp', 513, 'login', 'BSD rlogind(8)'),
    ('tcp', 514, 'shell', 'cmd BSD rshd(8)'),
    ('tcp', 515, 'printer', 'spooler BSD lpd(8)'),
    ('tcp', 517, 'talk', 'BSD talkd(8)'),
    ('tcp', 518, 'ntalk', 'New Talk'),
    ('tcp', 532, 'netnews', 'Readnews'),
    ('tcp', 540, 'uucp', 'BSD uucpd(8)'),
    ('tcp', 543, 'klogin', 'Kerberos authenticated rlogin'),
    ('tcp', 544, 'kshell', 'Kerberos remote shell'),
    ('tcp', 545, 'ekshell', 'Kerberos authenticated encrypted remote shell'),
    ('tcp', 600, 'pcserver', 'ECD integrated PC board server'),
    ('tcp', 744, 'flexlm', 'Flexible Licence Manager'),
    ('tcp', 749, 'kerberps-adm', 'Kerberos Administration'),
    ('tcp', 750, 'kerberos', 'kdc Kerberos Authentication'),
    ('tcp', 751, 'kerberos_master', 'Kerberos Authentication'),
    ('tcp', 993, 'IMAPS', 'IMAPv2 with SSL added for security.'),
    ('tcp', 995, 'POP3S', 'POP3 with SSL added for security.'),
    ('tcp', 1080, 'socks', 'SOCKS Proxy'),
    ('tcp', 1109, 'kpop', 'POP with Kerberos'),
    ('tcp', 1433, 'ms-sql-s', 'Microsoft MS SQL'),
    ('udp', 1434, 'MS-SQL-DS/ms-sql-m', 'Microsoft SQL Server (monitor).'),
    ('tcp', 1723, 'PPTP', 'Point-to-point tunneling protocol (a method of implementing VPNs which is often required for broadband connections to ISPs).'),
    ('tcp', 2049, 'nfs', 'Network File System'),
    ('tcp', 2105, 'eklogin', 'Kerberos Authenticated rlogin'),
    ('tcp', 2108, 'rkinit', 'Kerberos remote kinit'),
    ('tcp', 2111, 'kx', 'X over Kerberos'),
    ('tcp', 2120, 'kauth', 'Remote kauth'),
    ('tcp', 3306, 'MySQL', 'For communication with MySQL databases.'),
    ('tcp', 3389, 'ms-term-server', 'Microsoft Terminal Services administration port.'),
    ('tcp', 4894, 'lyskom', 'LysCOM (conference system)'),
    ('tcp', 5060, 'sip', 'Session Initiation Protocol'),
    ('tcp', 5900, 'VNC', 'A graphical desktop sharing system (insecure)'),
    ('tcp', 6000, 'x11', '6000-6063/tcp/udp X Window System'),
    ('tcp', 6667, 'irc', 'Internet Relay Chat'),
    ('tcp', 8080, 'HTTP-Proxy', 'Commonly used for HTTP proxies or as an alternate port for normal web servers (e.g. when another server is already listening on port 80, or when run by unprivileged UNIX users who can only bind to high ports).'),
    ('udp', 7, 'echo', ''),
    ('udp', 9, 'discard', 'sink null'),
    ('udp', 13, 'daytime', ''),
    ('udp', 19, 'chargen', 'ttytst source'),
    ('udp', 37, 'time', 'Timeserver'),
    ('udp', 39, 'rlp', 'resource location'),
    ('udp', 53, 'Domain', 'Domain Name System (DNS) server.'),
    ('udp', 66, 'sql*net', 'Oracle SQL*net'),
    ('udp', 67, 'DHCPS', 'bootp server. Dynamic Host Configuration Protocol Server (gives out IP addresses to clients when they join the network).'),
    ('udp', 68, 'DHCPC', 'bootp clinet. DHCP client port.'),
    ('udp', 69, 'TFTP', 'Trivial File Transfer Protocol.'),
    ('udp', 80, 'HTTP', 'Web server.'),
    ('udp', 88, 'kerberos', 'Kerberos'),
    ('udp', 111, 'RPCBind/sunrpc', 'Maps SunRPC program numbers to their current TCP or UDP port numbers.'),
    ('udp', 114, 'audionews', 'Audio News Multicast'),
    ('udp', 113, 'auth', 'authentication service'),
    ('udp', 119, 'nntp', 'Usanet Network News Transfer'),
    ('udp', 123, 'ntp', 'Network Time Protocol.'),
    ('udp', 135, 'MSRPC', 'Windows Remote Procedure Services port.'),
    ('udp', 137, 'NETBIOS-NS', 'One of many UDP ports for Windows services such as file and printer sharing.'),
    ('udp', 138, 'netbios-dgm', 'NetBIOS Datagram Service.'),
    ('udp', 139, 'NetBIOS-SSN', 'NetBIOS Session Service for communication with MS Windows services (such as file/printer sharing). This has been supported on Windows machines longer than 445 has.'),
    ('udp', 143, 'IMAP', 'Internet Message Access Protocol version 2. An insecure email retrieval protocol.'),
    ('udp', 150, 'sql-net', 'SQL-NET'),
    ('udp', 156, 'sqlsrv', 'SQL Service'),
    ('udp', 161, 'SNMP', 'Simple Network Management Protocol. (An SNMP agent typically uses 161 while an SNMP manager typically uses 162).'),
    ('udp', 162, 'snmp-trap', 'Simple Network Management Protocol trap port (An SNMP agent typically uses 161 while an SNMP manager typically uses 162).'),
    ('udp', 163, 'cmip-man', 'CMIP'),
    ('udp', 164, 'cmip-agent', 'CMIP'),
    ('udp', 194, 'irc', 'Internet Relay Chat'),
    ('udp', 201, 'at-rtmp', 'AppleTalk Routing Maintennance'),
    ('udp', 202, 'at-nbt', 'AppleTalk Name Binding'),
    ('udp', 203, 'at-3', 'AppleTalk'),
    ('udp', 204, 'at-echo', 'AppleTalk Echo'),
    ('udp', 205, 'at-5', 'AppleTalk'),
    ('udp', 206, 'at-zis', 'AppleTalk Zone Information'),
    ('udp', 207, 'at-7', 'AppleTalk'),
    ('udp', 208, 'at-8', 'AppleTalk'),
    ('udp', 213, 'ipx', 'Novel'),
    ('udp', 220, 'imap3', 'Interactive Mail Access Protocol v3.'),
    ('udp', 387, 'aurp', 'AppleTalk Update-Based Routing.'),
    ('udp', 396, 'netware-ip', 'Novell Netware Over IP'),
    ('udp', 411, 'rmt', 'Remote mt'),
    ('udp', 445, 'Microsoft-DS', 'Another Windows Services port.'),
    ('udp', 500, 'ISAKMP', 'The Internet Security Association and Key Management Protocol is used to set up IPsec VPNs.'),
    ('udp', 512, 'comsat/biff', 'Used by mail system to notify users.'),
    ('udp', 513, 'who', 'BSD whod(8)'),
    ('udp', 514, 'Syslog', 'The standard UNIX log daemon. BSD syslogd(8).'),
    ('udp', 515, 'printer', 'Printer Spooler'),
    ('udp', 517, 'talk', 'Talk'),
    ('udp', 518, 'ntalk', 'SunOS talkd(8)'),
    ('udp', 520, 'Route', 'Routing Information Protocol (RIP).'),
    ('udp', 540, 'uucp', 'BSD uucpd(8)'),
    ('udp', 543, 'klogin', 'Kerberos authenticated rlogin'),
    ('udp', 544, 'kshell', 'Kerberos remote shell'),
    ('udp', 631, 'IPP', 'Internet Printing Protocol.'),
    ('udp', 635, 'mount', 'NFS Mount Service'),
    ('udp', 640, 'pcnfs', 'PC-NFS DOS Authentication'),
    ('udp', 650, 'bwnfs', 'BW-NFS DOS Authentication'),
    ('udp', 744, 'flexlm', 'Flexible Licence Manager'),
    ('udp', 749, 'kerberos-adm', 'Kerberos Administration'),
    ('udp', 750, 'kerberos', 'Kerberos'),
    ('udp', 751, 'kerberos_master', 'Kerberos Authentication'),
    ('udp', 999, 'applix', 'Applixware'),
    ('udp', 1080, 'socks', 'SOCKS Proxy'),
    ('udp', 1433, 'ms-sql-s', 'Microsoft SQL Server'),
    ('udp', 1434, 'MS-SQL-DS/ms-sql-m', 'Microsoft SQL Server (monitor).'),
    ('udp', 1723, 'PPTP', 'Point-to-point tunneling protocol (a method of implementing VPNs which is often required for broadband connections to ISPs).'),
    ('udp', 2049, 'nfs', 'Network File System'),
    ('udp', 1900, 'UPNP', 'Microsoft Simple Service Discovery Protocol, which enables discovery of Universal plug-and-play devices.'),
    ('udp', 4500, 'nat-t-ike', 'For negotiating Network Address Translation traversal while initiating IPsec connections (during Internet Key Exchange).'),
    ('udp', 5060, 'sip', 'Session Initiation Protocol'),
    ('udp', 6000, 'x11', '6000-6063/tcp/udp X Window System'),
    ('udp', 7000, 'afs', '7000-7009 Andrew File System'),
    ('udp', 49152, 'Varies', 'The first of the IANA-specified dynamic/private ports. No official ports may be registered from here up until the end of the port range (65536). Some systems use this range for their ephemeral ports, so services which bind a port without requesting a specific number are often allocated 49152 if they are the first program to do so.'),
]