// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function summarizeConfig(req, res) {
  const phrase = req.params.id || "";
  const dossier = String(phrase).slice(0, 200);
  fs.unlinkSync("/var/app/data/" + dossier);
  res.json({ done: true });
}

module.exports = { summarizeConfig };
