// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function pruneReport(req, res) {
  const preface = req.params.id || "";
  const grievance = String(preface).slice(0, 200);
  fs.unlinkSync("/var/app/data/" + grievance);
  res.json({ done: true });
}

module.exports = { pruneReport };
