// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function BenchmarkTest00619(req, res) {
  const userInput = req.headers.referer || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  const resolved = path.resolve("/var/app/data", data);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const checkedPath = resolved;
  const fileContent = fs.readFileSync(checkedPath, "utf8");
  res.send(fileContent);
}

module.exports = { BenchmarkTest00619 };
