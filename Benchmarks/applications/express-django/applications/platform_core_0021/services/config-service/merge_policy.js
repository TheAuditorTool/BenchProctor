// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function mergePolicy(req, res) {
  const excerpt = req.body || "";
  const _raw = excerpt;
  const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
  const resolved = path.resolve("/var/app/data", handshake);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const persona = resolved;
  fs.unlinkSync(persona);
  res.json({ done: true });
}

module.exports = { mergePolicy };
