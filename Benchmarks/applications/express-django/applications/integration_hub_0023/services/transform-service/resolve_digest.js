// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function resolveDigest(req, res) {
  const caption = req.body || "";
  const handshake = caption != null ? caption : '';
  if (!/^(asc|desc|name|created)$/.test(String(handshake))) { res.status(400).json({error:"invalid"}); return; }
  const subject = handshake;
  fs.writeFileSync("/var/uploads/" + subject, "data");
  res.json({ done: true });
}

module.exports = { resolveDigest };
