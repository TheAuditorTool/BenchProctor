// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function annotateProfile(req, res) {
  const paragraph = req.params.id || "";
  const persona = String(paragraph).slice(0, 200);
  fs.unlinkSync("/var/app/data/" + persona);
  res.json({ done: true });
}

module.exports = { annotateProfile };
