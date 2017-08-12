REM kill task for OPEN VPN
taskkill /Fi /IM openvpn.exe /T 2> nul
taskkill /F /IM openvpn-gui.exe /T 2> nul
REM Start new connection to get new IP adress
CD C:\Program Files\OpenVPN\bin
start openVPN-gui --connect CA_Montreal.ovpn

REM  WAIT for connection to establish
SLEEP 20