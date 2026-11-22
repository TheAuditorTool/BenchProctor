// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function annotateReport(req, res) {
  const remark = req.body.field || "";
  let gauge;
  try { gauge = JSON.parse(remark).value || remark; }
  catch (e) { gauge = remark; }
  nodeSerialize.unserialize(gauge);
  res.json({ done: true });
}

module.exports = { annotateReport };
