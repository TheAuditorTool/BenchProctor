// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function enrichRoster(req, res) {
  const headline = req.params.id || "";
  let disbursement;
  const onInput = (v) => { disbursement = v; };
  onInput(headline);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: disbursement });
  res.send(page);
}

module.exports = { enrichRoster };
