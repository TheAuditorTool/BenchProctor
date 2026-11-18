// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function validateWorkspace(req, res) {
  const remark = req.body.payload || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const synopsis = normalize(remark);
  childProcess.execFileSync("echo", [synopsis]);
  res.json({ done: true });
}

module.exports = { validateWorkspace };
