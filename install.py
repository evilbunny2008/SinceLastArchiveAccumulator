""" Installer for SinceLastArchiveAccumulator service. """

import configobj

from weecfg.extension import ExtensionInstaller

VERSION = "0.0.1"

def loader():
    """ Load and return the extension installer. """
    return SinceLastArchiveAccumulatorInstaller()

class SinceLastArchiveAccumulatorInstaller(ExtensionInstaller):
    """ The extension installer. """
    def __init__(self):

        install_dict = {
            'version': VERSION,
            'name': 'SinceLastArchiveAccumulator',
            # add a leading space, so that long versions does not run into the description
            'description': ' A simple accumulator to provide the totals since the last archive cycle',
            'author': "John Smith",
            'author_email': "deltafoxtrot256+SinceLastArchiveAccumulator@gmail.com",
            'files': [('bin/user', ['bin/user/SinceLastArchiveAccumulator.py'])]
        }

        install_dict['prep_services'] = 'user.SinceLastArchiveAccumulator.SinceLastArchiveAccumulatorService'

        super().__init__(install_dict)
