#!/bin/sh
cd  `dirname $0`
ansible-galaxy collection install -p ./ ../freedge-acs-*.tar.gz
fake-switches &
ID=$!
ansible-playbook acs.yml --check
ret=$?
kill $ID
exit $ret


