// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00099(req, res) {
  const userInput = req.headers.referer || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  fs.writeFileSync("/var/uploads/" + data, "data");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00099 };
