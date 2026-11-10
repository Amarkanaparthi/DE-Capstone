#!/usr/bin/env bash
# Summarise a log file: total lines, count per level, top 3 ERROR messages.
# Usage: bash count_errors.sh <logfile>

# Stop with a usage message if no file was given
if [ $# -lt 1 ]; then
  echo "Usage: $0 <logfile>"
  exit 1
fi

logfile=$1

# Stop if the file doesn't exist
if [ ! -f "$logfile" ]; then
  echo "File not found: $logfile"
  exit 1
fi

echo "Log summary for: $logfile"
echo "Total lines: $(wc -l < "$logfile")"

echo
echo "Count per level:"
for level in INFO WARN ERROR; do
  count=$(grep -c " $level " "$logfile")
  echo "  $level: $count"
done

echo
echo "Top 3 ERROR messages:"
awk '$3 == "ERROR" {print $4}' "$logfile" | sort | uniq -c | sort -rn | head -3