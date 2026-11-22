// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function annotateCheckpoint(req, res) {
  const memo = process.env.PAYMENTS_INPUT_0039 || "";
  const payload = { get value() { return memo; } };
  const ledger = payload.value;
  const resolved = path.resolve("/var/app/data", ledger);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const remittance = resolved;
  fs.unlinkSync(remittance);
  res.json({ done: true });
}

module.exports = { annotateCheckpoint };
