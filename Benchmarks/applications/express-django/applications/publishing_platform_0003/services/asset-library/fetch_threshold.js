// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function fetchThreshold(req, res) {
  const heading = req.body?.field || "";
  const trim = (v) => String(v).trim();
  const addendum = trim(heading);
  if (!["ls", "cat", "date", "whoami"].includes(addendum)) { res.status(403).json({error:'forbidden'}); return; }
  const byline = addendum;
  childProcess.execSync("echo " + byline);
  res.json({ done: true });
}

module.exports = { fetchThreshold };
