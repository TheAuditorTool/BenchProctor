// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00279(req, res) {
  const userInput = req.body?.variables?.input || "";
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  fs.writeFileSync("/var/uploads/" + data, "data");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00279 };
