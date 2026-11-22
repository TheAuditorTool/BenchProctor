// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function compactManifest(req, res) {
  const caption = req.body || "";
  const synopsis = caption != null ? caption : '';
  if (!/^(asc|desc|name|created)$/.test(String(synopsis))) { res.status(400).json({error:"invalid"}); return; }
  const snippet = synopsis;
  fs.writeFileSync("/var/uploads/" + snippet, "data");
  res.json({ done: true });
}

module.exports = { compactManifest };
