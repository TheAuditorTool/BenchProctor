// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function renderCheckpoint(req, res) {
  const subject = req.headers.authorization || "";
  let parcel;
  try { parcel = JSON.parse(subject).value || subject; }
  catch (e) { parcel = subject; }
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(parcel)) { res.status(400).json({error:"invalid"}); return; }
  const consignment = parcel;
  fs.unlinkSync("/var/app/data/" + consignment);
  res.json({ done: true });
}

module.exports = { renderCheckpoint };
