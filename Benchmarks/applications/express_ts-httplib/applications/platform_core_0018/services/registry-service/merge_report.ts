// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const mergeReport = async (req: Request, res: Response): Promise<void> => {
  const subtitle = (req.headers["user-agent"] as string) || "";
  const persona = subtitle != null ? subtitle : '';
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: persona });
  res.send(page);
}
