# -*- coding: utf-8 -*-

###############################################################################
#
# GetAllContacts
# Retrieve data for all contacts in an account.
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

class GetAllContacts(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetAllContacts Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetAllContacts, self).__init__(temboo_session, '/Library/Google/Contacts/GetAllContacts')


    def new_input_set(self):
        return GetAllContactsInputSet()

    def _make_result_set(self, result, path):
        return GetAllContactsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAllContactsChoreographyExecution(session, exec_id, path)

class GetAllContactsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetAllContacts
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        super(GetAllContactsInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((required, string) The client ID provided by Google when you register your application.)
        """
        super(GetAllContactsInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((required, string) The client secret provided by Google when you registered your application.)
        """
        super(GetAllContactsInputSet, self)._set_input('ClientSecret', value)
    def set_Group(self, value):
        """
        Set the value of the Group input for this Choreo. ((optional, string) Constrains the results to only the contacts belonging to the group specified. The value of this parameter specifies group ID.)
        """
        super(GetAllContactsInputSet, self)._set_input('Group', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) The maximum number of entries to return.)
        """
        super(GetAllContactsInputSet, self)._set_input('MaxResults', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((required, string) The refresh token retrieved in the last step of the OAuth process. This is used when an access token is expired or not provided.)
        """
        super(GetAllContactsInputSet, self)._set_input('RefreshToken', value)
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) Sorting order direction. Can be either ascending or descending.)
        """
        super(GetAllContactsInputSet, self)._set_input('SortOrder', value)
    def set_StartIndex(self, value):
        """
        Set the value of the StartIndex input for this Choreo. ((optional, integer) The index of the first result to be retrieved (for paging).)
        """
        super(GetAllContactsInputSet, self)._set_input('StartIndex', value)
    def set_UpdatedMin(self, value):
        """
        Set the value of the UpdatedMin input for this Choreo. ((optional, date) The lower bound on entry update dates to filter by (e.g., 2015-01-16T00:00:00).)
        """
        super(GetAllContactsInputSet, self)._set_input('UpdatedMin', value)
    def set_UserEmail(self, value):
        """
        Set the value of the UserEmail input for this Choreo. ((optional, string) The email address of the user whose contacts you want to retrieve. Defaults to "default," or the user whose OAuth access token is passed.)
        """
        super(GetAllContactsInputSet, self)._set_input('UserEmail', value)

class GetAllContactsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetAllContacts Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_AccessToken(self):
        """
        Retrieve the value for the "AccessToken" output from this Choreo execution. ((optional, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        return self._output.get('AccessToken', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google.)
        """
        return self._output.get('Response', None)

class GetAllContactsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetAllContactsResultSet(response, path)
