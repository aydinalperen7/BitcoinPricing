import requests

cookies = {
    '__utma': '10102256.1065507994.1711579351.1713151801.1713209667.3',
    '__utmc': '10102256',
    '__utmz': '10102256.1713209667.3.3.utmcsr=trends.google.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    '__utmt': '1',
    '__utmb': '10102256.2.9.1713209670081',
    '__Secure-ENID': '12.SE=i-s6eWOWGC41LKnoxf5sK49oKBXhf1YWOsrUSia2pf5SoMPmQfmfGqKbGbqUQCA9m0CzpEO4olACgfoEoZ0BAKwKfLSTYLRYe8DfKDGUwpmFH-XYEIyF35LeVhmYjEQia19_8YbWGC6h78E1-b0__4TlaoWzXJv1ym-Gb79H-Byk0dTnD8uw7RShEAhRPaTr5MsFW0TEWrHCWpKA1--uzmvIhJcEVgisthDiofGe-RT_01pHqsJERkmY5rJ66hGUdc0',
    'SEARCH_SAMESITE': 'CgQI75kB',
    'OTZ': '7487923_76_80_104160_76_446820',
    'SID': 'g.a000iAhQJFx68zWybo1ka0KSpZGkFyShvyRz5_ho_Df2H7rX9iYwNrKgzLAGoEZrpidmKScGgQACgYKAX4SAQASFQHGX2MiMdq7NaXeOhoZVwzlcdWdlxoVAUF8yKr-xeDGLOc55dJMormiypyz0076',
    '__Secure-1PSID': 'g.a000iAhQJFx68zWybo1ka0KSpZGkFyShvyRz5_ho_Df2H7rX9iYwaRLqJNHIANTsFMpmROGU3gACgYKAd0SAQASFQHGX2Mi3yQgiMQAj8KOSBSKEW35qxoVAUF8yKrMWostA2d-oh22Befpjh3N0076',
    '__Secure-3PSID': 'g.a000iAhQJFx68zWybo1ka0KSpZGkFyShvyRz5_ho_Df2H7rX9iYw8kXth9OdK_bEAnBS6LMSEgACgYKAT8SAQASFQHGX2Mi_Gmi1PdI_5f9fLR5r-U5-BoVAUF8yKqZbcyrV-hwIpjNHAoNCgvd0076',
    'HSID': 'AcCeSplMp1-i0efp4',
    'SSID': 'Aj1I1qCvjUEobMEzt',
    'APISID': 'hGw-x4cAwzq1WYmb/A0AYLFHlEvj39Fmuf',
    'SAPISID': 'n51k6TkTDi2sch1e/AgkJuLDLBVR8tmszv',
    '__Secure-1PAPISID': 'n51k6TkTDi2sch1e/AgkJuLDLBVR8tmszv',
    '__Secure-3PAPISID': 'n51k6TkTDi2sch1e/AgkJuLDLBVR8tmszv',
    'AEC': 'AQTF6HwU6YcVsLLCNWWgnkmoaYZ4LDdkjHQix48kooojbUy7SkNexCY7bw',
    '__Secure-1PSIDTS': 'sidts-CjEB7F1E_N8yKGXPShQkv4AoYSwlq7CR-msB48Fe7OIj0vZ-rqYU17PHr07-9C6Dq-OlEAA',
    '__Secure-3PSIDTS': 'sidts-CjEB7F1E_N8yKGXPShQkv4AoYSwlq7CR-msB48Fe7OIj0vZ-rqYU17PHr07-9C6Dq-OlEAA',
    '_gid': 'GA1.3.526307513.1713151793',
    'NID': '513=QKSy30cX73x8rEY4NIkkmNMRBDR3E2ytii0XO5yCkbuKp12FWPpuJ1Li5EWXEw0VIJlK8RVSUmVUnRGfOdhhp88p-pvBblMVSnlldj7he2iS0r698nFBMkGcQQFce3Kbh_bAd4p-AqEXYUgNE5b8QJENpfRg-DvImjW7hRFWjp00NeBVwh0jsi3R7wjKyJnR4vDJV0Kza6DHifFOfb6QHfSTP54bsKIJFU4idJS2OMw6QdDB9JvexQCM43Ql73a2rALVeKTPRYG4Vkme2Rrz8dSRDxq2-J6FJ_nu-6dRkXE-8mqEbCbir06n8NBNmhuekRN-Sh7weUaEoQ10FTF2bOstL0KU20nY7J-2rwDm9NxMrvlO9z0HK-I7zDVDhsb5R0N0kWMaQBB74heSfd3QmcLHjDsAHVMyBUompB6MlyXVy4sfaKN1fiRwqxjG5R6_ORXjHIgV5b2-a6x9euhA1J5hPiXRBsNWj_yIdFXWpCCmrngHyBklMgCOxWOTdzeup4MrQlqeFkFSHmAtNfxgDkR9siBRc55cCQTpv_vymI41CMjMV1TVLqyF-N0BM7QeQXPAIYCxps7dv8zX_7JUMOaUU9_jGiHN_pHf9JwV0GdPIpCSqOKle_fdyXxK482Va0yCbxyXz4HsIfBaBK1wcPBhCg7CMazVzvC-BEWFPink6xfe_Oul55D2MTQVuhQl49mfHjrOSHeID_HWya3b3O1EqOs89rPjmsRe3na5eJI6vTUcicWrxYvBjiEt30EoP3l0Gsof7MksfwbXeulNKTOZBBneovziFFsM7al6ubXJJVU',
    '_ga': 'GA1.3.1065507994.1711579351',
    '_gat_gtag_UA_4401283': '1',
    'SIDCC': 'AKEyXzUu9vXIKws4olXdh5XDUMoQDCRu1ESdB7GqpvVF1JiW3dK7Fze-kfRjEvckN-96alP_yhQ',
    '__Secure-1PSIDCC': 'AKEyXzWUWzwBoHZ7kve0Y-Sn3o_slhPjdGkVC_LYfSI3LzJNhVibPilyxgDVf2cS5BCw3lx62ZWw',
    '__Secure-3PSIDCC': 'AKEyXzX9hNTuPuVvfHGnPTLLGOlbLIX7Up4TYUPX2Qauv0bxWdRW58hJeE2mQx7Y34rRLV_g1jo8',
    '_ga_VWZPXDNJJB': 'GS1.1.1713209635.3.1.1713209721.0.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '__utma=10102256.1065507994.1711579351.1713151801.1713209667.3; __utmc=10102256; __utmz=10102256.1713209667.3.3.utmcsr=trends.google.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; __utmb=10102256.2.9.1713209670081; __Secure-ENID=12.SE=i-s6eWOWGC41LKnoxf5sK49oKBXhf1YWOsrUSia2pf5SoMPmQfmfGqKbGbqUQCA9m0CzpEO4olACgfoEoZ0BAKwKfLSTYLRYe8DfKDGUwpmFH-XYEIyF35LeVhmYjEQia19_8YbWGC6h78E1-b0__4TlaoWzXJv1ym-Gb79H-Byk0dTnD8uw7RShEAhRPaTr5MsFW0TEWrHCWpKA1--uzmvIhJcEVgisthDiofGe-RT_01pHqsJERkmY5rJ66hGUdc0; SEARCH_SAMESITE=CgQI75kB; OTZ=7487923_76_80_104160_76_446820; SID=g.a000iAhQJFx68zWybo1ka0KSpZGkFyShvyRz5_ho_Df2H7rX9iYwNrKgzLAGoEZrpidmKScGgQACgYKAX4SAQASFQHGX2MiMdq7NaXeOhoZVwzlcdWdlxoVAUF8yKr-xeDGLOc55dJMormiypyz0076; __Secure-1PSID=g.a000iAhQJFx68zWybo1ka0KSpZGkFyShvyRz5_ho_Df2H7rX9iYwaRLqJNHIANTsFMpmROGU3gACgYKAd0SAQASFQHGX2Mi3yQgiMQAj8KOSBSKEW35qxoVAUF8yKrMWostA2d-oh22Befpjh3N0076; __Secure-3PSID=g.a000iAhQJFx68zWybo1ka0KSpZGkFyShvyRz5_ho_Df2H7rX9iYw8kXth9OdK_bEAnBS6LMSEgACgYKAT8SAQASFQHGX2Mi_Gmi1PdI_5f9fLR5r-U5-BoVAUF8yKqZbcyrV-hwIpjNHAoNCgvd0076; HSID=AcCeSplMp1-i0efp4; SSID=Aj1I1qCvjUEobMEzt; APISID=hGw-x4cAwzq1WYmb/A0AYLFHlEvj39Fmuf; SAPISID=n51k6TkTDi2sch1e/AgkJuLDLBVR8tmszv; __Secure-1PAPISID=n51k6TkTDi2sch1e/AgkJuLDLBVR8tmszv; __Secure-3PAPISID=n51k6TkTDi2sch1e/AgkJuLDLBVR8tmszv; AEC=AQTF6HwU6YcVsLLCNWWgnkmoaYZ4LDdkjHQix48kooojbUy7SkNexCY7bw; __Secure-1PSIDTS=sidts-CjEB7F1E_N8yKGXPShQkv4AoYSwlq7CR-msB48Fe7OIj0vZ-rqYU17PHr07-9C6Dq-OlEAA; __Secure-3PSIDTS=sidts-CjEB7F1E_N8yKGXPShQkv4AoYSwlq7CR-msB48Fe7OIj0vZ-rqYU17PHr07-9C6Dq-OlEAA; _gid=GA1.3.526307513.1713151793; NID=513=QKSy30cX73x8rEY4NIkkmNMRBDR3E2ytii0XO5yCkbuKp12FWPpuJ1Li5EWXEw0VIJlK8RVSUmVUnRGfOdhhp88p-pvBblMVSnlldj7he2iS0r698nFBMkGcQQFce3Kbh_bAd4p-AqEXYUgNE5b8QJENpfRg-DvImjW7hRFWjp00NeBVwh0jsi3R7wjKyJnR4vDJV0Kza6DHifFOfb6QHfSTP54bsKIJFU4idJS2OMw6QdDB9JvexQCM43Ql73a2rALVeKTPRYG4Vkme2Rrz8dSRDxq2-J6FJ_nu-6dRkXE-8mqEbCbir06n8NBNmhuekRN-Sh7weUaEoQ10FTF2bOstL0KU20nY7J-2rwDm9NxMrvlO9z0HK-I7zDVDhsb5R0N0kWMaQBB74heSfd3QmcLHjDsAHVMyBUompB6MlyXVy4sfaKN1fiRwqxjG5R6_ORXjHIgV5b2-a6x9euhA1J5hPiXRBsNWj_yIdFXWpCCmrngHyBklMgCOxWOTdzeup4MrQlqeFkFSHmAtNfxgDkR9siBRc55cCQTpv_vymI41CMjMV1TVLqyF-N0BM7QeQXPAIYCxps7dv8zX_7JUMOaUU9_jGiHN_pHf9JwV0GdPIpCSqOKle_fdyXxK482Va0yCbxyXz4HsIfBaBK1wcPBhCg7CMazVzvC-BEWFPink6xfe_Oul55D2MTQVuhQl49mfHjrOSHeID_HWya3b3O1EqOs89rPjmsRe3na5eJI6vTUcicWrxYvBjiEt30EoP3l0Gsof7MksfwbXeulNKTOZBBneovziFFsM7al6ubXJJVU; _ga=GA1.3.1065507994.1711579351; _gat_gtag_UA_4401283=1; SIDCC=AKEyXzUu9vXIKws4olXdh5XDUMoQDCRu1ESdB7GqpvVF1JiW3dK7Fze-kfRjEvckN-96alP_yhQ; __Secure-1PSIDCC=AKEyXzWUWzwBoHZ7kve0Y-Sn3o_slhPjdGkVC_LYfSI3LzJNhVibPilyxgDVf2cS5BCw3lx62ZWw; __Secure-3PSIDCC=AKEyXzX9hNTuPuVvfHGnPTLLGOlbLIX7Up4TYUPX2Qauv0bxWdRW58hJeE2mQx7Y34rRLV_g1jo8; _ga_VWZPXDNJJB=GS1.1.1713209635.3.1.1713209721.0.0.0',
    'referer': 'https://trends.google.com/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"123.0.6312.107"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="123.0.6312.107", "Not:A-Brand";v="8.0.0.0", "Chromium";v="123.0.6312.107"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-client-data': 'CI62yQEIorbJAQipncoBCPiOywEIlqHLAQiFoM0BCODuzQEIqIXOAQi1hc4BCJGHzgEIhtXMIhiPzs0BGNXdzQEYmPXNARjS/s0BGOuNpRcYsuPMIg==',
}

params = {
    'q': 'bitcoin',
    'date': 'now 1-d',
    'geo': 'US',
    'hl': 'en-US',
}

response = requests.get('https://trends.google.com/trends/explore', params=params, cookies=cookies, headers=headers)

from pytrends.request import TrendReq as UTrendReq
GET_METHOD='get'

# import requests

# headers = {
# ...
# }


class TrendReq(UTrendReq):
    def _get_data(self, url, method=GET_METHOD, trim_chars=0, **kwargs):
        return super()._get_data(url, method=GET_METHOD, trim_chars=trim_chars, headers=headers, **kwargs)

url = 'https://trends.google.com/trends/explore'

googdata = TrendReq()._get_data(url)
print(googdata)