// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function publishLedger(req, res) {
  const excerpt = req.headers.authorization || "";
  let dossier;
  try { dossier = JSON.parse(excerpt).value || excerpt; }
  catch (e) { dossier = excerpt; }
  nodeSerialize.unserialize(dossier);
  res.json({ done: true });
}

module.exports = { publishLedger };
