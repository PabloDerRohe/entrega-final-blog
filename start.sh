#! /usr/bin/zsh

echo "Checking venv"
sleep 2

if [ $VIRTUAL_ENVIROMENT ]; then
  echo $(deactivate)
  sleep 2
else
  echo "No active venv. Proceeding to activate."
fi

sleep 2

if [ -f  "./pip.lock" ]; then
    echo "Activating pipenv"
    sleep 2
    echo $(pipenv shell)
fi

if [ -d "./venv/" ]; then
    echo "Activating Python venv"
    sleep 2
    echo $(. venv/bin/activate)
else
    echo "No virtual enviroment found. Check directory."
fi

