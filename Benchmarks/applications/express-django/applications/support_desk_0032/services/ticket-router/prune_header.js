// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function pruneHeader(req, res) {
  const note = req.headers.referer || "";
  const [inquiry] = String(note).split(',');
  nodeSerialize.unserialize(inquiry);
  res.json({ done: true });
}

module.exports = { pruneHeader };
