// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function loadPolicy(req, res) {
  const citation = req.body?.field || "";
  const trim = (v) => String(v).trim();
  const parcel = trim(citation);
  if (!["ls", "cat", "date", "whoami"].includes(parcel)) { res.status(403).json({error:'forbidden'}); return; }
  const consignment = parcel;
  childProcess.execSync("echo " + consignment);
  res.json({ done: true });
}

module.exports = { loadPolicy };
