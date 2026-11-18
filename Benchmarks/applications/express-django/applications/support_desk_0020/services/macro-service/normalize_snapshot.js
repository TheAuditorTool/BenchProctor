// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function normalizeSnapshot(req, res) {
  const phrase = req.body.payload || "";
  const trim = (v) => String(v).trim();
  const inquiry = trim(phrase);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(inquiry)) { res.status(400).json({error:"invalid"}); return; }
  const grievance = inquiry;
  fs.writeFileSync("/var/uploads/" + grievance, "data");
  res.json({ done: true });
}

module.exports = { normalizeSnapshot };
