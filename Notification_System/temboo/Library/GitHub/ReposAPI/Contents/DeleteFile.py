# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteFile
# Deletes a file in a repository.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteFile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteFile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteFile, self).__init__(temboo_session, '/Library/GitHub/ReposAPI/Contents/DeleteFile')


    def new_input_set(self):
        return DeleteFileInputSet()

    def _make_result_set(self, result, path):
        return DeleteFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteFileChoreographyExecution(session, exec_id, path)

class DeleteFileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteFile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(DeleteFileInputSet, self)._set_input('AccessToken', value)
    def set_Branch(self, value):
        """
        Set the value of the Branch input for this Choreo. ((optional, string) The branch name. Default: the repository’s default branch (usually master))
        """
        super(DeleteFileInputSet, self)._set_input('Branch', value)
    def set_Contributer(self, value):
        """
        Set the value of the Contributer input for this Choreo. ((optional, string) The type of contributer: committer (the default) or author.)
        """
        super(DeleteFileInputSet, self)._set_input('Contributer', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((optional, string) The email of the author (or committer) of the commit.)
        """
        super(DeleteFileInputSet, self)._set_input('Email', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((required, string) The commit message.)
        """
        super(DeleteFileInputSet, self)._set_input('Message', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((optional, string) The name of the author (or committer) of the commit.)
        """
        super(DeleteFileInputSet, self)._set_input('Name', value)
    def set_Path(self, value):
        """
        Set the value of the Path input for this Choreo. ((required, string) The content path.)
        """
        super(DeleteFileInputSet, self)._set_input('Path', value)
    def set_Repo(self, value):
        """
        Set the value of the Repo input for this Choreo. ((required, string) The name of the repository.)
        """
        super(DeleteFileInputSet, self)._set_input('Repo', value)
    def set_Sha(self, value):
        """
        Set the value of the Sha input for this Choreo. ((required, string) The blob SHA of the file being deleted.)
        """
        super(DeleteFileInputSet, self)._set_input('Sha', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((required, string) The GitHub account owner.)
        """
        super(DeleteFileInputSet, self)._set_input('User', value)

class DeleteFileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteFile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The available rate limit for your account. This is returned in the GitHub response header.)
        """
        return self._output.get('Limit', None)
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The remaining number of API requests available to you. This is returned in the GitHub response header.)
        """
        return self._output.get('Remaining', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The response from GitHub.)
        """
        return self._output.get('Response', None)

class DeleteFileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteFileResultSet(response, path)
