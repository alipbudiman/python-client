"""
    NFT Storage API

    # API Reference   # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import nft_storage
from nft_storage.model.files import Files
from nft_storage.model.nft_deals import NFTDeals
from nft_storage.model.pin import Pin
globals()['Files'] = Files
globals()['NFTDeals'] = NFTDeals
globals()['Pin'] = Pin
from nft_storage.model.nft import NFT


class TestNFT(unittest.TestCase):
    """NFT unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNFT(self):
        """Test NFT"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NFT()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
