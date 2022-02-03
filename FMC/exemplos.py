def _url(self, namespace='base', path=''):
    """
    Generate URLs on the fly for requests to firepower api
    :param namespace: name of the url namespace that should be used. options: base, config, auth. default = base
    :param path: the url path for which a full url should be created
    :return: url in string format
    """
    if namespace == 'config':
        return '{0}://{1}{2}/domain/{3}{4}'.format(self.protocol, self.hostname, API_CONFIG_URL, self.domain, path)
    if namespace == 'platform':
        return '{0}://{1}{2}{3}'.format(self.protocol, self.hostname, API_PLATFORM_URL, path)
    if namespace == 'auth':
        return '{0}://{1}{2}{3}'.format(self.protocol, self.hostname, API_AUTH_URL, path)
    if namespace == 'refresh':
        return '{0}://{1}{2}{3}'.format(self.protocol, self.hostname, API_REFRESH_URL, path)
    return '{0}://{1}{2}'.format(self.protocol, self.hostname, path)