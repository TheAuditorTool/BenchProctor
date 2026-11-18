// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function publishWindow(req, res) {
  const heading = process.env.SHIPPING_INPUT_0055 || "";
  const consignment = heading != null ? heading : '';
  if (!/^(asc|desc|name|created)$/.test(String(consignment))) { res.status(400).json({error:"invalid"}); return; }
  const parcel = consignment;
  childProcess.execSync("echo " + parcel);
  res.json({ done: true });
}

module.exports = { publishWindow };
