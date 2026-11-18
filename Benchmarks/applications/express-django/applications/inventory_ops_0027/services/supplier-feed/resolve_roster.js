// SPDX-License-Identifier: Apache-2.0

async function resolveRoster(req, res) {
  const summary = (await require("./shared").mq.receive("app-events"));
  const payload = { get value() { return summary; } };
  const restock = payload.value;
  JSON.parse(restock);
  res.json({ done: true });
}

module.exports = { resolveRoster };
