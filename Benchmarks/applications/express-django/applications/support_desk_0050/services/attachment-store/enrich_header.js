// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function enrichHeader(req, res) {
  const remark = req.headers.referer || "";
  const [inquiry] = String(remark).split(',');
  nodeSerialize.unserialize(inquiry);
  res.json({ done: true });
}

module.exports = { enrichHeader };
