# auto-doc
This repo only serves as a basis to learn how to automate documentation building and publishing on github pages.

It will contain a couple of dummy modules that will almost surely be useless to anyone :)


Done steps: 

            - can build in the vm
            - extract from vm and push to /docs
            - set up gh-pages repo
            - push to gh-pages instead of /docs
            - set up website
            - change some stuff to see how fast website updates

Main Issue: - .nojekyll is not included in the push hence it disappears with prevents github pages to do it s magic.
Solved by forking and modifying https://github.com/s0/git-publish-subdir-action
