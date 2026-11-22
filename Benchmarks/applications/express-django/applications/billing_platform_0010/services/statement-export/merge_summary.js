// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function mergeSummary(req, res) {
  const headline = process.env.BILLING_INPUT_0010 || "";
  const payload = { get value() { return headline; } };
  const remittance = payload.value;
  const resolved = path.resolve("/var/app/data", remittance);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const dunning = resolved;
  fs.unlinkSync(dunning);
  res.json({ done: true });
}

module.exports = { mergeSummary };
