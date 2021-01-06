# github-playground
A safe place to experiment with git & GitHub in a group setting


## Purpose
This is a playground open to anyone looking to practice using git & GitHub in a group project. Feel free to make any and all changes as you test your GitHub chops. One caveat, we ask you please do not change the main readme unless you are making an improvement (P.S. please help the next person and make improvements).

To reiterate this repository is to get people (you!) comfortable with using GitHub - do not be scared to try things out!

#### Give it a try!

* [Fork](https://help.github.com/articles/fork-a-repo/) the repo (this step is optional if you have have "contributor" access to the repo).
* [Clone](https://help.github.com/articles/cloning-a-repository/) from your command line `git clone https://github.com/youruserID/github-playground.git`. 
* Move to main directory `cd github-playground`
* Check your status `git status` Should see "On Branch Master" "Your branch is up-to-date with 'origin/master'"
* Create and checkout a branch to work from: `git checkout -b <branch_name>` EX: `git checkout -b training-branch` You can see all branches by typing `git branch`. Note: we are using training-branch in this example but by the time you follow these instructions someone may have already created `training-branch` you should create a unique branch.
* Read about git [branching and merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging).
* Make a change to an existing file or create a new file and save. `EX: echo "print("hello")" > hello.py`
* Check status of your change with `git status`. Your file should show up under "Untracked Files" EX: `hello.py` or whatever file you created.
* Add file to changes `git add <filename>` or `git add .` (adds all untracked files -- CAREFUL use with caution) EX: `git add hello.py`
* See exactly what [changes](https://git-scm.com/docs/git-diff) are staged `git diff --cached` (or `git diff` if files are not yet staged).
* Commit your changes `git commit -m "Hey this is my first commit"` [Read](http://chris.beams.io/posts/git-commit/) about how to write good commit messages.
* Check your [remote](https://help.github.com/articles/adding-a-remote/) `git remote -v` (if you started by cloning a repo from GitHub origin should already be set)
* [Push](https://help.github.com/articles/pushing-to-a-remote/) your changes to the remote server by typing `git push <remote-name> <your-branch>` EX: `git push origin training-branch`
* Open the repo in GitHub and select your [branch](https://help.github.com/articles/viewing-branches-in-your-repository/).
* You should see [compare and pull request](https://help.github.com/articles/about-pull-requests/). This will bring up a summary of your changes and show you what branch you are merging.
* Edit your message and click submit. Now you should see your pull request show up in the pull requests tab!
* In a real project your PR may be discussed and reviewed. Stakeholders may suggest changes or updates and (hopefully) eventually your code will be merged!
  * If you need to make changes to the code in your PR you can make the changes EX: `echo "print("hello good sir")" > hello.py`
  * `git diff` to check your changes
  * `git add hello.py` to stage your changes
  * `git commit -m "More formal greeting"`
  * Do another `git push origin <branch>` and changes show automatically show up in the PR (No need to open another PR).

#### Maintaining Your Fork Up-to-Date with the Project Branch
After your commit has been merged, you may want to maintain your local fork up to date:

* Add the project branch as an [upstream repository](https://help.github.com/articles/configuring-a-remote-for-a-fork/) i.e. `git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git`
* Fetch the master branch from upstream `git fetch upstream`
* Checkout your fork's local master branch `git checkout master`
* Merge the upstream/master `git merge upstream/master`
* At this point you can always delete your local branch that you created (if you no longer need it) i.e. `git branch -d training-branch`
* To ensure that your fork on GitHub is also up-to-date you can do `git push origin master`

This only scratches the surface of what is possible with git and GitHub. Feel free continue to use this repo when you need to test out (or document for others!) more complicated workflow.

#### Tips for Contributing to Data for Democracy Projects
* Use pull requests whenever possible. Direct commits to `master` are best for trivial changes.
* Use separate branches for each enhancement or fix you're working on, unless the circumstances dictate otherwise.
* Make your new branch from the most appropriate current branch, e.g. if you’re working on a contribution to `feature-x`, branch from this (and especially not `master`).
* Make sure your branch is up to date before you start working.
* Give branches appropriate names, e.g. `fix/238` (where 238 is the issue number) or `original-branch/my-feature`.
* Make each PR as concise as possible. Don’t rewrite large sections of the codebase to fit a tiny contribution. Make a separate issue or PR for any extra modifications that need to be made.
* Don't merge new commits from `master` to your branches: wait till the final merge into `master` (or rebase your branches to `master`).
* Don't be scared and ask for help. Most of us have learned this "on the job".

#### Additional resources
* Try GitHub [desktop](https://desktop.github.com/) client if you prefer to work with GUI
* Created by Code School: [TryGit](https://try.github.io/levels/1/challenges/1) teaches you how to use Git in 15 minutes
* Lifesaving advice from [ohshitgit](http://ohshitgit.com/)
* Udacity [course](https://www.udacity.com/course/how-to-use-git-and-github--ud775)
* [Learn Version Control with Tower](https://www.git-tower.com/learn/git/videos/) (videos)
* [Comparing Workflows](https://www.atlassian.com/git/tutorials/comparing-workflows) for learning how the Forking Workflow…works

#### Encounter issues?
* Do not worry, we have all been there!
* Join [#github-help](https://datafordemocracy.slack.com/messages/github-help/) channel on Slack and ask for help.
* DM someone directly. The users below have volunteered to assist with GitHub questions:
  * @mattgawarecki, @margeaux, @bstarling, @john
* Was something not clear or was there an area you struggled with? Submit a [Pull request](https://help.github.com/articles/about-pull-requests/) (PR) or open an [issue](https://help.github.com/articles/creating-an-issue/) to help us improve!
