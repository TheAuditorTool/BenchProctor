// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00277(req, res) {
  const userInput = req.body.multipart_field || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  fs.writeFileSync("/var/uploads/" + data, "data");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00277 };
