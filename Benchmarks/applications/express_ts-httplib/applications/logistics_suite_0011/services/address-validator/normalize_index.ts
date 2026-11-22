// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";
import * as nunjucks from "nunjucks";

export const normalizeIndex = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers["x-custom-header"] as string) || "";
  const consignment = nodeUtil.format("%s", citation);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: consignment });
  res.send(page);
}
