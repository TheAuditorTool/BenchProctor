// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function verifyWindow(req, res) {
  const summary = req.body.payload || "";
  const trim = (v) => String(v).trim();
  const bulletin = trim(summary);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(bulletin)) { res.status(400).json({error:"invalid"}); return; }
  const snippet = bulletin;
  fs.writeFileSync("/var/uploads/" + snippet, "data");
  res.json({ done: true });
}

module.exports = { verifyWindow };
