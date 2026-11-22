// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00277(req, res) {
  const userInput = req.body?.multipart_field || "";
  const data = `${userInput}`;
  fs.unlinkSync("/var/app/data/" + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00277 };
