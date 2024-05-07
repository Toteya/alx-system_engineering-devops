#!/usr/bin/node

const fecth = require("node-fetch");
const url = "https://www.reddit.com/api/v1/access_token";
const authData = {
  grant_type: "password",
  username: "g9dDZPYiFqmFKdt19cVmJA",
  password: "CguisP8TQpfMkmURwpeK7LBpKnxreg",
};
var form = new FormData()
form.append('code', code);
form.append('grant_type', "authorization_code");
form.append('redirect_uri');

var request = fetch(url, {
    method: "POST",
    headers: {
      Accept: "application/json",
      'Content-Type': "application/json;charset=UTF-8",
      'User-Agent': "myApp:V0.1 by Toteya"
    },
    body: form,
}).then((response) => {
  console.log(response)
});
