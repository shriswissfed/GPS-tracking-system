# -*- coding: utf-8 -*-

###############################################################################
#
# FlatFileOrderReport
# Returns a tab-delimited flat file order report. The report shows orders from the previous 60 days.
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

class FlatFileOrderReport(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FlatFileOrderReport Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(FlatFileOrderReport, self).__init__(temboo_session, '/Library/Amazon/Marketplace/Reports/FlatFileOrderReport')


    def new_input_set(self):
        return FlatFileOrderReportInputSet()

    def _make_result_set(self, result, path):
        return FlatFileOrderReportResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FlatFileOrderReportChoreographyExecution(session, exec_id, path)

class FlatFileOrderReportInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FlatFileOrderReport
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(FlatFileOrderReportInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        super(FlatFileOrderReportInputSet, self)._set_input('AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        super(FlatFileOrderReportInputSet, self)._set_input('AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(FlatFileOrderReportInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, date) The end of a date range used for selecting the data to report, in ISO8601 date format (i.e. 2012-01-01).)
        """
        super(FlatFileOrderReportInputSet, self)._set_input('EndDate', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        super(FlatFileOrderReportInputSet, self)._set_input('Endpoint', value)
    def set_MWSAuthToken(self, value):
        """
        Set the value of the MWSAuthToken input for this Choreo. ((optional, string) The Amazon MWS authorization token for the given seller and developer.)
        """
        super(FlatFileOrderReportInputSet, self)._set_input('MWSAuthToken', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, date) The start of a date range used for selecting the data to report, in ISO8601 date format (i.e. 2012-01-01).)
        """
        super(FlatFileOrderReportInputSet, self)._set_input('StartDate', value)
    def set_TimeToWait(self, value):
        """
        Set the value of the TimeToWait input for this Choreo. ((optional, integer) By default, the Choreo will wait for 5 minutes to see if the report is ready for retrieval. Max is 120 minutes.)
        """
        super(FlatFileOrderReportInputSet, self)._set_input('TimeToWait', value)

class FlatFileOrderReportResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FlatFileOrderReport Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Report(self):
        """
        Retrieve the value for the "Report" output from this Choreo execution. ((multiline) The report contents.)
        """
        return self._output.get('Report', None)
    def get_GeneratedReportId(self):
        """
        Retrieve the value for the "GeneratedReportId" output from this Choreo execution. ((integer) The GeneratedReportId parsed from the Amazon response.)
        """
        return self._output.get('GeneratedReportId', None)
    def get_ReportProcessingStatus(self):
        """
        Retrieve the value for the "ReportProcessingStatus" output from this Choreo execution. ((string) The status of the report request parsed from the Amazon response.)
        """
        return self._output.get('ReportProcessingStatus', None)
    def get_ReportRequestId(self):
        """
        Retrieve the value for the "ReportRequestId" output from this Choreo execution. ((integer) The ReportRequestId parsed from the Amazon response. This id is used in GetReportRequestList.)
        """
        return self._output.get('ReportRequestId', None)

class FlatFileOrderReportChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return FlatFileOrderReportResultSet(response, path)
