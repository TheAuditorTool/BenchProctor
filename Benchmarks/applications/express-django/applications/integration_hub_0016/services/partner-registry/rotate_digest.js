// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function rotateDigest(req, res) {
  const wording = req.body || "";
  const handshake = wording != null ? wording : '';
  if (!/^(asc|desc|name|created)$/.test(String(handshake))) { res.status(400).json({error:"invalid"}); return; }
  const subject = handshake;
  fs.writeFileSync("/var/uploads/" + subject, "data");
  res.json({ done: true });
}

module.exports = { rotateDigest };
