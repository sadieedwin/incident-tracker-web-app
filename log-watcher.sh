#!/bin/bash

LOG_FILE="/var/log/incident-tracker/incident_tracker.log"
KEYWORDS="ERROR|WARNING|CRITICAL"

echo "Scanning $LOG_FILE for issues..."
grep -E "$KEYWORDS" "$LOG_FILE"

