// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function mergeReceipt(req, res) {
  const synopsis = req.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const rendition = normalize(synopsis);
  if (!["ls", "cat", "date", "whoami"].includes(rendition)) { res.status(403).json({error:'forbidden'}); return; }
  const montage = rendition;
  childProcess.execSync("echo " + montage);
  res.json({ done: true });
}

module.exports = { mergeReceipt };
