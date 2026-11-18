// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00077(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  res.send("<div>" + processed + "</div>");
}

module.exports = { BenchmarkTest00077 };
