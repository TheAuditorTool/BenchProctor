// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00710(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  fs.writeFileSync("/var/uploads/" + data, "data");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00710 };
