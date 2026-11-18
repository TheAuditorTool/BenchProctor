// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00147(req, res) {
  const userInput = req.body || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  fs.writeFileSync("/var/uploads/" + data, "data");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00147 };
