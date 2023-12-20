import pandas as pd
import os
import git


def get_git_root():
    try:
        # Create a GitPython Repo object
        repo = git.Repo(search_parent_directories=True)

        # Get the absolute path of the root folder
        git_root = repo.git.rev_parse("--show-toplevel")

        return git_root
    except git.InvalidGitRepositoryError:
        # Handle the case where the current directory is not a Git repository
        print("Not a Git repository or an error occurred.")
        return None

# Get the root folder of the Git repository
root_folder = get_git_root()
# load CSV file from dataset dir
dataset_dir=os.path.join(root_folder,"dataset/")
dataset_file="amazon.csv"
dataset_file_path=os.path.join(dataset_dir,dataset_file)





