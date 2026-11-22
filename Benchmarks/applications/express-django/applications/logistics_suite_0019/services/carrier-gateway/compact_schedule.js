// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function compactSchedule(req, res) {
  const citation = req.headers.authorization || "";
  const [parcel] = String(citation).split(',');
  childProcess.execSync("echo " + parcel);
  res.json({ done: true });
}

module.exports = { compactSchedule };
