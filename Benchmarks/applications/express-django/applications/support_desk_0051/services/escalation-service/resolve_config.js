// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function resolveConfig(req, res) {
  const preface = req.headers.referer || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const grievance = normalize(preface);
  childProcess.exec("echo " + grievance, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { resolveConfig };
