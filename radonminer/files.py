from enum import Enum
import json


class FailureProneFileEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, FailureProneFile):
            return {
                "filepath": o.filepath,
                "commit": o.commit,
                "fixing_commit": o.fixing_commit
            }

        return json.JSONEncoder.default(self, o)


class FailureProneFileDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, o):
        if type(o) == dict:
            return FailureProneFile(filepath=o["filepath"],
                                    commit=o["commit"],
                                    fixing_commit=o["fixing_commit"])


class FixingFile:
    """
    This class is responsible to implement the methods for storing information about fixing files (i.e., files belonging
    to fixing commits)
    """

    def __init__(self, filepath: str, fic: str, bic: str):
        """
        :param filepath: the file of the path at the fixing-commit
        :param fic: the fixing-commit sha
        :param bic: the bug-inducing-commit sha
        """
        self.filepath = filepath  # Name at FIXING-COMMIT
        self.fic = fic
        self.bic = bic

    def __eq__(self, other):
        if isinstance(other, FixingFile):
            return self.filepath == other.filepath

        return False


class FailureProneFile:
    """
    This class is responsible to implement the methods for storing information about labeled files
    """

    def __init__(self,
                 filepath: str,
                 commit: str,
                 fixing_commit: str):
        """
        :param filepath: the filepath from the root of the repository
        :param commit: the commit hash
        :param fixing_commit: the commit fixing this file
        """

        self.filepath = filepath
        self.commit = commit
        self.fixing_commit = fixing_commit

    def __eq__(self, other):
        if isinstance(other, FailureProneFile):
            return self.filepath == other.filepath and self.commit == other.commit

        return False
