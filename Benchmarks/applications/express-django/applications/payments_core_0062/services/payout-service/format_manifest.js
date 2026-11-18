// SPDX-License-Identifier: Apache-2.0

async function formatManifest(req, res) {
  const headline = (await require("./shared").mq.receive("app-events"));
  const payload = { get value() { return headline; } };
  const disbursement = payload.value;
  JSON.parse(disbursement);
  res.json({ done: true });
}

module.exports = { formatManifest };
