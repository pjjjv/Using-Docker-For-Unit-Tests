# Using-Docker-For-Unit-Tests
Example setup for using a Docker container for unit testing with Jenkins or some other test software


## What is this?##

This repository is setup with the script to be tested at the root, and the Dockerfile used to build the test environment in "tests".  You would create a repository like this, with your own code to be tested, and your own Dockerfile.

Your Jenkins or other CI server would:

1. Clone the repository.
2. Copy the code to be tested into "tests"
3. Build the Docker image, adding the code to be tested during the build
4. Run the image with your test command
5. Check the output

In the case of this repo:

    cp script-to-test.py tests
    push tests
    docker build -t my_test .  <-- note the period
    popd
    docker run -it my_test <arguments>
    # Then compare the output


**ProTip!**

The output of a `docker run` command in bash will have a carriage return, so if you're testing integers rather than strings, pipe it to `tr -cd '[[:digit:]]'` before comparing:

    $ RESULT="$(docker run --rm -it centos echo '2')"
    $ echo $RESULT
    2
    $ if [ $RESULT -eq 2 ] ; then echo 'equal' ; fi
    : integer expression expected
    $ RESULT="$(docker run --rm -it centos echo '2' | tr -cd '[[:digit:]]' )"
    $ if [ $RESULT -eq 2 ] ; then echo 'equal' ; fi
    equal


