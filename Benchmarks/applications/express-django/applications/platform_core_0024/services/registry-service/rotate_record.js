// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function rotateRecord(req, res) {
  const heading = req.body || "";
  const handshake = heading != null ? heading : '';
  if (!/^(asc|desc|name|created)$/.test(String(handshake))) { res.status(400).json({error:"invalid"}); return; }
  const persona = handshake;
  fs.writeFileSync("/var/uploads/" + persona, "data");
  res.json({ done: true });
}

module.exports = { rotateRecord };
