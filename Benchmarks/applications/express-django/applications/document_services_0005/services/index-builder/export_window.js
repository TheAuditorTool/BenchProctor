// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function exportWindow(req, res) {
  const footnote = process.env.DOCUMENTS_INPUT_0005 || "";
  const payload = { get value() { return footnote; } };
  const addendum = payload.value;
  const resolved = path.resolve("/var/app/data", addendum);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const dossier = resolved;
  fs.unlinkSync(dossier);
  res.json({ done: true });
}

module.exports = { exportWindow };
