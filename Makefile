.PHONY: sort check release

sort:
	python3 scripts/sort.py

check:
	python3 -m json.tool themes/solace.json > /dev/null

release: sort check
	@echo "Theme validated and sorted."
