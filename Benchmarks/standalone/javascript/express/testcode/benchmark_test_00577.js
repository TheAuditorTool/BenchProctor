// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00577(req, res) {
  const userInput = req.headers.host || "";
  const data = `${userInput}`;
  fs.writeFileSync("/var/uploads/" + data, "data");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00577 };
