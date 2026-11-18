// SPDX-License-Identifier: Apache-2.0

async function pruneSnapshot(req, res) {
  const transcript = (await require("./shared").mq.receive("app-events"));
  const payload = { get value() { return transcript; } };
  const rendition = payload.value;
  JSON.parse(rendition);
  res.json({ done: true });
}

module.exports = { pruneSnapshot };
