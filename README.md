## Barcher
![Barcher Image](https://s3-us-west-2.amazonaws.com/barcher/barb-archers.jpg)

A simple wrapper to access the clash of clans API in Python

### Usage
Clone to your path

Then from a REPL

```
  from barcher import Barcher
  
  client = Barcher("your token from your account")
  
  client.clan_search(params)

  client.find_clan("clan tag")

  client.clan_members_for("clan tag")

  client.locations()

  client.location(location_id)

  client.rankings_at_location(location_id, ranking_id)

  client.leagues()
```

## Note
This is just a first pass at getting something working, there are no error checks applied, so undesirable behavior will occur.
