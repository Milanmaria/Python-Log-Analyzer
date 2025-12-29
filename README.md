#  Python Log Analyzer

A simple Python-based log analysis tool that detects failed SSH login attempts and flags suspicious IP addresses.  
This project simulates basic SOC (Security Operations Center) analysis tasks.

##  Features
- Parses SSH authentication logs
- Extracts IP addresses from failed login attempts
- Counts attempts per IP
- Flags suspicious IPs based on a threshold
- Easy to extend for other log formats

##  Technologies Used
- Python 3
- Regular Expressions (`re`)
- Collections (`defaultdict`)

## What I Learned

- Working with real-world log files
- Using regex to extract security-relevant data
-Identifying brute-force patterns
-Writing modular Python scripts
-Understanding SOC-style analysis
