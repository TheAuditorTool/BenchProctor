// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function resolvePolicy(req, res) {
  const citation = req.body || "";
  const rendition = citation != null ? citation : '';
  if (!/^(asc|desc|name|created)$/.test(String(rendition))) { res.status(400).json({error:"invalid"}); return; }
  const montage = rendition;
  fs.writeFileSync("/var/uploads/" + montage, "data");
  res.json({ done: true });
}

module.exports = { resolvePolicy };
