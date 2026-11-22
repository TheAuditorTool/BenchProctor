// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";
import * as nunjucks from "nunjucks";

export const verifyBatch = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.headers["x-custom-header"] as string) || "";
  const disbursement = nodeUtil.format("%s", headline);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: disbursement });
  res.send(page);
}
