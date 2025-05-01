# SQLite db removal and restoration

### Removed the db file
```
-rw-rw-r-- 1 ubuntu ubuntu 18427 May  1 13:10 db-2025-05-01.sql
ubuntu@inci-track:~/incident-tracker-web-app$
ubuntu@inci-track:~/incident-tracker-web-app$ rm incidents.db
```

```
ubuntu@inci-track:~/incident-tracker-web-app$ systemctl status incident-tracker.service
● incident-tracker.service - Gunicorn instance to serve Flask app
     Loaded: loaded (/etc/systemd/system/incident-tracker.service; enabled; preset: enabled)
     Active: active (running) since Thu 2025-05-01 10:17:35 UTC; 3h 22min ago
   Main PID: 2224 (python)
      Tasks: 3 (limit: 1129)
     Memory: 95.5M (peak: 95.8M)
        CPU: 38.913s
     CGroup: /system.slice/incident-tracker.service
             ├─2224 /home/ubuntu/incident-tracker-web-app/venv/bin/python /home/ubuntu/incident-tracker-web-app/app.py
             └─2225 /home/ubuntu/incident-tracker-web-app/venv/bin/python /home/ubuntu/incident-tracker-web-app/app.py

May 01 13:38:42 inci-track python[2225]:   File "/home/ubuntu/incident-tracker-web-app/venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 2>May 01 13:38:42 inci-track python[2225]:     raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
May 01 13:38:42 inci-track python[2225]:   File "/home/ubuntu/incident-tracker-web-app/venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1>May 01 13:38:42 inci-track python[2225]:     self.dialect.do_execute(
May 01 13:38:42 inci-track python[2225]:   File "/home/ubuntu/incident-tracker-web-app/venv/lib/python3.12/site-packages/sqlalchemy/engine/default.py", lin>May 01 13:38:42 inci-track python[2225]:     cursor.execute(statement, parameters)
May 01 13:38:42 inci-track python[2225]: sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) attempt to write a readonly database
May 01 13:38:42 inci-track python[2225]: [SQL: INSERT INTO incident (title, description, priority, systems_affected, resolution, root_cause, created_at, up>May 01 13:38:42 inci-track python[2225]: [parameters: ('test', 'test', 'Low', '', '', '', '2025-05-01 13:38:42.009664', '2025-05-01 13:38:42.009668')]      May 01 13:38:42 inci-track python[2225]: (Background on this error at: https://sqlalche.me/e/20/e3q8)
```
## Errors after db file removal:
- Add and Edit is failing now

![image](https://github.com/user-attachments/assets/0a8663bd-04f8-4cbd-94fb-fd11ada7d704)
![image](https://github.com/user-attachments/assets/06fefdd7-7469-463a-a2b0-c4d9a939d5a1)
![image](https://github.com/user-attachments/assets/93bc3199-eded-41d0-8167-3dbd224271e3)

## Restoration:
- Restore db file from the backup:

```
ubuntu@inci-track:~/incident-tracker-web-app$ sudo systemctl stop incident-tracker.service
ubuntu@inci-track:~/incident-tracker-web-app$
ubuntu@inci-track:~/incident-tracker-web-app$ pwd
/home/ubuntu/incident-tracker-web-app
ubuntu@inci-track:~/incident-tracker-web-app$
ubuntu@inci-track:~/incident-tracker-web-app$ sqlite3 incidents.db < /home/ubuntu/incident-tracker-backups/db-2025-05-01.sql
ubuntu@inci-track:~/incident-tracker-web-app$
ubuntu@inci-track:~/incident-tracker-web-app$ sudo systemctl start incident-tracker.service
ubuntu@inci-track:~/incident-tracker-web-app$
ubuntu@inci-track:~/incident-tracker-web-app$ ll incidents.db
-rw-r--r-- 1 ubuntu ubuntu 32768 May  1 13:43 incidents.db
ubuntu@inci-track:~/incident-tracker-web-app$
ubuntu@inci-track:~/incident-tracker-web-app$ date
Thu May  1 13:43:23 UTC 2025
```

- **Working** :)

![image](https://github.com/user-attachments/assets/8479e3b7-54e4-4114-922c-95525763951e)
