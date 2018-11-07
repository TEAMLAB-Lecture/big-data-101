import errno
import os
import wget

# Take an absolute path; I've already seen horses puke! ;)
path_ = r'.{}all'.format(os.sep)
def mkdir_p(path):
    try:
        os.makedirs(path)
        return 'Path created.'
    except OSError as exc:  # Python > 2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            return 'Path already exists!'
        else:
            # Otherwise, throw error:
            raise

mkdir_p(path_)

for year in range(2001, 2017):
    url = 'https://www1.ncdc.noaa.gov/pub/data/noaa/{0}/081810-99999-{0}.gz'.format(year)  # Python > 3.6, otherwise use '…{}…'.format(year)
    print(url)
    filename = wget.download(url, out=path_)
