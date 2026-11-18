// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function summarizeProfile(req, res) {
  const note = req.body.payload || "";
  const trim = (v) => String(v).trim();
  const handshake = trim(note);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const persona = handshake;
  fs.writeFileSync("/var/uploads/" + persona, "data");
  res.json({ done: true });
}

module.exports = { summarizeProfile };
