// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";
import * as nunjucks from "nunjucks";

export const archiveHeader = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers["x-custom-header"] as string) || "";
  const restock = nodeUtil.format("%s", excerpt);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: restock });
  res.send(page);
}
