// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const rotateConversion = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.headers["user-agent"] as string) || "";
  const addendum = snippet != null ? snippet : '';
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: addendum });
  res.send(page);
}
