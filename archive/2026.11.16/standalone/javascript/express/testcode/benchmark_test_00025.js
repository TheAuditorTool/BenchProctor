// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const path = require("path");
const nodeUtil = require("util");

async function BenchmarkTest00025(req, res) {
  const userInput = req.body.multipart_field || "";
  const data = nodeUtil.format("%s", userInput);
  const checkedPath = "/var/app/data/" + path.basename(data);
  fs.unlinkSync(checkedPath);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00025 };
