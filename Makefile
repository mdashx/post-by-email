.PHONY: test
test:
# Create a Python environment and run tests
	TESTING=true tox --recreate -e py38
	.tox/py38/bin/pip freeze > dev_requirements.txt
	sed -i '/^post-by-email/d' ./dev_requirements.txt

.PHONY: devenv
devenv:
# A Python 3.8 virtualenv should be activated before running this.
# Install all of our dependencies into the user's active Python virtualenv
	pip install -e .
	pip install -r dev_requirements.txt

.PHONY: qtest
testquick:
# The dev virtualenv should be activated, and then we can test quickly without using tox
# The '-s' argument tells pytest to show us all of the output instead of hiding it 
	TESTING=true pytest -s

testmodule:
# TESTING=true pytest -s tests/<filename>::<module_name>
