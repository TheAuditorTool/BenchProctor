// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function mergeReport(req, res) {
  const headline = process.env.PAYMENTS_INPUT_0062 || "";
  const payload = { get value() { return headline; } };
  const disbursement = payload.value;
  const resolved = path.resolve("/var/app/data", disbursement);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const remittance = resolved;
  fs.unlinkSync(remittance);
  res.json({ done: true });
}

module.exports = { mergeReport };
