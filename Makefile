.PHONY: clean
clean:
# Remove Python build artifacts
	find . -name 'dist' -type d -exec rm -rf {} +
	find . -name '*.egg-info' -type d -exec rm -rf {} +
	find . -name '*.pyc' -delete
	find . -name '*pycache*' -delete


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

# --------------------------------------------
# Get our Python package installed and running
# --------------------------------------------

dist:
	python setup.py sdist bdist_wheel

# Create Python environment on the server
.PHONY: py
py:
	ssh ${USER}@${HOST} 'sudo apt-get install -y software-properties-common'
	ssh ${USER}@${HOST} 'sudo add-apt-repository -y ppa:deadsnakes/ppa'
	ssh ${USER}@${HOST} 'sudo apt-get update'
	ssh ${USER}@${HOST} 'sudo apt-get install -y python3.8'
	ssh ${USER}@${HOST} ' sudo apt-get install -y python3-venv'
	ssh ${USER}@${HOST} 'python3.8 -m venv .virtualenv/py3'

# Install Python package on the server
install: clean dist
	ssh ${USER}@${HOST} 'mkdir -p /home/${USER}/post-by-email-app/'
	scp dist/post_by_email-${VERSION}-py3-none-any.whl ${USER}@${HOST}:/home/${USER}/post-by-email-app/post_by_email-${VERSION}-py3-none-any.whl
	ssh ${USER}@${HOST} 'source .virtualenv/py3/bin/activate && pip uninstall -y post_by_email'
	ssh ${USER}@${HOST} 'source .virtualenv/py3/bin/activate && pip install /home/${USER}/post-by-email-app/post_by_email-${VERSION}-py3-none-any.whl'

#	scp ./.env ${USER}@${HOST}:/home/${USER}/${WORKING_DIR}/.env
