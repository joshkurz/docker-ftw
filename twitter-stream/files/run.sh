#!/bin/bash
bash ./run-hc-server  &  PIDIOS=$!
python twitter-stream.py &  PIDMIX=$!
wait $PIDIOS
wait $PIDMIX
