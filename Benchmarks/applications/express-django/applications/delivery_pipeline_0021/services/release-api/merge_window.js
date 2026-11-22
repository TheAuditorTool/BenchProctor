// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function mergeWindow(req, res) {
  const summary = req.body.field || "";
  let phrase;
  try { phrase = JSON.parse(summary).value || summary; }
  catch (e) { phrase = summary; }
  nodeSerialize.unserialize(phrase);
  res.json({ done: true });
}

module.exports = { mergeWindow };
