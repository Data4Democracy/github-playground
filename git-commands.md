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

9. You made a change in `.gitignore`, but then changed your mind and **dropped it**. This instruction changes file back to where it was at last commit
```
vim .gitignore
git checkout -- .gitignore
```

10. You decided to apply and commit other change
```
vim .gitignore
git status
git add .gitignore
git commit -m "Modifying .gitignore to exclude all .pyc files"
```

11. Take a look at what is different from our last commit. In this case we want the diff of our most recent commit, and we can refer to it using **_HEAD_**
```
git diff HEAD
```

12. We can unstage files by using the `git reset` command
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

4. Back to the top of the main branch (**_master_**)
```
git checkout master
```

5. Change back to the new branch
```
git checkout my_new_feature
```

6. We are inside the NEW `my_new_feature` branch, so further changes will go in there
```
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
```

3. Removing directories
```
git rm -r folder_of_cats
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

## Handling remote repositories

1. Download a full repository
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

6. Pulling, but in a more compact way
```
git pull origin master
```

7. Add a remote repository to push our local repo to the GitHub server (i.e.: We created out repository from scratch and we are setting `origin` in order to be able to _push it_ to a remote server)
```
git remote add origin https://github.com/try-git/try_git.git
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
