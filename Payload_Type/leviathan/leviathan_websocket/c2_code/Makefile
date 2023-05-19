.PHONY: default
default: build_linux ;

BINARY_NAME?=mythic_leviathan_websocket_server
DEBUG_LEVEL?="debug"
MYTHIC_SERVER_HOST?="127.0.0.1"
MYTHIC_SERVER_PORT?="17443"

build:
	go mod download 
	go mod tidy
	CGO_ENABLED=0 go build -o ${BINARY_NAME} -tags=websocket .
	cp ${BINARY_NAME} /

build_local:
	go mod download 
	go mod tidy
	CGO_ENABLED=0 go build -o ${BINARY_NAME} -tags=websocket .

run:
	cp /${BINARY_NAME} .

build_macos:
	go build -o ${BINARY_NAME} -tags=websocket .

run_custom:
	DEBUG_LEVEL=${DEBUG_LEVEL} \
MYTHIC_SERVER_HOST=${MYTHIC_SERVER_HOST} \
MYTHIC_SERVER_PORT=${MYTHIC_SERVER_PORT} \
./${BINARY_NAME}
