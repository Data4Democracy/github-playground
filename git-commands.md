# Git commands

This is a set of recipes to use Git, partly based on a very good tutorial in
'Real Python' called [Introduction to Git and GitHub for Python Developers](https://realpython.com/python-git-github-intro/)

## Basic, day-to-day commands

1. Initialize a new local repository (repo) from scratch: Create a directory, get into it, and use `git init`
```
mkdir my_new_repo
cd my_new_repo
git init
```

2. See current status. Very useful instruction, and used very often
```
git status
```

3. Create new file in repo. Now file exists, but it is _untracked_ by Git
```
echo "print('Hello World')" > hello.py
git status
```

4. Add new file to Git tracking. Now it is tracked but it is not yet part of the repo. It is in the **_staging area_**
```
git add hello.py
git status
```

5. Commit a change, adding a comment. Now `hello.py` belongs to repo
```
git commit -m "Creating hello.py"
git status
```

6. Create another file and add it to repo. Original `hello.py` was also modified, so it must be again added and commited
```
vim myname.py
vim hello.py
git add hello.py myname.py
git status
git commit -m "Added myname module. Minor modification to hello.py"
```

   - Instead of specifying each file in the `git add` line, we can do:
```
git add --all
```

7. The `.gitignore` file is special, because it contains the names of the files which should be ignored by Git, like for instance, python `.pyc` files. It is Ok to use wildcards inside it
```
vim .gitignore
git add .gitignore
git commit -m "Created .gitignore"
```

8. See a log of the changes. This can be verbose when you have commited many changes
```
git log
```

9. The command `git log` provides, besides the commit messages of the changes, the **_SHA_** ID of every commit. Then, one can use the command `git show SHA` to get a detailed description of the changes related to that commit:
```
git show fcf22e5d3cf1c
```

10. You made a change in `.gitignore`, but then changed your mind and **dropped it**. This instruction changes the file back to where it was at last commit
```
vim .gitignore
git checkout -- .gitignore
```

11. You decided to apply and commit other change
```
vim .gitignore
git status
git add .gitignore
git commit -m "Modifying .gitignore to exclude all .pyc files"
```

12. Take a look at what is different from our last commit. In this case we want the diff of our most recent commit, and we can refer to it using **_HEAD_**
```
git diff HEAD
```
If what we want to check is whether we are about to commit a file with whitespace errors, let's use:
```
git diff --check
```

13. We can unstage files by using the `git reset` command
```
git reset octofamily/octodog.txt
```

## Handling branches

1. To see all branches
```
git branch
```

2. To create a new branch _AND MOVE IN THERE_
```
git checkout -b my_new_feature
```

3. To see all branches again (current branch is marked with '\*')
```
git branch
```

4. Back to the top of the main branch (**_master_**), and confirm we are indeed there
```
git checkout master
git branch
```

5. Change back to the new branch. Confirm we are where we want
```
git checkout my_new_feature
git branch
```

6. We are inside the **NEW** `my_new_feature` branch, so further changes will go in there
```
vim hello.py
git add hello.py
git commit -m "Added code for feature x"
```

7. Get back to the top of the `master` branch
```
git checkout master
```

8. Compare the state of two branches
```
git show-branch my_new_feature master
git show-branch my_new_feature
git show-branch master
```

9. `HEAD` is where the repository is currently pointing to (in this case, the last commit done in `my_new_feature`)
```
git show-branch HEAD
```

10. This is like regular 'show-branch' but using SHA codes instead of names
```
git show-branch --sha1-name my_new_feature master
```

11. Go back to `master` and **MERGE** changes **FROM** `my_new_feature` **TO** `master`
```
git checkout master
git merge my_new_feature
```

12. Removing a branch which is no longer needed
```
git branch -d my_new_feature
```

13. This is for checking out (use) the repository at an specific point in time (98011e69...). The long number is the (unique) SHA code
```
git checkout 98011e69fda0df3937e99e2d7ac11ca3a1e37959
```

## Miscellaneous instructions

1. Rename a file
```
git mv <old-file> <new-file>
git commit -m "Renaming file"
```

2. Removing files (wildcards are also valid)
```
git rm <target-file>
git commit -m "Removed target file"
```

3. Removing directories
```
git rm -r folder_of_cats
git commit -m "Removed directory 'folder_of_cats'"
```

4. Set user email and name _for every repository_ in your computer
```
git config --global user.email "user@example.com"
git config --global user.name "User Surname"
```

5. Set user email and name _for a single repository_
```
git config user.email "user@example.com"
git config user.name "User Surname"
```

6. Several aspects of Git behavior, like aliases, may be set up at file `~/.gitconfig`. An example content could be:
```
[user]
    name = architest
    email = 23104729+architest@users.noreply.github.com
[color]
    ui = true
[alias]
    co = checkout
    br = branch
```

## Handling remote repositories

1. Download (_clone_) a full repository
```
git clone https://github.com/jima80525/github-playground.git
```

2. **Download** (_pull_) to the current computer the changes in an already present repository
```
git pull https://github.com/architest/git-example
```

3. **Upload** (_push_) the local changes to GitHub:
```
git push https://github.com/architest/git-example master
```

4. '**origin**' is an alias for the remote server repository (if we started by _cloning_ a repo), so the former instruction can be abbreviated as:
```
git push origin master
```

5. The same, but the `-u` option tell Git to remember the parameters, so afterwards we only need to write `git push` (some conditions may apply)
```
git push -u origin master
```

6. _Pulling_, but in a more compact way
```
git pull origin master
```
'Pulling' can be seen as the combination of two commands: `git fetch`, which fetches down all the changes on the server that we don't have yet, but doesn't modify the working directory, and `git merge`, which combines remote and local data.

7. Add a remote repository to push our local repo to the GitHub server (i.e.: We created our repository from scratch, and we are setting `origin` in order to be able to _push it_ to a remote server)
```
git remote add origin https://github.com/try-git/try_git.git
```

8. In order to make a _tracking branch_, i.e., a local branch that automatically tracks a remote branch, we can do:
```
git checkout -b serverfix origin/serverfix
```
In this way, the local _serverfix_ branch tracks the remote _serverfix_ branch in _origin_. A shorthand for the former operation is:
```
git checkout --track origin/serverfix
```
If the local branch doesn't exist, and you know the (unique) name of the branch in the remote, we can even do:
```
git checkout serverfix
```
If one wants to use a different name for the local branch (_myfix_ in this example):
```
git checkout -b myfix origin/serverfix
```

9. In order to see which tracking branches have been setup, we use the `-vv` option with `git branch`:
```
 git branch -vv
        iss53     7e424c3 [origin/iss53: ahead 2] forgot the brackets
        master    1ae2a45 [origin/master] deploying index fix
      * serverfix f8674d9 [teamone/server-fix-good: ahead 3, behind 1] this should do it
        testing   5ea463a trying something new
```
Or, even better, to get completely up-to-date numbers from all tracked remotes:
```
git fetch -all
git branch -vv
```

## Configure Git to sync your fork with the original repository

1. First, fork the repository using GitHub facilities for that

   - Original repository is: https://github.com/jima80525/github-playground.git
   - The forked repository is: https://github.com/architest/github-playground.git

2. Then, clone the repository to the local machine
```
git clone https://github.com/architest/github-playground.git
```

3. Get into the cloned repository. It is good to check the currently configured remote repository
```
git remote -v
```

  The result should be something like:
```
origin  https://github.com/architest/github-playground.git (fetch)
origin  https://github.com/architest/github-playground.git (push)
```

4. Add the path to the original repository
```
git remote add upstream https://github.com/jima80525/github-playground.git
```

5. Verify that it worked:
```
git remote -v
```
```
origin  https://github.com/architest/github-playground.git (fetch)
origin  https://github.com/architest/github-playground.git (push)
upstream    https://github.com/jima80525/github-playground.git (fetch)
upstream    https://github.com/jima80525/github-playground.git (push)
```

6. Now, in order to fetch changes from the `upstream` repository you do:
```
git fetch upstream
```

7. Possible changes are in `upstream/master`. Make sure you're in `master`:
```
git checkout master
```

8. Merge changes from `upstream/master` into local `master` branch
```
git merge upstream/master
```

9. Updated!!!


# Simple git workflow:

1. `git status` – Make sure your current area is clean.
2. `git pull` – Get the latest version from the remote. This saves merging issues later.
3. Edit your files and make your changes. Remember to run your linter and do unit tests!
4. `git status` – Find all files that are changed. Make sure to watch untracked files too!
5. `git add [files]` – Add the changed files to the staging area.
6. `git commit -m "message"` – Make your new commit.
7. `git push origin [branch-name]` – Push your changes up to the remote.
