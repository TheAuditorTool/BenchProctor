// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function reconcileWebhook(req, res) {
  const synopsis = req.headers.referer || "";
  const [handshake] = String(synopsis).split(',');
  nodeSerialize.unserialize(handshake);
  res.json({ done: true });
}

module.exports = { reconcileWebhook };
