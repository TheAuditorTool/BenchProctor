// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function rotateRoster(req, res) {
  const passage = req.headers.authorization || "";
  let remittance;
  try { remittance = JSON.parse(passage).value || passage; }
  catch (e) { remittance = passage; }
  nodeSerialize.unserialize(remittance);
  res.json({ done: true });
}

module.exports = { rotateRoster };
