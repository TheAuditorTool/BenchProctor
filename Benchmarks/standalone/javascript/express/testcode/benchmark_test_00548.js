// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const path = require("path");

async function BenchmarkTest00548(req, res) {
  const userInput = req.body.multipart_field || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const checkedPath = "/var/app/data/" + path.basename(data);
  fs.writeFileSync(checkedPath, "data");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00548 };
