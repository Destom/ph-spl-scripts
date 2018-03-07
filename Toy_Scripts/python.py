import robobrowser

br = robobrowser.RoboBrowser()

br.open("https://accounts.google.com/signin/v2/identifier?service=accountsettings&passive=1209600&osid=1&continue=https%3A%2F%2Fmyaccount.google.com%2Fintro%3Futm_source%3DOGB%26utm_medium%3Dapp&followup=https%3A%2F%2Fmyaccount.google.com%2Fintro%3Futm_source%3DOGB%26utm_medium%3Dapp&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
form = br.get_form()
