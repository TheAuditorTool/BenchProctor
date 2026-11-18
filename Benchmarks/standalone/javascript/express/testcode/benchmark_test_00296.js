// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00296(req, res) {
  const userInput = req.headers.referer || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  fs.unlinkSync("/var/app/data/" + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00296 };
