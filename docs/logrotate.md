### 📁 Log Rotation Configuration

I configured **log rotation** for the incident tracker application logs located at `/var/log/incident-tracker/incident_tracker.log`. This helps manage log file size and keeps logs organized.

**Logrotate Config:** 
```
ubuntu@inci-track:~$ ll /etc/logrotate.d/incident_tracker
-rw-r--r-- 1 root root 168 Apr 16 06:14 /etc/logrotate.d/incident_tracker
```

    /var/log/incident-tracker/incident_tracker.log { 

    weekly # Rotate logs weekly 
    
    rotate 4 # Keep 4 archived logs 
    
    compress # Compress old logs to save space 
    
    delaycompress # Delay compression until next rotation 
    
    missingok # Ignore if log file is missing 
    
    notifempty # Don’t rotate empty logs 
    
    create 0640 ubuntu ubuntu # Create new logs with this permission and ownership
    
    }


✅ Added inline comments for clarity and maintainability.  
✅ Validated that log rotation will keep the logs under control automatically.

**app.py for logging:**
import logging
```python
# Logging
logging.basicConfig(
    filename='/var/log/incident-tracker/incident_tracker.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
)

add route: app.logger.info(f"Incident created: Title='{title}', Priority={priority}")
edit route: app.logger.info(f"Incident updated: ID={incident.id}, Title='{incident.title}', Priority={incident.priority}")
delete route: app.logger.info(f"Incident deleted: ID={incident.id}, Title='{incident.title}'")
```
