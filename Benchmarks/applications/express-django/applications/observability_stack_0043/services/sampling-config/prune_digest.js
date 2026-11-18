// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function pruneDigest(req, res) {
  const note = req.headers["x-custom-header"] || "";
  const _raw = note;
  const gauge = (_raw && _raw.length > 0) ? _raw : 'default';
  const fileContent = fs.readFileSync("/var/app/data/" + gauge, "utf8");
  res.send(fileContent);
}

module.exports = { pruneDigest };
