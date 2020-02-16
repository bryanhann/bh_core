export BH_APP_NAME=bhcore

pushd $0/.. > /tmp/x
export ROOT=$PWD
popd > /tmp/x

VENV=${ROOT}/venv
MAIN=${ROOT}/main.sh
LINK=${HOME}/.local/bin/${BH_APP_NAME}
SCRIPT=${ROOT}/app/main.py

[ -d ${VENV} ] || >&2 python3 -m venv ${VENV}

${VENV}/bin/python3 ${SCRIPT} $*
