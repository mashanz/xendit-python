import pytest

from .base_integration_test import BaseIntegrationTest
from tests.sampleresponse.disbursement import disbursement_response
from tests.sampleresponse.disbursement import disbursement_banks_response


class TestDisbursement(BaseIntegrationTest):
    @pytest.fixture
    def Disbursement(self, xendit_instance):
        return xendit_instance.Disbursement

    def test_create_virtual_account_return_correct_keys(self, Disbursement):
        disbursement = Disbursement.create(
            "demo_1475459775872",
            "BCA",
            "Bob Jones",
            "1231242311",
            "Reimbursement for shoes",
            17000,
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            disbursement, disbursement_response()
        )

    def test_get_disbursement_by_id_return_correct_keys(self, Disbursement):
        disbursement = Disbursement.get("5ef1befeecb16100179e1d05")
        self.assert_returned_object_has_same_key_as_sample_response(
            disbursement, disbursement_response()
        )

    def test_get_disbursement_by_external_id_return_correct_keys(self, Disbursement):
        disbursement = Disbursement.get_by_ext_id("demo_1475459775872")
        self.assert_returned_object_has_same_key_as_sample_response(
            disbursement[0], disbursement_response()
        )

    def test_get_disbursement_banks_return_correct_keys(self, Disbursement):
        disbursement_banks = Disbursement.get_available_banks()
        self.assert_returned_object_has_same_key_as_sample_response(
            disbursement_banks[0], disbursement_banks_response()[0]
        )
