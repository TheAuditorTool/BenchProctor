// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function reconcileThreshold(req, res) {
  const snippet = req.body || "";
  const _raw = snippet;
  const persona = (_raw && _raw.length > 0) ? _raw : 'default';
  const resolved = path.resolve("/var/app/data", persona);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const handshake = resolved;
  fs.unlinkSync(handshake);
  res.json({ done: true });
}

module.exports = { reconcileThreshold };
