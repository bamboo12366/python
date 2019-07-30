# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.14.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.apis.admissionregistration_v1beta1_api import AdmissionregistrationV1beta1Api


class TestAdmissionregistrationV1beta1Api(unittest.TestCase):
    """ AdmissionregistrationV1beta1Api unit test stubs """

    def setUp(self):
        self.api = kubernetes.client.apis.admissionregistration_v1beta1_api.AdmissionregistrationV1beta1Api()

    def tearDown(self):
        pass

    def test_create_mutating_webhook_configuration(self):
        """
        Test case for create_mutating_webhook_configuration

        
        """
        pass

    def test_create_validating_webhook_configuration(self):
        """
        Test case for create_validating_webhook_configuration

        
        """
        pass

    def test_delete_collection_mutating_webhook_configuration(self):
        """
        Test case for delete_collection_mutating_webhook_configuration

        
        """
        pass

    def test_delete_collection_validating_webhook_configuration(self):
        """
        Test case for delete_collection_validating_webhook_configuration

        
        """
        pass

    def test_delete_mutating_webhook_configuration(self):
        """
        Test case for delete_mutating_webhook_configuration

        
        """
        pass

    def test_delete_validating_webhook_configuration(self):
        """
        Test case for delete_validating_webhook_configuration

        
        """
        pass

    def test_get_api_resources(self):
        """
        Test case for get_api_resources

        
        """
        pass

    def test_list_mutating_webhook_configuration(self):
        """
        Test case for list_mutating_webhook_configuration

        
        """
        pass

    def test_list_validating_webhook_configuration(self):
        """
        Test case for list_validating_webhook_configuration

        
        """
        pass

    def test_patch_mutating_webhook_configuration(self):
        """
        Test case for patch_mutating_webhook_configuration

        
        """
        pass

    def test_patch_validating_webhook_configuration(self):
        """
        Test case for patch_validating_webhook_configuration

        
        """
        pass

    def test_read_mutating_webhook_configuration(self):
        """
        Test case for read_mutating_webhook_configuration

        
        """
        pass

    def test_read_validating_webhook_configuration(self):
        """
        Test case for read_validating_webhook_configuration

        
        """
        pass

    def test_replace_mutating_webhook_configuration(self):
        """
        Test case for replace_mutating_webhook_configuration

        
        """
        pass

    def test_replace_validating_webhook_configuration(self):
        """
        Test case for replace_validating_webhook_configuration

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
