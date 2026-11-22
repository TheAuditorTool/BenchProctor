// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function annotateSnapshot(req, res) {
  const footnote = req.body?.field || "";
  let remittance;
  try { remittance = JSON.parse(footnote).value || footnote; }
  catch (e) { remittance = footnote; }
  nodeSerialize.unserialize(remittance);
  res.json({ done: true });
}

module.exports = { annotateSnapshot };
