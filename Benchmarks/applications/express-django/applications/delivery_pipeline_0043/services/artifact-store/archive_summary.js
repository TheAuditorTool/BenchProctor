// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function archiveSummary(req, res) {
  const remark = process.env.DELIVERY_INPUT_0043 || "";
  const payload = { get value() { return remark; } };
  const note = payload.value;
  const resolved = path.resolve("/var/app/data", note);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const phrase = resolved;
  fs.unlinkSync(phrase);
  res.json({ done: true });
}

module.exports = { archiveSummary };
