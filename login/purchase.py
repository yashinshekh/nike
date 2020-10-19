from seleniumwire import webdriver
import json
import csv
import requests


base_headers = {}

if __name__ == '__main__':

    jsondata = json.loads(open('nike.har','r').read())['log']['entries']



    for d in jsondata:

        if 'https://unite.nike.com/login?appVersion=833&experienceVersion=833' in d['request']['url'] and d['request']['method'] == "POST":

            headers = d['request']['headers']
            for key in headers:
                base_headers[key['name']] = key['value']

            cookies = {}
            single_cookie = ""
            for head in headers:
                if head['name'] == "Cookie":
                    single_cookie = head['value']

            print(single_cookie)

            cookie_values = ['_abck','_derived_epik','_fbp','_ga','_gat_UA-167630499-2','_gcl_au','_gid','_pin_unauth','_scid','_sctr','_uetsid',
                             '_uetvid','ak_bmsc','AKA_A2','AMCV_F0935E09512D2C270A490D4D@AdobeOrg','AnalysisUserId','anonymousId','audience_segmentation_performed',
                             'bc_nike_new_zealand_triggermail','bc_nike_triggermail','bm_mi','bm_sv','bm_sz','bounceClientVisit2436',
                             'cid','CONSUMERCHOICE','CONSUMERCHOICE_SESSION','cto_bundle','dreamcatcher_sample','feature_enabled__as_nav_rollout',
                             'geoloc','guidS','guidSTimestamp','guidU','llCheck','lls','neo_sample','NIKE_CART','NIKE_COMMERCE_COUNTRY',
                             'NIKE_COMMERCE_LANG_LOCALE','nike_locale','optimizelyEndUserId','ppd','RES_TRACKINGID','ResonanceSegment','RT',
                             's_ecid','siteCatalyst_sample','sq','visitData']

            for c_value in cookie_values:
                try:
                    cookies[c_value] = [i.replace(c_value+'=','').strip() for i in single_cookie.split(';') if c_value in i.split('=')[0].strip()][0]
                except:
                    cookies[c_value] = ''


            r = requests.get("https://www.nike.com/",
                             headers={
                            **base_headers,
                            "Host": "www.nike.com",
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                            "Referer": "https://www.nike.com/",
                            "Cookie": single_cookie,
                            "Upgrade-Insecure-Requests": "1",
                            "Cache-Control": "max-age=0",
                            "TE": "Trailers",
                        },cookies=cookies)

            with open("login.html","w") as f:
                f.write(r.text)


            # print(base_headers)
            #
            # print(single_cookie)




            # print(headers[[i.keys() for i in headers].index('Cookie')])

            # print(headers)


    # print(jsondata)