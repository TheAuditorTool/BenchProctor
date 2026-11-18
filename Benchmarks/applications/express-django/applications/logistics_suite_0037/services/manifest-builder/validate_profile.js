// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function validateProfile(req, res) {
  const footnote = req.body.payload || "";
  const trim = (v) => String(v).trim();
  const consignment = trim(footnote);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(consignment)) { res.status(400).json({error:"invalid"}); return; }
  const parcel = consignment;
  fs.writeFileSync("/var/uploads/" + parcel, "data");
  res.json({ done: true });
}

module.exports = { validateProfile };
