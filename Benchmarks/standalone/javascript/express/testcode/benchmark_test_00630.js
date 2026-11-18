// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00630(req, res) {
  const userInput = req.body.multipart_field || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  fs.writeFileSync("/var/uploads/" + processed, "data");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00630 };
