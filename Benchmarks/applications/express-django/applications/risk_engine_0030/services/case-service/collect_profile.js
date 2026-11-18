// SPDX-License-Identifier: Apache-2.0

async function collectProfile(req, res) {
  const summary = (await require("./shared").mq.receive("app-events"));
  const payload = { get value() { return summary; } };
  const grievance = payload.value;
  JSON.parse(grievance);
  res.json({ done: true });
}

module.exports = { collectProfile };
