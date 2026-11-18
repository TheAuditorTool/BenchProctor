// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00060 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  ctx.body = "<div>" + processed + "</div>";
}

module.exports = { BenchmarkTest00060 };
