// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const path = require("path");

async function BenchmarkTest00420(req, res) {
  const userInput = req.body || "";
  const data = Buffer.from(userInput, "base64").toString();
  const checkedPath = "/var/app/data/" + path.basename(data);
  fs.unlinkSync(checkedPath);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00420 };
