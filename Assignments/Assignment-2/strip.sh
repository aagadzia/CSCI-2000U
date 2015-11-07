#!/bin/bash

# Ama Agadzi - 100449923

read k m filename

tail -n +$k | head -n -$m $filename > gadsby_stripped.txt


