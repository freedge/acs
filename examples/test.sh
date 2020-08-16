#!/bin/sh
cd  `dirname $0`
ansible-galaxy collection install -p ./ ../freedge-acs-*.tar.gz
fake-switches &
ID=$!
sleep 1
mkdir ~/.ssh ; touch ~/.ssh/known_hosts
ssh-keyscan -T 2 -p 2222 -t rsa 127.0.0.1 >> ~/.ssh/known_hosts
ansible-playbook acs.yml --check
ret=$?
kill $ID
exit $ret


