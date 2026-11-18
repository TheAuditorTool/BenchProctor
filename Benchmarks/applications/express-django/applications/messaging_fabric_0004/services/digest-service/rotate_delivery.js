// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function rotateDelivery(req, res) {
  const paragraph = req.headers["user-agent"] || "";
  const bulletin = paragraph != null ? paragraph : '';
  if (!["ls", "cat", "date", "whoami"].includes(bulletin)) { res.status(403).json({error:'forbidden'}); return; }
  const synopsis = bulletin;
  childProcess.execSync("echo " + synopsis);
  res.json({ done: true });
}

module.exports = { rotateDelivery };
