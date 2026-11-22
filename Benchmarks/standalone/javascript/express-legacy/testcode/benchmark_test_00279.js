// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00279(req, res) {
  const userInput = req.headers.host || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  fs.writeFileSync("/var/uploads/" + data, "data");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00279 };
