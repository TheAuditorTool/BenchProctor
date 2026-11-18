// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function pruneManifest(req, res) {
  const caption = req.headers["user-agent"] || "";
  const parcel = caption != null ? caption : '';
  if (!["ls", "cat", "date", "whoami"].includes(parcel)) { res.status(403).json({error:'forbidden'}); return; }
  const consignment = parcel;
  childProcess.execSync("echo " + consignment);
  res.json({ done: true });
}

module.exports = { pruneManifest };
