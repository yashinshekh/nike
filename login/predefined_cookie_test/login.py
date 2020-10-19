import requests
import csv

cookies = {
    "_abck": "AF02B081DB4FE398C3A07B2996B814A9~-1~YAAQZ3bNF3UYHjV1AQAAi1c4PwTXcBczak3nZA0CvbjTDKdxpu4HHGEvgXqEWoe2AEsfuIsev9utpGAn1o+66K54E4rwGn0euAvC0oavJXd9zBJR28XIq6ENFvLkGLlG10wpJoa684z+8RwF+zuNbe8d0znyErWTdiEFiXhpD/zxIICy79NzvaG/Pvf6h2UEfY/l5gX0ZCVVWlnwH+ST4qWeoQ5N00VJKoX3xb10noiPpruBLqNRV0aO+eZthXX2fhuEMHEE6s0wOLc4IkHwObOL+rjvkm+AvK4/LRf/u5MNpLSGbeqVMDqI93jOmB7v4VLJqy2V6Wh7ev3pVE3fforySXEZ85dnk5HiVuyUO2B7Tut/xgNAl0yPPQD71orvA8Ubydj5n5jCaUQmnMqew+ulbn5t1A0PLVgM3NAptBMX8m0j6FPrORLzUolihT5SPq0W94M=~0~-1~-1",
    "_derived_epik": "dj0yJnU9bDkzN3lfN0VicnZCWEk0RkU0ckcxSk9udm42aE9hSXkmbj1KSkU2OWZ2TWNTZW1TZGpIOXFBZnN3Jm09MSZ0PUFBQUFBRjg0dWcwJnJtPTEmcnQ9QUFBQUFGODR1ZzA",
    "_fbp": "fb.1.1597552061317.1648663435",
    "_ga": "GA1.2.752594614.1597116714",
    "_gat_UA-167630499-2": "1",
    "_gcl_au": "1.1.479043779.1597116712",
    "_gid": "GA1.2.413769502.1603083339",
    "_pin_unauth": "dWlkPVpHVXhNelV4WmpVdE56STBPUzAwWmpJekxXSTVORGd0TWpBMVpXSmxaREJtTnpneiZycD1kSEoxWlE",
    "_scid": "59c7c1b0-3d66-4b99-bbb8-fcca8c9c03db",
    "_sctr": "1|1597515300000",
    "_uetsid": "4eb1ae3011c711eb8180f1f68b67fd64",
    "_uetvid": "f04de01c34172d44de90d261e9cfb70e",
    "ak_bmsc": "F3B37198947690A1010F3EEC8520207817CD7651B87000003C1C8D5F4772D404~plQkp+Ba5Q5U8rjcJHDEMR8JDd3bT4qkyNJKFWIq1luGdb5fPVcEqhkXHQt7m+l4BcQMWMZ+KRGvOkyo4W5E0JYIw6n8LHo0bCSE3i3akDHTkf/yfkRVngV8kAqcuLUex/MM4/lSoAdLK8YTu4mKw4pVlnXqUnUQeTdekIsTFbgxEimTqIof5O17jCk2pnwLqSxTQcarBWHwtnrPTvAdpOJdV0rKWJZSR4YB0N2dnMdhIPRtp9gGqgIemgJUik+BRh",
    "AKA_A2": "A",
    "AMCV_F0935E09512D2C270A490D4D@AdobeOrg": "1994364360|MCMID|33389469561038572447356666046441492316|MCAID|NONE|MCOPTOUT-1597123911s|NONE|vVersion|3.4.0",
    "AnalysisUserId": "844520c0-eb46-4ff7-8775-9a2b88884903",
    "anonymousId": "32267D718C54CCA23AC7F4101A04C615",
    "audience_segmentation_performed": "true",
    "bc_nike_new_zealand_triggermail": "{\"distinct_id\": \"173f585e56a3b7-082fedd8fc26e78-7f2c6753-15f900-173f585e56b1a8\",\"cart_total\": 0}",
    "bc_nike_triggermail": "{\"distinct_id\": \"173f26653b8232-07e11812d031158-7f2c6753-15f900-173f26653b91c0\",\"cart_total\": 0,\"ch\": \"556396943\",\"bluecoreSiteIsMember\": true,\"bc_persist_updated\": 1603083329304,\"bc_id\": -1310386303}",
    "bm_mi": "D0EF12EC951AFBCA83A60FC432546A7F~SpTodZ1I1gW3+qp9WLMs4Aqqsl2zr9Q3+Foxi9oONjMhu1iZ2k1hmC02bfT39Ohs0HmJpfU5ryqrOFo10gHIA/CBBvdHA4DX/QMyF4u6NT0yReWXjiU9owf3eleInJgXsmSPLm2HKAGKhcelT2LUl6RZzA54PumH5cQCLg2rIw2Ft220KoigLpvJjD28BZCTJdfvOvxqXbvfh2NOFw64OdPoQo7pjSTVN1+/g6zUhJ8=",
    "bm_sv": "D45967773F9BED56FD4FD47D35C43C4F~OlzytJZbhti93nds/WMjN1AeYlfFXzgeHGlUWM8ThBRdYcPmF35RrazTmuUg1zqjhX2OIMCreiL5+Rv6MaOia3S31Ehup0LkueOtMK29rXiw7vblrrUgO/AXYrDI4CCzTxQgRAg9Fk1Hjj2DbD3p2w==",
    "bm_sz": "2FC8E496DEB596EC916E0DF8AE49A9BC~YAAQUXbNF2wBp+x0AQAA5VE2Pwnv+DxhJ9bpa069qX+AYvnl3ircq4k1IyImFS7xVosj6w/qHpVOhwDVR4AbmU33eN/lC/CITLCq8GILfROngq7Wu8QQwMBU5BVIw8I7YyOu7jUS2Tcu5v9lK+8Rp4medu9uSF3bdb5k5Q/iburSzgL3cOEnu0SjtJE/UmupHCTMLSRvlNjjA30nW38tMWGlNLvFN12eYzw+5ku+gnrXHTnICl7rwYeBqyZayGk53nSupnzcV2wK2+wAq+9zLGqwgdMxKdy0BLWzBL0=",
    "bounceClientVisit2436": "N4IgZgbgLiBcCMBWAnAdkYgzPAbDgNCBAJYAmcSaG2ALKgByoAMi88hAhgPZxOEA2ABzggAFlCiCAzgFJMAQRkAmAGLKVAdy0A6AHbEA1gFNtAYy4BbdboBe6kJym9CEQRDhLC5WCHKEATiIOIKbQFCjoWPB0hFJkcDSEAOamgbBKfCAWzr7xPhnwLEw4yDSIzMjIiEo4GMH8YQgR1Lg4AL5AA",
    "cid": "undefined|undefined",
    "CONSUMERCHOICE": "us/en_us",
    "CONSUMERCHOICE_SESSION": "t",
    "cto_bundle": "2n7AMF9HNmxwWUFkT05FeFNzQiUyRmwza2JSOGVvZkthMnV4YmdCNUJYUmx6R0tXUVZBdXN0SHRFSERwUUFXekNYaXdPJTJCUDFENEFQcXpraEY1eXZqY1BwUEszcmdPOXZqZUdlQ3Z6VTlFaE5BWlVMNlpGUjl5ZmpPY3JlT3FRanBaTWh4NDhOZVZ2WHNNd1BsWVNTVFV1NWhQQSUyQkElM0QlM0Q",
    "dreamcatcher_sample": "92",
    "feature_enabled__as_nav_rollout": "true",
    "geoloc": "cc=NP,rc=,tp=vhigh,tz=GMT+5.75,la=27.67,lo=85.32",
    "guidS": "8e7b49ae-7d43-41aa-93ba-fe1c1928be1a",
    "guidSTimestamp": "1600925024796|1600925024796",
    "guidU": "b21e3988-7ec5-42ec-cf2e-2d79bbf9da0a",
    "llCheck": "lYe6joX2AkMg4TG9gQk4JQZ5S0JFMMNq8xSzRe6gLfgA7MQ78CHZ2GWIjWrUpQDqXBYs5viAY3mqjlsf7h8s8Pz75r+5BtLmSaHdG8YnHlrA8tWhLliOslO4YmB+1w/l040FAO6nW1Ea+W8RbMV8EA2H/BbLdmUgdr/xb/tU54g=",
    "lls": "3",
    "neo_sample": "94",
    "NIKE_CART": "b:c",
    "NIKE_COMMERCE_COUNTRY": "NP",
    "NIKE_COMMERCE_LANG_LOCALE": "en_NP",
    "nike_locale": "np/en_np",
    "optimizelyEndUserId": "oeu1597930126743r0.697496215128809",
    "ppd": "homepage|nikecom>homepage",
    "RES_TRACKINGID": "282558582937435",
    "ResonanceSegment": "1",
    "RT": "\"z=1&dm=nike.com&si=f0af3c6b-ec35-470d-986b-104669ce3ebd&ss=kgg2f55l&sl=3&tt=63h&bcn=//684d0d3b.akstat.io/&ld=2rv9\"",
    "s_ecid": "MCMID|33389469561038572447356666046441492316",
    "siteCatalyst_sample": "52",
    "sq": "3",
    "visitData": "{\"visit\":\"1\",\"visitor\":\"19be2c29-92dd-4c7d-a563-22b4e024f265\"}"
}

headers = {
    "Request Headers (4.970 KB)": {
        "headers": [
            {
                "name": "Accept",
                "value": "*/*"
            },
            {
                "name": "Accept-Encoding",
                "value": "gzip, deflate, br"
            },
            {
                "name": "Accept-Language",
                "value": "en-NP,en;q=0.5"
            },
            {
                "name": "Connection",
                "value": "keep-alive"
            },
            {
                "name": "Content-Length",
                "value": "173"
            },
            {
                "name": "Content-Type",
                "value": "application/json"
            },
            {
                "name": "Cookie",
                "value": "AMCV_F0935E09512D2C270A490D4D%40AdobeOrg=1994364360%7CMCMID%7C33389469561038572447356666046441492316%7CMCAID%7CNONE%7CMCOPTOUT-1597123911s%7CNONE%7CvVersion%7C3.4.0; AnalysisUserId=844520c0-eb46-4ff7-8775-9a2b88884903; s_ecid=MCMID%7C33389469561038572447356666046441492316; anonymousId=32267D718C54CCA23AC7F4101A04C615; sq=3; _gcl_au=1.1.479043779.1597116712; _ga=GA1.2.752594614.1597116714; NIKE_CART=b:c; siteCatalyst_sample=52; dreamcatcher_sample=92; neo_sample=94; guidU=b21e3988-7ec5-42ec-cf2e-2d79bbf9da0a; cto_bundle=2n7AMF9HNmxwWUFkT05FeFNzQiUyRmwza2JSOGVvZkthMnV4YmdCNUJYUmx6R0tXUVZBdXN0SHRFSERwUUFXekNYaXdPJTJCUDFENEFQcXpraEY1eXZqY1BwUEszcmdPOXZqZUdlQ3Z6VTlFaE5BWlVMNlpGUjl5ZmpPY3JlT3FRanBaTWh4NDhOZVZ2WHNNd1BsWVNTVFV1NWhQQSUyQkElM0QlM0Q; _scid=59c7c1b0-3d66-4b99-bbb8-fcca8c9c03db; _sctr=1|1597515300000; _fbp=fb.1.1597552061317.1648663435; _derived_epik=dj0yJnU9bDkzN3lfN0VicnZCWEk0RkU0ckcxSk9udm42aE9hSXkmbj1KSkU2OWZ2TWNTZW1TZGpIOXFBZnN3Jm09MSZ0PUFBQUFBRjg0dWcwJnJtPTEmcnQ9QUFBQUFGODR1ZzA; _pin_unauth=dWlkPVpHVXhNelV4WmpVdE56STBPUzAwWmpJekxXSTVORGd0TWpBMVpXSmxaREJtTnpneiZycD1kSEoxWlE; bounceClientVisit2436=N4IgZgbgLiBcCMBWAnAdkYgzPAbDgNCBAJYAmcSaG2ALKgByoAMi88hAhgPZxOEA2ABzggAFlCiCAzgFJMAQRkAmAGLKVAdy0A6AHbEA1gFNtAYy4BbdboBe6kJym9CEQRDhLC5WCHKEATiIOIKbQFCjoWPB0hFJkcDSEAOamgbBKfCAWzr7xPhnwLEw4yDSIzMjIiEo4GMH8YQgR1Lg4AL5AA; bc_nike_new_zealand_triggermail=%7B%22distinct_id%22%3A%20%22173f585e56a3b7-082fedd8fc26e78-7f2c6753-15f900-173f585e56b1a8%22%2C%22cart_total%22%3A%200%7D; CONSUMERCHOICE_SESSION=t; lls=3; llCheck=lYe6joX2AkMg4TG9gQk4JQZ5S0JFMMNq8xSzRe6gLfgA7MQ78CHZ2GWIjWrUpQDqXBYs5viAY3mqjlsf7h8s8Pz75r+5BtLmSaHdG8YnHlrA8tWhLliOslO4YmB+1w/l040FAO6nW1Ea+W8RbMV8EA2H/BbLdmUgdr/xb/tU54g=; optimizelyEndUserId=oeu1597930126743r0.697496215128809; RES_TRACKINGID=282558582937435; ResonanceSegment=1; guidS=8e7b49ae-7d43-41aa-93ba-fe1c1928be1a; guidSTimestamp=1600925024796|1600925024796; NIKE_COMMERCE_COUNTRY=NP; NIKE_COMMERCE_LANG_LOCALE=en_US; RT=\"z=1&dm=nike.com&si=f0af3c6b-ec35-470d-986b-104669ce3ebd&ss=kgg2f55l&sl=3&tt=63h&bcn=%2F%2F684d0d3b.akstat.io%2F&ld=2rv9\"; CONSUMERCHOICE=us/en_us; cid=undefined%7Cundefined; geoloc=cc=NP,rc=,tp=vhigh,tz=GMT+5.75,la=27.67,lo=85.32; feature_enabled__as_nav_rollout=true; audience_segmentation_performed=true; ak_bmsc=F3B37198947690A1010F3EEC8520207817CD7651B87000003C1C8D5F4772D404~plQkp+Ba5Q5U8rjcJHDEMR8JDd3bT4qkyNJKFWIq1luGdb5fPVcEqhkXHQt7m+l4BcQMWMZ+KRGvOkyo4W5E0JYIw6n8LHo0bCSE3i3akDHTkf/yfkRVngV8kAqcuLUex/MM4/lSoAdLK8YTu4mKw4pVlnXqUnUQeTdekIsTFbgxEimTqIof5O17jCk2pnwLqSxTQcarBWHwtnrPTvAdpOJdV0rKWJZSR4YB0N2dnMdhIPRtp9gGqgIemgJUik+BRh; AKA_A2=A; bm_sz=2FC8E496DEB596EC916E0DF8AE49A9BC~YAAQUXbNF2wBp+x0AQAA5VE2Pwnv+DxhJ9bpa069qX+AYvnl3ircq4k1IyImFS7xVosj6w/qHpVOhwDVR4AbmU33eN/lC/CITLCq8GILfROngq7Wu8QQwMBU5BVIw8I7YyOu7jUS2Tcu5v9lK+8Rp4medu9uSF3bdb5k5Q/iburSzgL3cOEnu0SjtJE/UmupHCTMLSRvlNjjA30nW38tMWGlNLvFN12eYzw+5ku+gnrXHTnICl7rwYeBqyZayGk53nSupnzcV2wK2+wAq+9zLGqwgdMxKdy0BLWzBL0=; _abck=AF02B081DB4FE398C3A07B2996B814A9~-1~YAAQZ3bNF3UYHjV1AQAAi1c4PwTXcBczak3nZA0CvbjTDKdxpu4HHGEvgXqEWoe2AEsfuIsev9utpGAn1o+66K54E4rwGn0euAvC0oavJXd9zBJR28XIq6ENFvLkGLlG10wpJoa684z+8RwF+zuNbe8d0znyErWTdiEFiXhpD/zxIICy79NzvaG/Pvf6h2UEfY/l5gX0ZCVVWlnwH+ST4qWeoQ5N00VJKoX3xb10noiPpruBLqNRV0aO+eZthXX2fhuEMHEE6s0wOLc4IkHwObOL+rjvkm+AvK4/LRf/u5MNpLSGbeqVMDqI93jOmB7v4VLJqy2V6Wh7ev3pVE3fforySXEZ85dnk5HiVuyUO2B7Tut/xgNAl0yPPQD71orvA8Ubydj5n5jCaUQmnMqew+ulbn5t1A0PLVgM3NAptBMX8m0j6FPrORLzUolihT5SPq0W94M=~0~-1~-1; nike_locale=us/en_us; bm_sv=D45967773F9BED56FD4FD47D35C43C4F~OlzytJZbhti93nds/WMjN1AeYlfFXzgeHGlUWM8ThBRdYcPmF35RrazTmuUg1zqjhX2OIMCreiL5+Rv6MaOia3S31Ehup0LkueOtMK29rXiw7vblrrUgO/AXYrDI4CCzTxQgRAg9Fk1Hjj2DbD3p2w==; bm_mi=D0EF12EC951AFBCA83A60FC432546A7F~SpTodZ1I1gW3+qp9WLMs4Aqqsl2zr9Q3+Foxi9oONjMhu1iZ2k1hmC02bfT39Ohs0HmJpfU5ryqrOFo10gHIA/CBBvdHA4DX/QMyF4u6NT0yReWXjiU9owf3eleInJgXsmSPLm2HKAGKhcelT2LUl6RZzA54PumH5cQCLg2rIw2Ft220KoigLpvJjD28BZCTJdfvOvxqXbvfh2NOFw64OdPoQo7pjSTVN1+/g6zUhJ8=; ppd=homepage|nikecom>homepage; _gid=GA1.2.413769502.1603083339; visitData={\"visit\":\"1\",\"visitor\":\"19be2c29-92dd-4c7d-a563-22b4e024f265\"}; _uetsid=4eb1ae3011c711eb8180f1f68b67fd64; _uetvid=f04de01c34172d44de90d261e9cfb70e; bc_nike_triggermail=%7B%22distinct_id%22%3A%20%22173f26653b8232-07e11812d031158-7f2c6753-15f900-173f26653b91c0%22%2C%22cart_total%22%3A%200%2C%22ch%22%3A%20%22556396943%22%2C%22bluecoreSiteIsMember%22%3A%20true%2C%22bc_persist_updated%22%3A%201603083329304%2C%22bc_id%22%3A%20-1310386303%7D; _gat_UA-167630499-2=1"
            },
            {
                "name": "Host",
                "value": "unite.nike.com"
            },
            {
                "name": "Origin",
                "value": "https://www.nike.com"
            },
            {
                "name": "Referer",
                "value": "https://www.nike.com/login"
            },
            {
                "name": "TE",
                "value": "Trailers"
            },
            {
                "name": "User-Agent",
                "value": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0"
            }
        ]
    }
}

base_headers = {}

for key in headers.keys():
    for data in headers[key]['headers']:
        base_headers[data['name']] = data['value']



r = requests.get("https://www.nike.com/",headers={**base_headers},cookies=cookies)

with open("login.html","w") as f:
    f.write(r.text)