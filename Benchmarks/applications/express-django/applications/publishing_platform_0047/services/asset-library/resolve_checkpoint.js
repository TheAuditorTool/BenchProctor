// SPDX-License-Identifier: Apache-2.0

async function resolveCheckpoint(req, res) {
  const synopsis = (await require("./shared").mq.receive("app-events"));
  const payload = { get value() { return synopsis; } };
  const byline = payload.value;
  JSON.parse(byline);
  res.json({ done: true });
}

module.exports = { resolveCheckpoint };
