#!/bin/sh
cd  `dirname $0`
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
ansible-galaxy collection install -p ./ ../freedge-acs-*.tar.gz
fake-switches &
ID=$!
ansible-playbook acs.yml --check
ret=$?
kill $ID
deactivate
exit $ret


