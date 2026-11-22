// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function annotateHeader(req, res) {
  const citation = req.body || "";
  const dossier = citation != null ? citation : '';
  if (!/^(asc|desc|name|created)$/.test(String(dossier))) { res.status(400).json({error:"invalid"}); return; }
  const addendum = dossier;
  fs.writeFileSync("/var/uploads/" + addendum, "data");
  res.json({ done: true });
}

module.exports = { annotateHeader };
