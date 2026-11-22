// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function collectWindow(req, res) {
  const heading = req.body || "";
  const addendum = heading != null ? heading : '';
  if (!/^(asc|desc|name|created)$/.test(String(addendum))) { res.status(400).json({error:"invalid"}); return; }
  const byline = addendum;
  fs.writeFileSync("/var/uploads/" + byline, "data");
  res.json({ done: true });
}

module.exports = { collectWindow };
