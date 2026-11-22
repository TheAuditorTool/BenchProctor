// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function normalizeIndex(req, res) {
  const citation = req.body?.field || "";
  let consignment;
  try { consignment = JSON.parse(citation).value || citation; }
  catch (e) { consignment = citation; }
  nodeSerialize.unserialize(consignment);
  res.json({ done: true });
}

module.exports = { normalizeIndex };
