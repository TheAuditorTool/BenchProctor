// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00147(req, res) {
  const userInput = req.query.id || "";
  const data = decodeURIComponent(userInput);
  fs.writeFileSync("/var/uploads/" + data, "data");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00147 };
