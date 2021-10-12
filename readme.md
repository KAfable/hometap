# HomeTap Take Home

## Getting Started

It is recommended you run this project in a Python virtual environment. After cloning, install the packages with `pip install -r requirements.txt` and then `flask run` to run the app. You can also run it in development mode with `python app.py`, which will use the mock environment variables found in `.flaskenv`.

The api keys for each individual 3rd party service (HouseCanary, etc.) are labelled appriopriately in `.env`. The base URL's of each specific 3rd party service you want to access are appropriately labeled under `.flaskenv`.

## Notes
- GOAL: prompt homeowners with an additional question if home has a septic system.
- we want to leave the web app implementation alone:
  - assuming they want to leave FE engineers alone
  - make the aggregator at the backend, instead of the web app talking to multiple 3rd party API's
  - make that information available through a custom API endpoint you design for our web app to use.
 
## Alternatives Considered
- building this a GraphQL aggregate data layer if this was going to be pulling from many individual data sources
- returning only a boolean, instead of a True/False/None
  - there might a scenario where the API user might want to know if we couldn't verify if our response is accurate

## To Do List
- implement authentication and authorization at Flask level
  - check out flask convention/native flask modules (if any) for security
- setup Docker so the API is built inside a container for scalabiliy
  - basic MAKEFILE command for `docker-compose` shorthand
- actual factual HTTP request to HouseCanary if given credentials
- unit testing in whatever native testing module Flask has (if there is one)

## Reflections
- caught off guard by global context variables such as `request`, feels weird to import something to the global scope without declaring it, or passing it in
  - I assume it is just similar to how the browser provides the `window` object auto-magically to most frontend apps
- Flask was straight forward, but mocking a proxy and it's response in unit testing less so
- Unsure of nature authentication/authorization
  - unlikely that this app would store it's own variation of users/uer info
  - would use existing organiation's authentication/authorization
  - need to include scenarios where the 3rd party API's might require an api key per user in the organization