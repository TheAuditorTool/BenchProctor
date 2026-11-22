// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function publishCheckpoint(req, res) {
  const remark = req.body.field || "";
  let persona;
  try { persona = JSON.parse(remark).value || remark; }
  catch (e) { persona = remark; }
  nodeSerialize.unserialize(persona);
  res.json({ done: true });
}

module.exports = { publishCheckpoint };
