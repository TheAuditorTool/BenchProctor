// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function archiveRoster(req, res) {
  const citation = req.body.payload || "";
  const trim = (v) => String(v).trim();
  const parcel = trim(citation);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(parcel)) { res.status(400).json({error:"invalid"}); return; }
  const consignment = parcel;
  fs.writeFileSync("/var/uploads/" + consignment, "data");
  res.json({ done: true });
}

module.exports = { archiveRoster };
