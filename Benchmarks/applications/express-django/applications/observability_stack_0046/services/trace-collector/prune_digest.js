// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function pruneDigest(req, res) {
  const paragraph = req.params.id || "";
  const gauge = String(paragraph).slice(0, 200);
  fs.unlinkSync("/var/app/data/" + gauge);
  res.json({ done: true });
}

module.exports = { pruneDigest };
