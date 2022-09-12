

#### Software And Tools Requirements
1. [Github Account](https://github.com)
2. [HerokuAccount](https://heroku.com)
3. [VSCodeIDE](https://code.visualstudio.com)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)


### Creating conda environment
conda create -p venv python==3.7 -y

### -p to create conda environment in the current directory.
### -n to create conda environment in the anaconda env directory.

conda activate venv/

### Installation of the requirements.txt file
pip install -r requirements.txt


### git commands:

## To Add files to git
'''
git add .
'''
OR 

'''
git add
'''
Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status
'''
git status
'''
To check all version maintained by git
'''
git log
'''

To create version/commit all changes by git
'''
git commit -m "message"

'''
To send version/changes to github
'''
git push origin main
'''
To check remote url
'''
git remote -v
'''
