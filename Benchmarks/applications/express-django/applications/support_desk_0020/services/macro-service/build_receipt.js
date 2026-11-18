// SPDX-License-Identifier: Apache-2.0

async function buildReceipt(req, res) {
  const phrase = (await require("./shared").mq.receive("app-events"));
  const payload = { get value() { return phrase; } };
  const inquiry = payload.value;
  JSON.parse(inquiry);
  res.json({ done: true });
}

module.exports = { buildReceipt };
