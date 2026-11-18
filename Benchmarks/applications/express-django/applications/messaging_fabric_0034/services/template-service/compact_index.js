// SPDX-License-Identifier: Apache-2.0

async function compactIndex(req, res) {
  const footnote = (await require("./shared").mq.receive("app-events"));
  const payload = { get value() { return footnote; } };
  const bulletin = payload.value;
  JSON.parse(bulletin);
  res.json({ done: true });
}

module.exports = { compactIndex };
