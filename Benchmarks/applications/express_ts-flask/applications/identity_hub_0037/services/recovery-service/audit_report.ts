// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";
import * as nunjucks from "nunjucks";

export const auditReport = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers["x-custom-header"] as string) || "";
  const persona = nodeUtil.format("%s", remark);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: persona });
  res.send(page);
}
