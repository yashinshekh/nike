import requests

pid = "05c77932-7781-5fc4-8a48-b828007119ca"
skuid = "f119a54c-7594-5a92-a525-5b251bacc6b2"


base_headers = {
    "Host": "api.nike.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.nike.com/launch/t/kobe-5-protro-big-stage?size=12&productId="+str(pid),
    "Origin": "https://www.nike.com",
    "Connection": "keep-alive",
    "TE": "Trailers",
}



#productId  https://api.nike.com/merch/skus/v2/?filter=productId(de739f57-a247-5160-a736-1415b3712b40),country(US)
# skuid https://api.nike.com/merch/skus/v2/?filter=productId(de739f57-a247-5160-a736-1415b3712b40),country(US)


r = requests.put(
    "https://api.nike.com/buy/checkout_previews/v2/ddcdb745-8f00-45eb-92b5-0bd8d062ea68",
    # cookies={
    #     "_abck": "7CDA1A9B43C1FABF84F37B03E1D4EEE0~-1~YAAQFzx8aJXyy95zAQAA0u9r8gQ1EkhuoxWAvWd2OF02Xsz5o6lqvuhgvIvDvHjNbh/ttJntshYnC0qDuslN/qoDrdeb6p122DJ31pu8tD1tFicAh6hJK71fpT7gXi2sW2PfUYifNVgmMNnxk4lM+Kf4K9gICJlWfWk/8J0YT4TGZmxMG53e/KbnOodZ/iIeL0H6gVjaoqVm8+qNs0Cvfq9qjbKKqtRLk//fDU0KsvClj308JPxIcAOlUcttgocYcLr34yv1WHnXtvnSTUIBeWsXL+ad/iqpb4+f7Thpgytq0covWJki4g65y6Sbl388EdYyiuH0rFhE9jsm+sPZm1/j6UlwEAv6/0/sLtZUwig=~-1~-1~-1",
    #     "AMCV_F0935E09512D2C270A490D4D@AdobeOrg": "1994364360|MCMID|00294189374137604813259715564028173940|MCAID|NONE|MCOPTOUT-1597465308s|NONE|vVersion|3.4.0",
    #     "s_ecid": "MCMID|00294189374137604813259715564028173940",
    #     "AnalysisUserId": "da94ad5c-c167-4690-aafe-8f88056ba18c",
    #     "anonymousId": "4B71B72D3661418C396607466AD01852",
    #     "cid": "undefined|undefined",
    #     "_ga": "GA1.2.196654611.1597458108",
    #     "_gid": "GA1.2.1369648122.1597458108",
    #     "_gcl_au": "1.1.1870944954.1597458108",
    #     "fs_uid": "rs.fullstory.com#BM7A6#5578006502522880:5297599244615680/1628994108",
    #     "RT": '"z=1&dm=nike.com&si=14c357e8-364d-4ed6-bf39-497016999f11&ss=kdvpyzv2&sl=c&tt=q3k&bcn=//173e250d.akstat.io/&ld=alx7"',
    #     "cto_bundle": "tkf_BF94enY4M1l4ZDBLejFLN3NXTWp4QlNKM3kzJTJGRGNxUUJtNmt5S3VHSGJ0UGEwSEgwMUQxaFdURHJRYlFOVjA4Y0I4SmY2UEpTT1NoZzBaJTJGVG1acVNpODdCV05CU2p3eGdKaXdGMlk4TW0yMmpLcURJODMzY1RYakVFU2xSR1olMkZQSnpOdVRRZSUyRmZxb1lKTUhOUzAzaWtHdyUzRCUzRA",
    #     "NIKE_CART": "b:c",
    #     "siteCatalyst_sample": "26",
    #     "dreamcatcher_sample": "23",
    #     "neo_sample": "58",
    #     "guidU": "4bdbae0a-6147-4f92-ee84-379bed6784f5",
    #     "sq": "3",
    #     "geoloc": "cc=US,rc=LA,tp=vhigh,tz=CST,la=30.2894,lo=-93.0808",
    #     "AKA_A2": "A",
    #     "ak_bmsc": "72DFA28E81DB2B3724CC961F8E1BB961687C3C17BF46000086E8375F74F9AB44~plZ1bxyeJkqDCaAYLzHhAeKpgqQ8jzhh4U1ALkT/q/O3nuBGEAvG2zRghYoctaSUlMFkSKg0WiOiZMB4DlDPHMUHCINwVdBJUWclWOzAsOmHBbZSz/BtxEa9wCbpvGh3uj5OAtjdAAEJ1AvJmfrw7JB4QA9MYtufALlJa0pB9+RLRZ82NZfTPuy0H3elHVvZlQcRHnc7yoKLAeOjoNyra1qVthlRH4/ICmLqF87G65zK3khd1IIObMKRG+zSXhCc7n",
    #     "bm_sz": "12EA937E575089D3226E566579CA216C~YAAQFzx8aBZwy95zAQAA2k1k8ghowvWQkp21XmIHra/R8yc88ca0ZARSqrFwcC2D59Jg+AdnUlF+sxenleAhf2SJoHonXg+zaOxGHulA3Uy5tTuqyFsX2fghsjmkj2f6rQSEMcfHpTPWRBGGFarNfKgGRQrvO+pSeJxLX7Kw0YXUl/S0ljb5Y8O4pZT4Xw==",
    #     "CONSUMERCHOICE": "us/en_us",
    #     "NIKE_COMMERCE_COUNTRY": "US",
    #     "NIKE_COMMERCE_LANG_LOCALE": "en_US",
    #     "bm_sv": "EC49B4AD7BA4B6296C88B6AF1D49AEEE~aKX9go9lZbK3gvgowxnU3adLGU7YAP06k9rNPcwz2ioYj62Beqw9RKFK/CK+KRzfn0ZAhT4PtH7ONUTE5zhFhhmvqBkbpwhObhIf2TFvzEVkII8XMafFZ9/BGar/JZL5pXfhvJwdiIhMnxNNKD2nYLJfy/GYTY8BrensG0Ppox8=",
    #     "ppd": "checkout|snkrs>checkout>order review",
    #     "guidS": "99203149-1925-4fd2-8fe0-4b6da2f74ca1",
    #     "guidSTimestamp": "1597499533166|1597499954857",
    #     "slCheck": "MtkEh3cI8gchXIn4HrQrAcYE9wU7Zg12Gk46Ld4XSRAqHqOAVhYzDx24FrcCGL791UVSoXGw1+Z4IGOgZ9h0ypJWE+32pvxA35LXAV6qd30xgMA0BAYQGQIv+qVTLsyt",
    #     "lls": "3",
    #     "llCheck": "ble4krlbp1vDy4vDtZSW3Lj59DRpNScFZI7WB98GMOk1dHiD5Uivnkn/+iQGWOYSa1rzyFBrdCwMtC1z3tBEXa72mUZxLGOX4MM+uiDJttxxPnHJ8evD0QU+4VUGzY5X1lg5FWVCGPqCELysliw02a9vOqMafjS2mkpDwTuuAXs=",
    #     "sls": "3",
    #     "cpd": "member|nikecom>member>settings",
    #     "optimizelyEndUserId": "oeu1597499600763r0.8550496391841063",
    #     "RES_TRACKINGID": "567758884036616",
    #     "RES_SESSIONID": "766366506847812",
    #     "ResonanceSegment": "1",
    #     "bc_nike_triggermail": '{"distinct_id": "173f2657d7fbc-06d48f44f36bf2-4c302273-13c680-173f2657d80ba"}',
    #     "co_size": "8.5",
    #     "_uetsid": "bf86dbff5917bf273c7cce95320898cf",
    #     "_uetvid": "5290adcc8795b91d97f1ed636edd6475",
    # },
    headers={
        **base_headers,
        "Accept": "application/json",
        "appid": "com.nike.commerce.snkrs.web",
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImFlYmJkMWMyLTNjNDUtNDM5NS04MGMzLWE3YTIyMmJlOTJmMHNpZyJ9.eyJ0cnVzdCI6MTAwLCJpYXQiOjE1OTc0OTk1NzAsImV4cCI6MTU5NzUwMzE3MCwiaXNzIjoib2F1dGgyYWNjIiwianRpIjoiODAyNzZhNzktNDRiMS00ZTVjLTgwNzQtMjFkMmEwMjQ0ZmNkIiwibGF0IjoxNTk3NDk5NTcwLCJhdWQiOiJjb20ubmlrZS5kaWdpdGFsIiwic3ViIjoiY29tLm5pa2UuY29tbWVyY2Uuc25rcnMud2ViIiwic2J0IjoibmlrZTphcHAiLCJzY3AiOlsiY29tbWVyY2UiXSwicHJuIjoiYTI0MTM1NjQtYjlhOS00NjdlLTg4OGQtMWZhMjI2YjFlZjMyIiwicHJ0IjoibmlrZTpwbHVzIn0.Kuvk13h6OsyE0ecyYmo-6vGhweWoJBk_aZhGHVMwbYNYt-Rj8jSBWWiW_dXMLiuMOL7Wks0bPnqYwBkPgeP3C7wzvZLzbDGPOKersQINGmaObeqrsiFhkI8O_nioEAboQKYTsQJSmsx2S_u4C5UTyLqmzVtSwcDjs1ZXDTAHvy-8vjjVuTuFovh_EBPfZ9oAoiBFQ3sPhuGHj_jM_KKS6R2ab5Vt3MljnoYj7PpncO9mJrCZ3MCr5PQ-J7lcB29yBxwVDZE1619uvAlze1glsH4rI-5UdIX9dJqarrfVfiWc_BNX_J3vpwIAjKFu3GNom6dgYR3BAI8MDzbwl0KKTQ",
        "X-B3-TraceId": "0802a428c8b8e29d",
        "X-B3-SpanId": "06d2ac2cd5e5fa5f",
        "X-B3-ParentSpanId": "51a467b619e0e948",
        "Cookie": '_abck=7CDA1A9B43C1FABF84F37B03E1D4EEE0~-1~YAAQFzx8aJXyy95zAQAA0u9r8gQ1EkhuoxWAvWd2OF02Xsz5o6lqvuhgvIvDvHjNbh/ttJntshYnC0qDuslN/qoDrdeb6p122DJ31pu8tD1tFicAh6hJK71fpT7gXi2sW2PfUYifNVgmMNnxk4lM+Kf4K9gICJlWfWk/8J0YT4TGZmxMG53e/KbnOodZ/iIeL0H6gVjaoqVm8+qNs0Cvfq9qjbKKqtRLk//fDU0KsvClj308JPxIcAOlUcttgocYcLr34yv1WHnXtvnSTUIBeWsXL+ad/iqpb4+f7Thpgytq0covWJki4g65y6Sbl388EdYyiuH0rFhE9jsm+sPZm1/j6UlwEAv6/0/sLtZUwig=~-1~-1~-1; AMCV_F0935E09512D2C270A490D4D%40AdobeOrg=1994364360%7CMCMID%7C00294189374137604813259715564028173940%7CMCAID%7CNONE%7CMCOPTOUT-1597465308s%7CNONE%7CvVersion%7C3.4.0; s_ecid=MCMID%7C00294189374137604813259715564028173940; AnalysisUserId=da94ad5c-c167-4690-aafe-8f88056ba18c; anonymousId=4B71B72D3661418C396607466AD01852; cid=undefined%7Cundefined; _ga=GA1.2.196654611.1597458108; _gid=GA1.2.1369648122.1597458108; _gcl_au=1.1.1870944954.1597458108; fs_uid=rs.fullstory.com#BM7A6#5578006502522880:5297599244615680/1628994108; RT="z=1&dm=nike.com&si=14c357e8-364d-4ed6-bf39-497016999f11&ss=kdvpyzv2&sl=c&tt=q3k&bcn=%2F%2F173e250d.akstat.io%2F&ld=alx7"; cto_bundle=tkf_BF94enY4M1l4ZDBLejFLN3NXTWp4QlNKM3kzJTJGRGNxUUJtNmt5S3VHSGJ0UGEwSEgwMUQxaFdURHJRYlFOVjA4Y0I4SmY2UEpTT1NoZzBaJTJGVG1acVNpODdCV05CU2p3eGdKaXdGMlk4TW0yMmpLcURJODMzY1RYakVFU2xSR1olMkZQSnpOdVRRZSUyRmZxb1lKTUhOUzAzaWtHdyUzRCUzRA; NIKE_CART=b:c; siteCatalyst_sample=26; dreamcatcher_sample=23; neo_sample=58; guidU=4bdbae0a-6147-4f92-ee84-379bed6784f5; sq=3; geoloc=cc=US,rc=LA,tp=vhigh,tz=CST,la=30.2894,lo=-93.0808; AKA_A2=A; ak_bmsc=72DFA28E81DB2B3724CC961F8E1BB961687C3C17BF46000086E8375F74F9AB44~plZ1bxyeJkqDCaAYLzHhAeKpgqQ8jzhh4U1ALkT/q/O3nuBGEAvG2zRghYoctaSUlMFkSKg0WiOiZMB4DlDPHMUHCINwVdBJUWclWOzAsOmHBbZSz/BtxEa9wCbpvGh3uj5OAtjdAAEJ1AvJmfrw7JB4QA9MYtufALlJa0pB9+RLRZ82NZfTPuy0H3elHVvZlQcRHnc7yoKLAeOjoNyra1qVthlRH4/ICmLqF87G65zK3khd1IIObMKRG+zSXhCc7n; bm_sz=12EA937E575089D3226E566579CA216C~YAAQFzx8aBZwy95zAQAA2k1k8ghowvWQkp21XmIHra/R8yc88ca0ZARSqrFwcC2D59Jg+AdnUlF+sxenleAhf2SJoHonXg+zaOxGHulA3Uy5tTuqyFsX2fghsjmkj2f6rQSEMcfHpTPWRBGGFarNfKgGRQrvO+pSeJxLX7Kw0YXUl/S0ljb5Y8O4pZT4Xw==; CONSUMERCHOICE=us/en_us; NIKE_COMMERCE_COUNTRY=US; NIKE_COMMERCE_LANG_LOCALE=en_US; bm_sv=EC49B4AD7BA4B6296C88B6AF1D49AEEE~aKX9go9lZbK3gvgowxnU3adLGU7YAP06k9rNPcwz2ioYj62Beqw9RKFK/CK+KRzfn0ZAhT4PtH7ONUTE5zhFhhmvqBkbpwhObhIf2TFvzEVkII8XMafFZ9/BGar/JZL5pXfhvJwdiIhMnxNNKD2nYLJfy/GYTY8BrensG0Ppox8=; ppd=checkout|snkrs>checkout>order%20review; guidS=99203149-1925-4fd2-8fe0-4b6da2f74ca1; guidSTimestamp=1597499533166|1597499954857; slCheck=MtkEh3cI8gchXIn4HrQrAcYE9wU7Zg12Gk46Ld4XSRAqHqOAVhYzDx24FrcCGL791UVSoXGw1+Z4IGOgZ9h0ypJWE+32pvxA35LXAV6qd30xgMA0BAYQGQIv+qVTLsyt; lls=3; llCheck=ble4krlbp1vDy4vDtZSW3Lj59DRpNScFZI7WB98GMOk1dHiD5Uivnkn/+iQGWOYSa1rzyFBrdCwMtC1z3tBEXa72mUZxLGOX4MM+uiDJttxxPnHJ8evD0QU+4VUGzY5X1lg5FWVCGPqCELysliw02a9vOqMafjS2mkpDwTuuAXs=; sls=3; cpd=member|nikecom>member>settings; optimizelyEndUserId=oeu1597499600763r0.8550496391841063; RES_TRACKINGID=567758884036616; RES_SESSIONID=766366506847812; ResonanceSegment=1; bc_nike_triggermail=%7B%22distinct_id%22%3A%20%22173f2657d7fbc-06d48f44f36bf2-4c302273-13c680-173f2657d80ba%22%7D; co_size=8.5; _uetsid=bf86dbff5917bf273c7cce95320898cf; _uetvid=5290adcc8795b91d97f1ed636edd6475',
    },
    json={"request":{"email":"nischal.aryalty@gmail.com","country":"US","currency":"USD","locale":"en_US","channel":"SNKRS","clientInfo":{"deviceId":"0400CIfeAe15Cx8Nf94lis1ztjyRWpJUpQh+6/Ao2WE9gwqiRlixFE9uokqr6JjTMPRUWpRKnZWQmlqQqC/1vGJeln4B0MBHqt8ydik+BCIRXKJ0Pq5SDE3sFfMGeBJpb9TWP8qFSAZ42op95eoW86m0k9uux78+1SurJGAyT9LXrb7wVY9aG9/nrC1n0ozyxtXbZJH9gN5Fgi0V1uKgdfXRzjC3o7rRuIcSQuK/Lhpe/UsoDvlKqcW/vgHzj486sjgyUO+AInpd+UykzlhvKatVjhLVg2uhVbY78ysldFOVsFgv0nLv/jsDO5gWSO2+NA4Z1PGS9g4tRot8nTs/3e3TI3A+k9XRlIy/uUtzXhPDwdnj63kQgzZyPnFlJCWkjZy2D9I+WP8iW7T5nVHgqPS37ETKxXG8JJDHxA9x3qRKbjObZRutTbZvc93pZ/WuuaUQwj8P8KRxzaGjYmLrUKTmt2IexFSsDpBLFsF83Kpm3K25LqBNk4kdSilCz8QbOZkvdu4bMIE4yvytQqBfrJX4CYyuZLBMPTKD/pr71oD561r3o165QaLfQBLAFdmEsbtrJdp4gN+mEzSEKJ5sETrogpipU8Y+CT5OVQLI/nuq72WjU7n9xk3dwf7uzpZjbtz53kdITC3Lm7bIB9QxnksoWoWXzUILvpZkpdqSgJrtcJZJNPSTmMV8PkfLH/JZWu2VrI3MaSYrgzvK825aVpZM/CT/riUqiozfAOitx40UDza/slJ9rBwgiJI7ISgtaMhIsj69LfM7VRYrI1FeHSbDspvXHhwykQoiE53T97CusKlE42ys2aVDQcSm+xRvn4mvyorim+6kWksAoV8x9KfXlgm68rvRvAGkcYv1IEAR88cFJGkaA+tmVWEos54Hyaek6AYOPtdcTCMGS5+T399xR87YrajVnBUdXGOkjyIS4+jIP5CtRTTgr9PEHDh2HWsIiRq4bnOhFkXoMW1ohZqyNX6mAJ3ZTHu22dBsS3fnOJTxpdsaS2lbG3A+k9XRlIy/uUtzXhPDwdnj63kQgzZyPnFlJCWkjZy2D9I+WP8iW7T5nVHgqPS37IC64CoOx4YA4yvRhXnDkItcyigokVvvMQA3zolt1kOfbDyI3xIc28v80eA0eB8S/cdq5O8NwL0ymoJ9YWBJl5I="},"items":[{"id":pid,"skuId":skuid,"quantity":1,"recipient":{"firstName":"Nischal","lastName":"Aryal"},"shippingAddress":{"address1":"807 Walters St.","address2":"47","city":"Lake Charles","state":"LA","postalCode":"70607","country":"US"},"contactInfo":{"email":"nischal.aryalty@gmail.com","phoneNumber":"3374476456"},"shippingMethod":"STANDARD"}]}}
)

print(r.text)