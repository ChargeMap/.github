docker container run --rm -v $(pwd):/srv/app nyurik/alpine-python3-requests python3 /srv/app/$@ --working-dir=/srv/app
