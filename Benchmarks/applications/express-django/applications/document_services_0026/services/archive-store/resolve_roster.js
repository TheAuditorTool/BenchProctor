// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function resolveRoster(req, res) {
  const preface = req.headers["x-custom-header"] || "";
  const addendum = Buffer.from(preface, "hex").toString();
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(addendum)) { res.status(400).json({error:"invalid"}); return; }
  const dossier = addendum;
  fs.unlinkSync("/var/app/data/" + dossier);
  res.json({ done: true });
}

module.exports = { resolveRoster };
