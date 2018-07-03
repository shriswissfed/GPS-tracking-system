# -*- coding: utf-8 -*-

###############################################################################
#
# GetIntradayTimeSeries
# Returns the intraday time series for a given resource based on a date range you specify.
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

class GetIntradayTimeSeries(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetIntradayTimeSeries Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetIntradayTimeSeries, self).__init__(temboo_session, '/Library/Fitbit/Statistics/GetIntradayTimeSeries')


    def new_input_set(self):
        return GetIntradayTimeSeriesInputSet()

    def _make_result_set(self, result, path):
        return GetIntradayTimeSeriesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetIntradayTimeSeriesChoreographyExecution(session, exec_id, path)

class GetIntradayTimeSeriesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetIntradayTimeSeries
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(GetIntradayTimeSeriesInputSet, self)._set_input('AccessToken', value)
    def set_DetailLevel(self, value):
        """
        Set the value of the DetailLevel input for this Choreo. ((conditional, string) Number of data points to include. for heart rate data, this must be either 1sec or 1min. For other activities, it can be 1min or 15min.)
        """
        super(GetIntradayTimeSeriesInputSet, self)._set_input('DetailLevel', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((required, date) The end date of the date range for the data you want to retrieve (in the format yyyy-MM-dd). You can also specify the value '1d'.)
        """
        super(GetIntradayTimeSeriesInputSet, self)._set_input('EndDate', value)
    def set_EndTime(self, value):
        """
        Set the value of the EndTime input for this Choreo. ((optional, date) The end of the period, in the format HH:mm.)
        """
        super(GetIntradayTimeSeriesInputSet, self)._set_input('EndTime', value)
    def set_ResourcePath(self, value):
        """
        Set the value of the ResourcePath input for this Choreo. ((required, string) The resource path that you want to access (for example: activities/heart). See Choreo documentation for a full list of resource paths.)
        """
        super(GetIntradayTimeSeriesInputSet, self)._set_input('ResourcePath', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in: xml or json. Defaults to json.)
        """
        super(GetIntradayTimeSeriesInputSet, self)._set_input('ResponseFormat', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((required, date) The start date of the date range for the data you want to retrieve (in the format yyyy-MM-dd). You can also specify the value 'today'.)
        """
        super(GetIntradayTimeSeriesInputSet, self)._set_input('StartDate', value)
    def set_StartTime(self, value):
        """
        Set the value of the StartTime input for this Choreo. ((optional, date) The start of the period, in the format HH:mm.)
        """
        super(GetIntradayTimeSeriesInputSet, self)._set_input('StartTime', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided.)
        """
        super(GetIntradayTimeSeriesInputSet, self)._set_input('UserID', value)

class GetIntradayTimeSeriesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetIntradayTimeSeries Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Fitbit.)
        """
        return self._output.get('Response', None)

class GetIntradayTimeSeriesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetIntradayTimeSeriesResultSet(response, path)
