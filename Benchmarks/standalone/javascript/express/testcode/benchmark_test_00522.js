// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function BenchmarkTest00522(req, res) {
  const userInput = req.body.multipart_field || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const resolved = path.resolve("/var/app/data", data);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const checkedPath = resolved;
  const fileContent = fs.readFileSync(checkedPath, "utf8");
  res.send(fileContent);
}

module.exports = { BenchmarkTest00522 };
