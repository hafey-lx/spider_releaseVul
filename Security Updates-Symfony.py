# -*- coding:utf-8 -*-

'''
author: 南瓜 pump
date:   2021-10
'''

import requests
from bs4 import BeautifulSoup

url = "https://symfony.com/blog/?page={}"
cveList = []
for x in range(1, 283):
    if x % 10 == 0:
        print(x)
    resp = requests.get(url.format(x), timeout=3)
    html = resp.text
    if resp.status_code == 200:
        soup = BeautifulSoup(html, 'lxml')
        aList = soup.find_all('a')

        for a in aList:
            href = a.get('href')

            if "cve" in href:
                if "http" not in href:
                    href = "https://symfony.com" + href
                # print(a, href)
                if href not in cveList:
                    cveList.append(href)

for x in cveList:
    print(x)

'''
https://symfony.com/blog/cve-2021-32693-authentication-granted-to-all-firewalls-instead-of-just-one
https://symfony.com/blog/cve-2021-21424-prevent-user-enumeration-in-authentication-mechanisms
/blog/cve-2020-15094-prevent-rce-when-calling-untrusted-remote-with-cachinghttpclient
https://symfony.com/blog/cve-2020-5275-all-access-control-rules-are-required-when-a-firewall-uses-the-unanimous-strategy
https://symfony.com/blog/cve-2020-5255-prevent-cache-poisoning-via-a-response-content-type-header
https://symfony.com/blog/cve-2020-5274-fix-exception-message-escaping-rendered-by-errorhandler
https://symfony.com/blog/cve-2019-11325-fix-escaping-of-strings-in-varexporter
https://symfony.com/blog/cve-2019-18888-prevent-argument-injection-in-a-mimetypeguesser
https://symfony.com/blog/cve-2019-18886-prevent-user-enumeration-using-switch-user-functionality
https://symfony.com/blog/cve-2019-18887-use-constant-time-comparison-in-urisigner
https://symfony.com/blog/cve-2019-18889-forbid-serializing-abstractadapter-and-tagawareadapter-instances
https://symfony.com/blog/cve-2019-10911-add-a-separator-in-the-remember-me-cookie-hash
https://symfony.com/blog/cve-2019-10912-prevent-destructors-with-side-effects-from-being-unserialized
/blog/cve-2019-10913-reject-invalid-http-method-overrides
https://symfony.com/blog/cve-2019-10909-escape-validation-messages-in-the-php-templating-engine
https://symfony.com/blog/cve-2019-10910-check-service-ids-are-valid
https://symfony.com/blog/cve-2018-19789-disclosure-of-uploaded-files-full-path
/blog/cve-2018-19790-open-redirect-vulnerability-when-using-security-http
/blog/cve-2018-14773-remove-support-for-legacy-and-risky-http-headers
/blog/cve-2018-14774-possible-host-header-injection-when-using-httpcache
https://symfony.com/blog/cve-2018-11407-unauthorized-access-on-a-misconfigured-ldap-server-when-using-an-empty-password
https://symfony.com/blog/cve-2018-11385-session-fixation-issue-for-guard-authentication
https://symfony.com/blog/cve-2018-11386-denial-of-service-when-using-pdosessionhandler
https://symfony.com/blog/cve-2018-11408-open-redirect-vulnerability-on-security-handlers
https://symfony.com/blog/cve-2018-11406-csrf-token-fixation
/blog/cve-2017-16653-csrf-protection-does-not-use-different-tokens-for-http-and-https
https://symfony.com/blog/cve-2017-16652-open-redirect-vulnerability-on-security-handlers
https://symfony.com/blog/cve-2017-16654-intl-bundle-readers-breaking-out-of-paths
https://symfony.com/blog/cve-2017-16790-ensure-that-submitted-data-are-uploaded-files
https://symfony.com/blog/cve-2017-11365-empty-passwords-validation-issue
https://symfony.com/blog/cve-2016-2403-unauthorized-access-on-a-misconfigured-ldap-server-when-using-an-empty-password
https://symfony.com/blog/cve-2016-4423-large-username-storage-in-session
https://symfony.com/blog/cve-2016-1902-securerandom-s-fallback-not-secure-when-openssl-fails
https://symfony.com/blog/cve-2015-8125-potential-remote-timing-attack-vulnerability-in-security-remember-me-service
https://symfony.com/blog/cve-2015-8124-session-fixation-in-the-remember-me-login-feature
https://symfony.com/blog/cve-2015-4050-esi-unauthorized-access
https://symfony.com/blog/cve-2015-2308-esi-code-injection
https://symfony.com/blog/cve-2015-2309-unsafe-methods-in-the-request-class
https://symfony.com/blog/cve-2014-6072-csrf-vulnerability-in-the-web-profiler
https://symfony.com/blog/cve-2014-6061-security-issue-when-parsing-the-authorization-header
https://symfony.com/blog/cve-2014-5245-direct-access-of-esi-urls-behind-a-trusted-proxy
/blog/cve-2014-5244-denial-of-service-with-a-malicious-http-host-header
https://symfony.com/blog/security-releases-cve-2014-4931-symfony-2-3-18-2-4-8-and-2-5-2-released
https://symfony.com/blog/security-releases-cve-2013-5958-symfony-2-0-25-2-1-13-2-2-9-and-2-3-6-released
https://symfony.com/blog/cve-2013-5750-security-issue-in-fosuserbundle-login-form

Process finished with exit code 0


'''


