// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00715(req, res) {
  const userInput = req.headers.host || "";
  const data = userInput != null ? userInput : '';
  fs.unlinkSync("/var/app/data/" + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00715 };
