SRC = src
EXEC = tp2.pyc

all: $(EXEC)

$(EXEC): $(SRC)/tp2.py
	python3 $(SRC)/compile.py
	cp $(SRC)/__pycache__/tp2.cpython-34.pyc tp2.pyc

.PHONY: clean
clean:
	rm -rf $(SRC)/__pycache__ tp2.pyc
