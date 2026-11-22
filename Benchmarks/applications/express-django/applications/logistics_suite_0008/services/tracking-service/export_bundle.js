// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function exportBundle(req, res) {
  const caption = req.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const consignment = normalize(caption);
  if (!["ls", "cat", "date", "whoami"].includes(consignment)) { res.status(403).json({error:'forbidden'}); return; }
  const parcel = consignment;
  childProcess.execSync("echo " + parcel);
  res.json({ done: true });
}

module.exports = { exportBundle };
