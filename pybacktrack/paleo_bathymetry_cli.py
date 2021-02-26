
#
# Copyright (C) 2021 The University of Sydney, Australia
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License, version 2, as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from pybacktrack.paleo_bathymetry import main

if __name__ == '__main__':
    
    import sys
    import traceback
    import warnings

    def warning_format(message, category, filename, lineno, file=None, line=None):
        # return '{0}:{1}: {1}:{1}\n'.format(filename, lineno, category.__name__, message)
        return '{0}: {1}\n'.format(category.__name__, message)

    # Print the warnings without the filename and line number.
    # Users are not going to want to see that.
    warnings.formatwarning = warning_format

    try:
        main()
        sys.exit(0)
    except Exception as exc:
        print('ERROR: {0}'.format(exc), file=sys.stderr)
        # Uncomment this to print traceback to location of raised exception.
        traceback.print_exc()
        sys.exit(1)

else:
    # User should only be using this module as a script, not importing it.
    raise RuntimeError("Only use as 'python -m pybacktrack.paleo_bathymetry_cli ...', not as 'import pybacktrack.paleo_bathymetry_cli'.")
