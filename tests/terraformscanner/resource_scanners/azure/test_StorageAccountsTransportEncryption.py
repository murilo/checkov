import unittest

from bridgecrew.terraformscanner.models.enums import ScanResult
from bridgecrew.terraformscanner.resource_scanners.azure.StorageAccountsTransportEncryption import scanner


class TestAzureManagedDiscEncryption(unittest.TestCase):

    def test_failure(self):
        resource_conf = {'name': ['test'], 'resource_group_name': ['${azurerm_resource_group.rg.name}'],
                         'location': ['${var.location}'], 'account_kind': ['StorageV2'], 'account_tier': ['Premium'],
                         'account_replication_type': ['LRS']}

        scan_result = scanner.scan_resource_conf(conf=resource_conf)
        self.assertEqual(ScanResult.FAILURE, scan_result)

    def test_success(self):
        def test_failure(self):
            resource_conf = {'name': ['test'], 'resource_group_name': ['${azurerm_resource_group.rg.name}'],
                             'location': ['${var.location}'], 'account_kind': ['StorageV2'],
                             'account_tier': ['Premium'], 'account_replication_type': ['LRS'],
                             'enable_https_traffic_only': [True]}
            scan_result = scanner.scan_resource_conf(conf=resource_conf)
            self.assertEqual(ScanResult.SUCCESS, scan_result)


if __name__ == '__main__':
    unittest.main()