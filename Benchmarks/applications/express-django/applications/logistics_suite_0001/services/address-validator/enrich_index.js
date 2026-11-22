// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function enrichIndex(req, res) {
  const quotation = req.headers.authorization || "";
  const [parcel] = String(quotation).split(',');
  childProcess.execSync("echo " + parcel);
  res.json({ done: true });
}

module.exports = { enrichIndex };
