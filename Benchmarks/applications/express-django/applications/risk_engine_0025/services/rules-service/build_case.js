// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function buildCase(req, res) {
  const excerpt = process.env.RISK_INPUT_0025 || "";
  const payload = { get value() { return excerpt; } };
  const verdict = payload.value;
  const resolved = path.resolve("/var/app/data", verdict);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const grievance = resolved;
  fs.unlinkSync(grievance);
  res.json({ done: true });
}

module.exports = { buildCase };
