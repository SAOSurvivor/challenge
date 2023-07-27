#!/usr/bin/env make

.DEFAULT_GOAL: help

MAKEFLAGS=--no-print-directory

DOCKER_COMPOSE?=docker-compose -p challenge

SHELL_COMMAND_WITHOUT_DEPS?=$(DOCKER_COMPOSE) run --user challenge:challenge --rm -T --no-deps python-flask bash -c

.PHONY: help
help: ## List all Python Makefile targets
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'


##
## Python Containers 📦
## -----------------
##
.PHONY: run
run:  ## Run a python-flask container
	$(DOCKER_COMPOSE) run -p 8080:8080 --rm python-flask python app.py

.PHONY: stop
stop:  ## Stop the running containers
	 $(DOCKER_COMPOSE) down --volumes --remove-orphans

.PHONY: build
build: ## Build the python docker image
	docker build --no-cache --label python-flask --label challenge -t challenge .

.PHONY: clear
clear:  ## Clear volumes and stop containers
	$(DOCKER_COMPOSE) down --volumes --remove-orphans
	docker image prune -af --filter label=challenge


##
## Python Tests 🧪
## ------------
##
.PHONY: test
test: ## Shortcut to launch all the test tasks (unit and integration).
	$(DOCKER_COMPOSE) run --rm python-flask pytest
