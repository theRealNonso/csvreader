[Unit]
Description=CSV extraction Service
After=multi-user.target
Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/nonso/Desktop/TestCSV/csvextraction.py
StandardInput=tty-force
User=nonso

[Install]
WantedBy=multi-user.target
