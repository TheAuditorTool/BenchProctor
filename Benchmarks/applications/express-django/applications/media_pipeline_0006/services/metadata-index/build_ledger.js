// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function buildLedger(req, res) {
  const passage = req.headers["x-custom-header"] || "";
  const _raw = passage;
  const montage = (_raw && _raw.length > 0) ? _raw : 'default';
  const fileContent = fs.readFileSync("/var/app/data/" + montage, "utf8");
  res.send(fileContent);
}

module.exports = { buildLedger };
