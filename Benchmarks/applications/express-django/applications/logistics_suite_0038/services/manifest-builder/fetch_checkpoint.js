// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function fetchCheckpoint(req, res) {
  const wording = req.headers.authorization || "";
  const [consignment] = String(wording).split(',');
  childProcess.execSync("echo " + consignment);
  res.json({ done: true });
}

module.exports = { fetchCheckpoint };
