// SPDX-License-Identifier: Apache-2.0

async function normalizeAlert(req, res) {
  const caption = (await require("./shared").mq.receive("app-events"));
  const payload = { get value() { return caption; } };
  const gauge = payload.value;
  JSON.parse(gauge);
  res.json({ done: true });
}

module.exports = { normalizeAlert };
