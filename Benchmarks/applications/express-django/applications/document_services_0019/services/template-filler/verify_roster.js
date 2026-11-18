// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function verifyRoster(req, res) {
  const passage = req.headers["x-custom-header"] || "";
  const _raw = passage;
  const dossier = (_raw && _raw.length > 0) ? _raw : 'default';
  const fileContent = fs.readFileSync("/var/app/data/" + dossier, "utf8");
  res.send(fileContent);
}

module.exports = { verifyRoster };
