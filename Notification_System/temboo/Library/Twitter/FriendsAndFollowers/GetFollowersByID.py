# -*- coding: utf-8 -*-

###############################################################################
#
# GetFollowersByID
# Retrieves a list of numeric IDs for every user following the specified user.
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

class GetFollowersByID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetFollowersByID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetFollowersByID, self).__init__(temboo_session, '/Library/Twitter/FriendsAndFollowers/GetFollowersByID')


    def new_input_set(self):
        return GetFollowersByIDInputSet()

    def _make_result_set(self, result, path):
        return GetFollowersByIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetFollowersByIDChoreographyExecution(session, exec_id, path)

class GetFollowersByIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetFollowersByID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        super(GetFollowersByIDInputSet, self)._set_input('AccessToken', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        super(GetFollowersByIDInputSet, self)._set_input('AccessTokenSecret', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The API Key (or Consumer Key) provided by Twitter.)
        """
        super(GetFollowersByIDInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The API Secret (or Consumer Secret) provided by Twitter.)
        """
        super(GetFollowersByIDInputSet, self)._set_input('ConsumerSecret', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) Specifies the number of IDs to retrieve, up to a maximum of 5,000 per distinct request.)
        """
        super(GetFollowersByIDInputSet, self)._set_input('Count', value)
    def set_Cursor(self, value):
        """
        Set the value of the Cursor input for this Choreo. ((optional, string) Allows you to pass in the previous_cursor or next_cursor in order to page through results.)
        """
        super(GetFollowersByIDInputSet, self)._set_input('Cursor', value)
    def set_ScreenName(self, value):
        """
        Set the value of the ScreenName input for this Choreo. ((conditional, string) The screen name of the user for whom to return results for. Required if UserID isn't specified.)
        """
        super(GetFollowersByIDInputSet, self)._set_input('ScreenName', value)
    def set_StringifyIDs(self, value):
        """
        Set the value of the StringifyIDs input for this Choreo. ((optional, boolean) A boolean flag indicating that Tweet IDs should be returned as strings.)
        """
        super(GetFollowersByIDInputSet, self)._set_input('StringifyIDs', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((conditional, string) The ID of the user for whom to return results for. Required if ScreenName isn't specified.)
        """
        super(GetFollowersByIDInputSet, self)._set_input('UserID', value)

class GetFollowersByIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetFollowersByID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The rate limit ceiling for this particular request.)
        """
        return self._output.get('Limit', None)
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The number of requests left for the 15 minute window.)
        """
        return self._output.get('Remaining', None)
    def get_Reset(self):
        """
        Retrieve the value for the "Reset" output from this Choreo execution. ((date) The remaining window before the rate limit resets in UTC epoch seconds.)
        """
        return self._output.get('Reset', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)

class GetFollowersByIDChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetFollowersByIDResultSet(response, path)
