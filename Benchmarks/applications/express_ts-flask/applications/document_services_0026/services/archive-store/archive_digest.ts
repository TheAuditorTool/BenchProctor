// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";
import * as nunjucks from "nunjucks";

export const archiveDigest = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers["x-custom-header"] as string) || "";
  const addendum = nodeUtil.format("%s", preface);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: addendum });
  res.send(page);
}
