// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function compactCheckpoint(req, res) {
  const citation = process.env.INTEGRATIONS_INPUT_0048 || "";
  const payload = { get value() { return citation; } };
  const handshake = payload.value;
  const resolved = path.resolve("/var/app/data", handshake);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const heading = resolved;
  fs.unlinkSync(heading);
  res.json({ done: true });
}

module.exports = { compactCheckpoint };
