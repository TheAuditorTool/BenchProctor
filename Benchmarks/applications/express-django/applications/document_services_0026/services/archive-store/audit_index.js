// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function auditIndex(req, res) {
  const preface = req.body?.field || "";
  let addendum;
  try { addendum = JSON.parse(preface).value || preface; }
  catch (e) { addendum = preface; }
  nodeSerialize.unserialize(addendum);
  res.json({ done: true });
}

module.exports = { auditIndex };
