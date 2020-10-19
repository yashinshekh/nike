import requests
base_headers = {
    "Host": "api.nike.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.nike.com/launch/t/kobe-5-protro-big-stage?size=12&productId=05c77932-7781-5fc4-8a48-b828007119ca",
    "Origin": "https://www.nike.com",
    "Connection": "keep-alive",
    "TE": "Trailers",
}

cookies = {"_abck":"9D4398D5700D998021F46936B25D604E~-1~YAAQFjZ8aFudrwJ0AQAAORhAGwTQKYzZeDvF+aioBYUR4MTQ9dqrWut4j0gSd3aKhhzoKoQz+qvp8EqfP/6xD3xU6QDIc56bDQ4yg55+mFTwQsUyew1sVQJzDgZUJKKUv+OUkLnyuhwLpY5usX79QbuEkHUJwcyJwK34zw7L+m5oBhE3bCWopyThE4Rh2TIsMrLpsMOE6ihMOb4Z/Xolt5AT4lGgEaLIZRLVqSU3JHJmtJ8WKd8E4eez5V7UpPYlgGJ5DderYtiFFwUzKvVmO7Jp6GeWaox8okNpJ+3/8A0gG62mhqfqAIcdO3wc71174epRdhiIsLzYW14tR6cGeW15ISt+/XNNHWI8oOJX/UQ=~-1~-1~-1","_derived_epik":"dj0yJnU9bDkzN3lfN0VicnZCWEk0RkU0ckcxSk9udm42aE9hSXkmbj1KSkU2OWZ2TWNTZW1TZGpIOXFBZnN3Jm09MSZ0PUFBQUFBRjg0dWcwJnJtPTEmcnQ9QUFBQUFGODR1ZzA","_fbp":"fb.1.1597552061317.1648663435","_ga":"GA1.2.752594614.1597116714","_gcl_au":"1.1.479043779.1597116712","_gid":"GA1.2.351501318.1598153969","_pin_unauth":"dWlkPVpHVXhNelV4WmpVdE56STBPUzAwWmpJekxXSTVORGd0TWpBMVpXSmxaREJtTnpneiZycD1kSEoxWlE","_scid":"59c7c1b0-3d66-4b99-bbb8-fcca8c9c03db","_sctr":"1|1597515300000","_uetsid":"aaaee3630f1f6f30302bbd811f7a4bba","_uetvid":"f04de01c34172d44de90d261e9cfb70e","ak_bmsc":"1BE034A1E4D72D97B311A282679719BF687C3616DC7F00000151425FEA416C3F~pll7ndkg/4iPoivhoU+7KsrGtE/gfpiNeZS/d4KT8MSQnA9qtYtDjSuZDypO+heFM1Uyu1mTL/K++xcQUtNoF6O/ingw6TKiVOd3cFIYYtebDe/YnoODjBEORmyyjIuasoVBX2YM+cDc+7LPXRRASQaKJR+0/n2hPYTr575YVDJ+4vMekulIgBvYuJ3Y3mznu4izR/WXWcypGJHLYmVgtkCYyQfVj35MuScHwS95P4cdOZoXqVk21EeI2fdgrcpBHA","AKA_A2":"A","AMCV_F0935E09512D2C270A490D4D@AdobeOrg":"1994364360|MCMID|33389469561038572447356666046441492316|MCAID|NONE|MCOPTOUT-1597123911s|NONE|vVersion|3.4.0","AnalysisUserId":"844520c0-eb46-4ff7-8775-9a2b88884903","anonymousId":"32267D718C54CCA23AC7F4101A04C615","audience_segmentation_performed":"true","bc_nike_new_zealand_triggermail":"{\"distinct_id\": \"173f585e56a3b7-082fedd8fc26e78-7f2c6753-15f900-173f585e56b1a8\",\"cart_total\": 0}","bc_nike_triggermail":"{\"distinct_id\": \"173f26653b8232-07e11812d031158-7f2c6753-15f900-173f26653b91c0\",\"cart_total\": 0,\"ch\": \"556396943\"}","bm_mi":"D88DF56F0BF912BD0312C6AE1CA93539~2Mr4vNKSQLwTAWusRLDIOnOFD5PFwJWwk5ghRdJSRfz0sP7DkV2r6iLmrRDlXknSe4BIwxCN6Q8vPSI3GOf4AFnE/fLvg/gvroHIeUr4NhqewsIK80nLt7dEH/JFNKWp4vDl9g3n2OtQpXxUuwrU+1cBAh4p26qLQ4g3m/2oHMFrhCNB4v1rm0bR2uAfOkYbFqgGhZqmqvgALuQr7Mt/LAnMfRtZI9kO2l3mkPqXTDdiLWYdCkHr+qjFkpp6kcI78Lihe5gEhLzpUYlAsvw8nQ==","bm_sv":"D883DE68A7DE80A95ECA034586E72EED~O8kVv14CT1Fq/7DGsGbLxdOiz94xMI4tZv4+rnkkpacoH79f3dS20Z0X0iEXdlPI7GZgHN7FNPD946ZulFNr0WqACdUwea3aICvao9IxhCUwXzAyf4Oa9486N+ZO6wgzYOUFe0V6G4qldKE1VZA52THxs6EnbZGRigtB4Daspeg=","bm_sz":"EFBC077169FEC0EDF3F8FF4790725B1C~YAAQFjZ8aDMgrwJ0AQAAtWsMGwhMVObnV6pQ87RzItJpz0UMS2D56RYd0mPd9C8NJxSmsxnnEMvtG9E9NCgzexkIJYnF5kTnRzR7JBLzJkIuoc9LHsQw98Uxf33InxWPb73Hb2mobFeN1tbnO6bVxfXbt0vzT/33oN7B49B8ll3Bg9DgiJRggl+j4pQQHw==","bounceClientVisit2436":"N4IgZgbgLiBcCMBWAnAdkYgzPAbDgNCBAJYAmcSaG2ALKgByoAMi88hAhgPZxOEA2ABzggAFlCiCAzgFJMAQRkAmAGLKVAdy0A6AHbEA1gFNtAYy4BbdboBe6kJym9CEQRDhLC5WCHKEATiIOIKbQFCjoWPB0hFJkcDSEAOamgbBKfCAWzr7xPhnwLEw4yDSIzMjIiEo4GMH8YQgR1Lg4AL5AA","cid":"4942550|2ec0f4ffdb8311ea829301d20a180510","CONSUMERCHOICE":"us/en_us","CONSUMERCHOICE_SESSION":"t","cto_bundle":"BXEddF9HNmxwWUFkT05FeFNzQiUyRmwza2JSOFhSR1J2Q1AlMkZyRU44VVY3OTd2VWlhRGclMkJXRmtVQk5zNkcxckFxJTJCQjU3MiUyRjFVcXQzZzFJUkhwM3ozRjYlMkZTUElUbmt1ZWN6eUcxM1BvTVJrY0FjM1dlb1hSb3klMkYzbU9pTTNyTlQ3cTVXdTZ3bW9xWFRFOCUyQkFSWSUyRnkxdnBId2Njc0ElM0QlM0Q","dreamcatcher_sample":"92","feature_enabled__as_esi_noop":"true","feature_tests":"as_esi_noop_test:variation_2","geoloc":"cc=NP,rc=,tp=vhigh,tz=GMT+5.75,la=27.67,lo=85.32","guidS":"7e64e196-b721-4ad8-a100-87c37ed368b7","guidSTimestamp":"1598181650558|1598182294355","guidU":"b21e3988-7ec5-42ec-cf2e-2d79bbf9da0a","llCheck":"fdertfxGTSqrPuCmFeWn/sOYNBzhEpe6XhZTIbLRnSPCQ2FXNvIg2OIdJvI92eC1a1rzyFBrdCwMtC1z3tBEXa72mUZxLGOX4MM+uiDJttwpllZRclNk8ZzjYGtnuxTPhbZ6eFiL+Qw67aawPrLEVFm0XWqMIadyJfFq6kIriY0=","lls":"3","neo_sample":"94","NIKE_CART":"b:c","NIKE_COMMERCE_COUNTRY":"US","NIKE_COMMERCE_LANG_LOCALE":"en_US","nike_locale":"us/en_us","optimizelyEndUserId":"oeu1597930126743r0.697496215128809","ppd":"homepage|nikecom>homepage","RES_TRACKINGID":"282558582937435","ResonanceSegment":"1","RT":"\"z=1&dm=nike.com&si=aff8f5db-c781-4fc2-9e52-cbf8f2d6cf2e&ss=ke70gx0p&sl=1&tt=626&bcn=//684d0d3e.akstat.io/&ld=1j0ah\"","s_ecid":"MCMID|33389469561038572447356666046441492316","siteCatalyst_sample":"52","sq":"3","visitData":"{\"visit\":\"2\",\"visitor\":\"1c8436ea-a8c3-4d30-8a77-4b60d87827b5\"}"}


username = "nischal.aryalty@gmail.com"
password = "1Nepal23Metallica007!"

s = requests.Session()


r = s.post(
    url="https://unite.nike.com/login?appVersion=807&experienceVersion=807&uxid=com.nike.commerce.nikedotcom.web&locale=en_US&backendEnvironment=identity&browser=&os=Linux x86_64&mobile=false&native=false&visit=2",
    json={"client_id":"HlHa2Cje3ctlaOqnxvgZXNaAs7T9nAuH","grant_type":"password","password":"1Nepal23Metallica007!","username":"nischal.aryalty@gmail.com","ux_id":"com.nike.commerce.nikedotcom.web"},
    headers={**base_headers},
    cookies=cookies
)

with open("test.html","w") as f:
    f.write(r.text)







# r = requests.post(
#     "https://api.nike.com/payment/preview/v2",
#     cookies=cookies,
#     headers={
#         **base_headers,
#         "appid": "com.nike.commerce.snkrs.web",
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImFlYmJkMWMyLTNjNDUtNDM5NS04MGMzLWE3YTIyMmJlOTJmMHNpZyJ9.eyJ0cnVzdCI6MTAwLCJpYXQiOjE1OTc0OTk1NzAsImV4cCI6MTU5NzUwMzE3MCwiaXNzIjoib2F1dGgyYWNjIiwianRpIjoiODAyNzZhNzktNDRiMS00ZTVjLTgwNzQtMjFkMmEwMjQ0ZmNkIiwibGF0IjoxNTk3NDk5NTcwLCJhdWQiOiJjb20ubmlrZS5kaWdpdGFsIiwic3ViIjoiY29tLm5pa2UuY29tbWVyY2Uuc25rcnMud2ViIiwic2J0IjoibmlrZTphcHAiLCJzY3AiOlsiY29tbWVyY2UiXSwicHJuIjoiYTI0MTM1NjQtYjlhOS00NjdlLTg4OGQtMWZhMjI2YjFlZjMyIiwicHJ0IjoibmlrZTpwbHVzIn0.Kuvk13h6OsyE0ecyYmo-6vGhweWoJBk_aZhGHVMwbYNYt-Rj8jSBWWiW_dXMLiuMOL7Wks0bPnqYwBkPgeP3C7wzvZLzbDGPOKersQINGmaObeqrsiFhkI8O_nioEAboQKYTsQJSmsx2S_u4C5UTyLqmzVtSwcDjs1ZXDTAHvy-8vjjVuTuFovh_EBPfZ9oAoiBFQ3sPhuGHj_jM_KKS6R2ab5Vt3MljnoYj7PpncO9mJrCZ3MCr5PQ-J7lcB29yBxwVDZE1619uvAlze1glsH4rI-5UdIX9dJqarrfVfiWc_BNX_J3vpwIAjKFu3GNom6dgYR3BAI8MDzbwl0KKTQ",
#         "X-B3-TraceId": "0802a428c8b8e29d",
#         "X-B3-SpanId": "06d2ac2cd5e5fa5f",
#         "X-B3-ParentSpanId": "51a467b619e0e948",
#         "Cookie": '_abck=7CDA1A9B43C1FABF84F37B03E1D4EEE0~-1~YAAQFzx8aJXyy95zAQAA0u9r8gQ1EkhuoxWAvWd2OF02Xsz5o6lqvuhgvIvDvHjNbh/ttJntshYnC0qDuslN/qoDrdeb6p122DJ31pu8tD1tFicAh6hJK71fpT7gXi2sW2PfUYifNVgmMNnxk4lM+Kf4K9gICJlWfWk/8J0YT4TGZmxMG53e/KbnOodZ/iIeL0H6gVjaoqVm8+qNs0Cvfq9qjbKKqtRLk//fDU0KsvClj308JPxIcAOlUcttgocYcLr34yv1WHnXtvnSTUIBeWsXL+ad/iqpb4+f7Thpgytq0covWJki4g65y6Sbl388EdYyiuH0rFhE9jsm+sPZm1/j6UlwEAv6/0/sLtZUwig=~-1~-1~-1; AMCV_F0935E09512D2C270A490D4D%40AdobeOrg=1994364360%7CMCMID%7C00294189374137604813259715564028173940%7CMCAID%7CNONE%7CMCOPTOUT-1597465308s%7CNONE%7CvVersion%7C3.4.0; s_ecid=MCMID%7C00294189374137604813259715564028173940; AnalysisUserId=da94ad5c-c167-4690-aafe-8f88056ba18c; anonymousId=4B71B72D3661418C396607466AD01852; cid=undefined%7Cundefined; _ga=GA1.2.196654611.1597458108; _gid=GA1.2.1369648122.1597458108; _gcl_au=1.1.1870944954.1597458108; fs_uid=rs.fullstory.com#BM7A6#5578006502522880:5297599244615680/1628994108; RT="z=1&dm=nike.com&si=14c357e8-364d-4ed6-bf39-497016999f11&ss=kdvpyzv2&sl=c&tt=q3k&bcn=%2F%2F173e250d.akstat.io%2F&ld=alx7"; cto_bundle=tkf_BF94enY4M1l4ZDBLejFLN3NXTWp4QlNKM3kzJTJGRGNxUUJtNmt5S3VHSGJ0UGEwSEgwMUQxaFdURHJRYlFOVjA4Y0I4SmY2UEpTT1NoZzBaJTJGVG1acVNpODdCV05CU2p3eGdKaXdGMlk4TW0yMmpLcURJODMzY1RYakVFU2xSR1olMkZQSnpOdVRRZSUyRmZxb1lKTUhOUzAzaWtHdyUzRCUzRA; NIKE_CART=b:c; siteCatalyst_sample=26; dreamcatcher_sample=23; neo_sample=58; guidU=4bdbae0a-6147-4f92-ee84-379bed6784f5; sq=3; geoloc=cc=US,rc=LA,tp=vhigh,tz=CST,la=30.2894,lo=-93.0808; AKA_A2=A; ak_bmsc=72DFA28E81DB2B3724CC961F8E1BB961687C3C17BF46000086E8375F74F9AB44~plZ1bxyeJkqDCaAYLzHhAeKpgqQ8jzhh4U1ALkT/q/O3nuBGEAvG2zRghYoctaSUlMFkSKg0WiOiZMB4DlDPHMUHCINwVdBJUWclWOzAsOmHBbZSz/BtxEa9wCbpvGh3uj5OAtjdAAEJ1AvJmfrw7JB4QA9MYtufALlJa0pB9+RLRZ82NZfTPuy0H3elHVvZlQcRHnc7yoKLAeOjoNyra1qVthlRH4/ICmLqF87G65zK3khd1IIObMKRG+zSXhCc7n; bm_sz=12EA937E575089D3226E566579CA216C~YAAQFzx8aBZwy95zAQAA2k1k8ghowvWQkp21XmIHra/R8yc88ca0ZARSqrFwcC2D59Jg+AdnUlF+sxenleAhf2SJoHonXg+zaOxGHulA3Uy5tTuqyFsX2fghsjmkj2f6rQSEMcfHpTPWRBGGFarNfKgGRQrvO+pSeJxLX7Kw0YXUl/S0ljb5Y8O4pZT4Xw==; CONSUMERCHOICE=us/en_us; NIKE_COMMERCE_COUNTRY=US; NIKE_COMMERCE_LANG_LOCALE=en_US; bm_sv=EC49B4AD7BA4B6296C88B6AF1D49AEEE~aKX9go9lZbK3gvgowxnU3adLGU7YAP06k9rNPcwz2ioYj62Beqw9RKFK/CK+KRzfn0ZAhT4PtH7ONUTE5zhFhhmvqBkbpwhObhIf2TFvzEWBPHM2jq1n801fZikAgDQkHbxn5XLu7BKu6lRMbr3kU3q9g2IPqUkPbwApnb+lw2w=; ppd=checkout|snkrs>checkout>order%20review; guidS=99203149-1925-4fd2-8fe0-4b6da2f74ca1; guidSTimestamp=1597499533166|1597499954857; slCheck=MtkEh3cI8gchXIn4HrQrAcYE9wU7Zg12Gk46Ld4XSRAqHqOAVhYzDx24FrcCGL791UVSoXGw1+Z4IGOgZ9h0ypJWE+32pvxA35LXAV6qd30xgMA0BAYQGQIv+qVTLsyt; lls=3; llCheck=ble4krlbp1vDy4vDtZSW3Lj59DRpNScFZI7WB98GMOk1dHiD5Uivnkn/+iQGWOYSa1rzyFBrdCwMtC1z3tBEXa72mUZxLGOX4MM+uiDJttxxPnHJ8evD0QU+4VUGzY5X1lg5FWVCGPqCELysliw02a9vOqMafjS2mkpDwTuuAXs=; sls=3; cpd=member|nikecom>member>settings; optimizelyEndUserId=oeu1597499600763r0.8550496391841063; RES_TRACKINGID=567758884036616; RES_SESSIONID=766366506847812; ResonanceSegment=1; bc_nike_triggermail=%7B%22distinct_id%22%3A%20%22173f2657d7fbc-06d48f44f36bf2-4c302273-13c680-173f2657d80ba%22%7D; co_size=8.5; _uetsid=bf86dbff5917bf273c7cce95320898cf; _uetvid=5290adcc8795b91d97f1ed636edd6475',
#     },
#     json={"checkoutId":"ddcdb745-8f00-45eb-92b5-0bd8d062ea68","total":180,"currency":"USD","country":"US","items":[{"productId":"05c77932-7781-5fc4-8a48-b828007119ca","shippingAddress":{"firstName":"Nischal","lastName":"Aryal","address1":"807 Walters St.","address2":"47","city":"Lake Charles","state":"LA","postalCode":"70607","phoneNumber":"3374476456","country":"US","region":"na","id":"94a2a35f-0561-4ee8-a11f-055058ad63dc","preferred":True}}],"paymentInfo":[{"id":"pidf6f122e5-9afe-4985-9fcf-82a749449c63","billingInfo":{"name":{"firstName":"Nischal","lastName":"Aryal"},"address":{"firstName":"Nischal","lastName":"Aryal","address1":"807 Walters St.","address2":"153","city":"Lake Charles","state":"LA","postalCode":"70607","country":"US","phoneNumber":"3374476456"},"contactInfo":{"phoneNumber":"3374476456","email":"nischal.aryalty@gmail.com"}},"type":"CreditCard","paymentId":"pidf6f122e5-9afe-4985-9fcf-82a749449c63"}]}
# )
#
#
#
# print(r.text)