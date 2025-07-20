class AwsCredentialsClipboardUpdater < Formula
  include Language::Python::Virtualenv

  desc "CLI tool to manage AWS credentials from clipboard or data"
  homepage "https://github.com/vavasilva/aws-credentials-clipboard-updater"
  url "https://github.com/vavasilva/aws-credentials-clipboard-updater/archive/v1.0.5.tar.gz"
  sha256 "0f9dcef211c18f5770562a5996a0216d5bf6ac4ea39fc323b868cc2ae1b3bc93"
  license "MIT"

  depends_on "python@3.12"

  resource "click" do
    url "https://files.pythonhosted.org/packages/96/d3/f04c7bfcf5c1862a2a5b845c6b2b360488cf47af55dfa79c98f6a6bf98b5/click-8.1.7.tar.gz"
    sha256 "ca9853ad459e787e2192211578cc907e7594e294c7ccc834310722b41b9ca6de"
  end

  resource "pyperclip" do
    url "https://files.pythonhosted.org/packages/a7/2c/4c64579f847bd5d539803c8b909e54ba087a79d01bb3aba433a95879a6c5/pyperclip-1.8.2.tar.gz"
    sha256 "105254a8b04934f0bc84e9c24eb360a591aaf6535c9def5f29d92af107a9bf57"
  end

  def install
    virtualenv_install_with_resources
  end

  test do
    assert_match "Usage:", shell_output("#{bin}/awscreds --help")
  end
end