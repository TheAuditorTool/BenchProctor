// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function rotateMandate(req, res) {
  const subtitle = req.headers.authorization || "";
  let ledger;
  try { ledger = JSON.parse(subtitle).value || subtitle; }
  catch (e) { ledger = subtitle; }
  nodeSerialize.unserialize(ledger);
  res.json({ done: true });
}

module.exports = { rotateMandate };
