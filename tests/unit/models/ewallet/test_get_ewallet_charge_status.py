import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.ewallet import ewallet_charge_response
from xendit.models import EWallet


# fmt: off
class TestGetEWalletChargeStatus(ModelBaseTest):
    @pytest.fixture
    def default_ewallet_charge_data(self):
        tested_class = EWallet
        class_name = "EWallet"
        method_name = "get_ewallet_charge_status"
        http_method_name = "get"
        args = ()
        kwargs = {
            "charge_id": "ewc_f3925450-5c54-4777-98c1-fcf22b0d1e1c",
        }
        params = (args, kwargs)
        url = f"/ewallets/charges/{kwargs['charge_id']}"
        expected_correct_result = ewallet_charge_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_ewallet_charge_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_ewallet_charge_data
        headers = {}
        body = {}
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [ewallet_charge_response()], indirect=True)
    def test_return_ewallet_charge_on_correct_params(
        self, mocker, mock_correct_response, default_ewallet_charge_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_ewallet_charge_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_ewallet_charge_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_ewallet_charge_data)

    @pytest.mark.parametrize("mock_correct_response", [ewallet_charge_response()], indirect=True)
    def test_return_ewallet_charge_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_ewallet_charge_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_ewallet_charge_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_ewallet_charge_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_ewallet_charge_data)

    @pytest.mark.parametrize("mock_correct_response", [ewallet_charge_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        self.run_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)
# fmt: on
