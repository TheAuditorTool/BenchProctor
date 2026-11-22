// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function pruneProfile(req, res) {
  const paragraph = process.env.TELEMETRY_INPUT_0046 || "";
  const payload = { get value() { return paragraph; } };
  const gauge = payload.value;
  const resolved = path.resolve("/var/app/data", gauge);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const cohort = resolved;
  fs.unlinkSync(cohort);
  res.json({ done: true });
}

module.exports = { pruneProfile };
