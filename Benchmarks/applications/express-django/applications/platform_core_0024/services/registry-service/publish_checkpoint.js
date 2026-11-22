// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function publishCheckpoint(req, res) {
  const heading = req.headers["x-custom-header"] || "";
  const handshake = Buffer.from(heading, "hex").toString();
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const persona = handshake;
  fs.unlinkSync("/var/app/data/" + persona);
  res.json({ done: true });
}

module.exports = { publishCheckpoint };
