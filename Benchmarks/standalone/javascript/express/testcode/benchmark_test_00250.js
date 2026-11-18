// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00250(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  fs.unlinkSync("/var/app/data/" + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00250 };
