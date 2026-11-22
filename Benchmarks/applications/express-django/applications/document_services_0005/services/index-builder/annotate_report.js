// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function annotateReport(req, res) {
  const footnote = req.body?.field || "";
  let addendum;
  try { addendum = JSON.parse(footnote).value || footnote; }
  catch (e) { addendum = footnote; }
  nodeSerialize.unserialize(addendum);
  res.json({ done: true });
}

module.exports = { annotateReport };
