# rules for image building and deployment

.PHONY: build_image
build_image:
	docker build --pull -t rueberger/foo:${BRANCH_NAME}-${GIT_COMMIT} -f Dockerfile ${CURDIR}

# push images
.PHONY: image
image: build_image
	docker push rueberger/foo:${BRANCH_NAME}-${GIT_COMMIT}

# set built images as latest and push
.PHONY: set_latest
set_latest:
	docker tag rueberger/foo:${BRANCH_NAME}-${GIT_COMMIT} rueberger/foo:${BRANCH_NAME}-latest
	docker push rueberger/foo:${BRANCH_NAME}-latest

# copy over .hypothesis if it exists
.PHONY: set_up_test_cache
set_up_test_cache:
ifneq ($(wildcard .hypothesis/.), )
	docker build -t rueberger/foo:${BRANCH_NAME}-${GIT_COMMIT}-test -f Dockerfile.test --build-arg BRANCH_NAME=${BRANCH_NAME} --build-arg GIT_COMMIT=${GIT_COMMIT} ${CURDIR}
else
	docker tag rueberger/foo:${BRANCH_NAME}-${GIT_COMMIT} rueberger/foo:${BRANCH_NAME}-${GIT_COMMIT}-test
endif

.PHONY: create_test_container
create_test_container: set_up_test_cache
	docker create --network foo_services_core --entrypoint="" --name foo-${BRANCH_NAME}-${GIT_COMMIT}-test rueberger/foo:${BRANCH_NAME}-${GIT_COMMIT}-test ./home/app/foo/scripts/run_tests.sh

.PHONY: run_tests
run_tests: create_test_container
	docker start --attach foo-${BRANCH_NAME}-${GIT_COMMIT}-test

# pull test results and caches out of container
.PHONY: pull_tests
pull_tests:
	docker cp foo-${BRANCH_NAME}-${GIT_COMMIT}-test:/home/app/foo/nosetests.xml nosetests.xml
	docker cp foo-${BRANCH_NAME}-${GIT_COMMIT}-test:/home/app/foo/pylint.log pylint.log
	rm -rf .hypothesis
	docker cp foo-${BRANCH_NAME}-${GIT_COMMIT}-test:/home/app/foo/.hypothesis/ .hypothesis

# clean up test container
.PHONY: clean_tests
clean_tests:
	docker stop foo-${BRANCH_NAME}-${GIT_COMMIT}-test
	docker rm foo-${BRANCH_NAME}-${GIT_COMMIT}-test
