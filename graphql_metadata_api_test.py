import jsbeautifier
import requests
import tableauserverclient as TSC

# Set the Tableau Server URL and Credentials we will use to login into Tableau 
ts_server_ip = '<tableau_server_ip>'
ts_server_url = TSC.Server('http://' + ts_server_ip)
metadata_url = 'http://' + ts_server_ip + '/relationship-service-war/graphql'
tableau_auth = TSC.TableauAuth('<tableau_user>','<tableau_password>')

# Now login to the Tableau Server
with ts_server_url.auth.sign_in(tableau_auth):

    # Define the simple query we will execute
    json = { 'query' : '{tableauSites(filter: {name: "Default"}) {id, name, workbooks (filter: {name: "Forecasting"}){id, name, sheets{name}}}}' }
    
    # Set the headers to have the token we got when we logged in
    headers = {'X-Tableau-Auth': ts_server_url._auth_token}
    
    # Execute the query passing in the token
    r = requests.post(url=metadata_url, json=json, headers=headers)
    
    # Print the pretty json response to the console
    print(jsbeautifier.beautify(r.text))
    