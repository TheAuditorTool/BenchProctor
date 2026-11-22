// SPDX-License-Identifier: Apache-2.0
const ldapjs = require("ldapjs");

const BenchmarkTest00148 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  const password = String((ctx.request.body && ctx.request.body.password) || "");
  if (!password) { ctx.status = 400; ctx.body = { error: "password required" }; return; }
  const authenticated = await new Promise((resolve) => {
    ldapClient.bind("uid=" + processed + ",ou=people,dc=example,dc=com", password, (err) => { ldapClient.unbind(); resolve(!err); });
  });
  ctx.body = { authenticated }; return;
}

module.exports = { BenchmarkTest00148 };
