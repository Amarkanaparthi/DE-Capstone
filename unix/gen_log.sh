#!/usr/bin/env bash
levels=(INFO INFO INFO WARN ERROR)
msgs=("user_login" "payment_processed" "db_timeout" "file_uploaded" "cache_miss")
for i in $(seq 1 200); do
  h=$(printf "%02d" $((RANDOM % 24)))
  m=$(printf "%02d" $((RANDOM % 60)))
  echo "2026-11-09 $h:$m:00 ${levels[$((RANDOM % 5))]} ${msgs[$((RANDOM % 5))]}"
done | sort > app.log