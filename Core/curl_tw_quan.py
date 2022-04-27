import requests
from requests.structures import CaseInsensitiveDict

class curl_tw_quan(object):
    """Curl Twitter
    """
    ## api twv2
    def tw_api(self, user_id, acess_token):
        url = "https://api.twitter.com/2/users/" + user_id + "/following?max_results=1000"

        headers = CaseInsensitiveDict()
        headers[
            "Authorization"] = acess_token

        resp = requests.get(url, headers=headers)
        print(resp.status_code)
        resp.close()

        return resp.content, resp.status_code

    def tw_api_pagination(self, user_id, acess_token, pag_token):
        url = "https://api.twitter.com/2/users/" + user_id + "/following?max_results=1000" +"&pagination_token=" + pag_token

        headers = CaseInsensitiveDict()
        headers[
            "Authorization"] = acess_token

        resp = requests.get(url, headers=headers)
        print(resp.status_code)
        resp.close()

        return resp.content, resp.status_code
