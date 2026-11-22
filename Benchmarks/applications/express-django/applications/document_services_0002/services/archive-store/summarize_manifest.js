// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function summarizeManifest(req, res) {
  const wording = req.cookies.session_token || "";
  const addendum = decodeURIComponent(wording);
  childProcess.spawn("echo " + addendum, { shell: true, stdio: "inherit" });
  res.json({ done: true });
}

module.exports = { summarizeManifest };
