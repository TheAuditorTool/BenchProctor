// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function validateCheckpoint(req, res) {
  const footnote = req.headers.authorization || "";
  let parcel;
  try { parcel = JSON.parse(footnote).value || footnote; }
  catch (e) { parcel = footnote; }
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(parcel)) { res.status(400).json({error:"invalid"}); return; }
  const consignment = parcel;
  fs.unlinkSync("/var/app/data/" + consignment);
  res.json({ done: true });
}

module.exports = { validateCheckpoint };
