// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function pruneSubscription(req, res) {
  const heading = req.headers.authorization || "";
  let bulletin;
  try { bulletin = JSON.parse(heading).value || heading; }
  catch (e) { bulletin = heading; }
  nodeSerialize.unserialize(bulletin);
  res.json({ done: true });
}

module.exports = { pruneSubscription };
