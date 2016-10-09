#!/bin/bash
bash ./run-hc-server  &  PIDIOS=$!
bash ./run-twitter-stream  &  PIDMIX=$!
wait $PIDIOS
wait $PIDMIX
