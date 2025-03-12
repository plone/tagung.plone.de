from tagung.plone.de import PACKAGE_NAME


class TestSetupInstall:
    def test_addon_installed(self, installer):
        """Test if tagung.plone.de is installed."""
        assert installer.is_product_installed(PACKAGE_NAME) is True

    def test_browserlayer(self, browser_layers):
        """Test that IBrowserLayer is registered."""
        from tagung.plone.de.interfaces import ITagungPloneDeLayer

        assert ITagungPloneDeLayer in browser_layers
