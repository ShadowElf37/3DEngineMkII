#!/bin/bash
ifdef file
	SRC := ${file}
else
	SRC := $(shell ls -t *.py |head -1 |sed -e 's/\.py$$//')
endif
compile:
	-python3 $(SRC).py
	py3compile $(SRC).py
	rename 's/cpython-35\.//g' -f __pycache__/*
	mv -f __pycache__/* compiled/
	rmdir __pycache__
	chmod +x compiled/$(SRC).pyc
run: FORCE
	./compiled/$(SRC).pyc
all: compile run
FORCE:
