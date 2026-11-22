// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const path = require("path");

async function BenchmarkTest00291(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const checkedPath = "/var/app/data/" + path.basename(data);
  fs.unlinkSync(checkedPath);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00291 };
