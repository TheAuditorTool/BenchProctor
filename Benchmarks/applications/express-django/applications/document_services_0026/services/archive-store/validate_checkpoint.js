// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function validateCheckpoint(req, res) {
  const preface = process.env.DOCUMENTS_INPUT_0026 || "";
  const payload = { get value() { return preface; } };
  const addendum = payload.value;
  const resolved = path.resolve("/var/app/data", addendum);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const dossier = resolved;
  fs.unlinkSync(dossier);
  res.json({ done: true });
}

module.exports = { validateCheckpoint };
