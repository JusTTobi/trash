#!/bin/bash
for f in `seq 400 -1 0`;
do
if [[ -e ./pull$f.pdb ]]
then
cat ./pull$f.pdb >> trj_pull.pdb
fi
done
