Recommended git workflow
========================

Preface
-------

There exist many workflows and guides for using Git, and everyone has their own preferred ways of handling certain
aspects of their Git repositories.

Whether or not you follow this guide in detail, or use other methods, it is important that you know what the commands
you are using do, and understand basic Git operations such as committing, pulling, merging, pushing and rebasing.

Please refer to the `git documentation`_ as needed, and create small demo repositories to test common operations before
applying them on to the Protwis repository. If in doubt, you are always welcome to contact members of the
:doc:`Protwis team <contact>`.

.. _git documentation: http://git-scm.com/documentation


Prerequisites
-------------
If you have followed the :doc:`setup guide <local_installation>`, you should already have created a fork of the Protwis repository, and cloned the
fork to your computer. This means that you have access to three different repositories, all containing the same code.
From your perspective, these repository are referred to as:

* upstream (the main Protwis repository, where you have read only access)
* origin (your fork of protwis, where you have full write access)
* local (the repository your work on locally)

Configuring the upstream repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The upstream repo is currently not connected to your local repo. To connect it, type the following on you local command
line (from the repo root dir)::

    git remote add upstream https://github.com/protwis/protwis.git

Workflow
--------

Branches
^^^^^^^^

Before doing any changes to the code, create and check out a new branch::

    git branch my_feature_branch
    git checkout my_feature_branch

You can always see which branch you are on by typing::

    git branch

Committing
^^^^^^^^^^

Once you have made changes on your branch, add them to the index and commit them::

    git add my_file.py
    git commit -m "Optimized the performance of my_file"

ALWAYS add a commit message with the -m flag.

Note that only files that have been added to the index will be committed, and you can add all modified or new files
with::

    git add --all

Keeping your branch up to date
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While you work on your branch, other developers may push their commits to the master branch. It is important that you
keep your repository updated with the latest changes. Do this DAILY.

To fetch the latest changes, checkout the master branch (make sure to commit all changes to your branch first) and pull
from upstream::

    git checkout master
    git pull upstream master

Your local master branch is now up to date, but your feature branch is not. To update it, use the rebase command::

    git checkout my_feature_branch
    git rebase master

The rebase will usually go through without issues, but if Git can not merge the changes automatically, a merge conflict
will arise.

If this happens, open the conflicted file (Git will tell you which file is conflicted) in a text editor. Conflicts are
displayed as two versions of the conflicted code block, one marked "HEAD", and one marked "master". There may be more
than one conflict in the same file. Edit the file manually to resolve the conflict(s) (i.e. remove one of the versions,
or combine them). Then add the file to the index, and continue the rebase::

    git add path/to/file
    git rebase --continue

This will usually complete the rebase. However, it is possible that a new conflict will arise. If this happens, do not
worry. Simply follow the same steps as before to resolve the conflict(s), until the rebase is completed.

Merging your branch into master
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

NOTE! Make sure your master and feature branches are updated before doing this.
When the changes on your feature branch are ready, merge them into master::

    git checkout master
    git merge my_feature_branch

Pushing changes to Bitbucket and sending a pull request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After merging your changes into master, you should push them to your fork on Bitbucket (origin) and send a pull request
(PR) to the main repository::

    git push origin master

Then go to the main website of your fork and select the "Create pull request" option in the left menu. The PR should be
from your fork's master branch, to upstream/master.
