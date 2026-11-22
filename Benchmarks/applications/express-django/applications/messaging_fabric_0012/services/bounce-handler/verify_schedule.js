// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function verifySchedule(req, res) {
  const preface = req.params.id || "";
  let bulletin;
  const onInput = (v) => { bulletin = v; };
  onInput(preface);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: bulletin });
  res.send(page);
}

module.exports = { verifySchedule };
