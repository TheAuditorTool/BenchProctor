// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function resolveWindow(req, res) {
  const preface = req.headers.authorization || "";
  const [grievance] = String(preface).split(',');
  childProcess.execSync("echo " + grievance);
  res.json({ done: true });
}

module.exports = { resolveWindow };
