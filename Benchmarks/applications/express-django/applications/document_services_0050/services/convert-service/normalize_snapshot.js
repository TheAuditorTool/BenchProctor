// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function normalizeSnapshot(req, res) {
  const citation = req.headers.authorization || "";
  const [dossier] = String(citation).split(',');
  childProcess.execSync("echo " + dossier);
  res.json({ done: true });
}

module.exports = { normalizeSnapshot };
