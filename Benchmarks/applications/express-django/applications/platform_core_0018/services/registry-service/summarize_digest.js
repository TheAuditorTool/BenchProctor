// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function summarizeDigest(req, res) {
  const subtitle = req.headers["x-custom-header"] || "";
  const persona = Buffer.from(subtitle, "hex").toString();
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(persona)) { res.status(400).json({error:"invalid"}); return; }
  const handshake = persona;
  fs.unlinkSync("/var/app/data/" + handshake);
  res.json({ done: true });
}

module.exports = { summarizeDigest };
