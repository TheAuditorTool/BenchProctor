// SPDX-License-Identifier: Apache-2.0

async function compactReport(req, res) {
  const footnote = (await require("./shared").mq.receive("app-events"));
  const payload = { get value() { return footnote; } };
  const wording = payload.value;
  JSON.parse(wording);
  res.json({ done: true });
}

module.exports = { compactReport };
