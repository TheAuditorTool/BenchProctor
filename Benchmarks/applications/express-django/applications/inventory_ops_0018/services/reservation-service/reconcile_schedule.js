// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function reconcileSchedule(req, res) {
  const transcript = req.body || "";
  const _raw = transcript;
  const backorder = (_raw && _raw.length > 0) ? _raw : 'default';
  const resolved = path.resolve("/var/app/data", backorder);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const restock = resolved;
  fs.unlinkSync(restock);
  res.json({ done: true });
}

module.exports = { reconcileSchedule };
