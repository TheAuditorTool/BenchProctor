// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function annotateIndex(req, res) {
  const phrase = req.params.id || "";
  const trim = (v) => String(v).trim();
  const persona = trim(phrase);
  childProcess.execSync("echo " + persona);
  res.json({ done: true });
}

module.exports = { annotateIndex };
