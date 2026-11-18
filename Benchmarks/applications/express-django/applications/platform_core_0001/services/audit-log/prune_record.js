// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function pruneRecord(req, res) {
  const tagline = req.body.payload || "";
  const trim = (v) => String(v).trim();
  const persona = trim(tagline);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(persona)) { res.status(400).json({error:"invalid"}); return; }
  const handshake = persona;
  fs.writeFileSync("/var/uploads/" + handshake, "data");
  res.json({ done: true });
}

module.exports = { pruneRecord };
