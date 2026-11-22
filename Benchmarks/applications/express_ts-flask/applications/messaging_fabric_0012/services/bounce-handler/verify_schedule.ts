// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";
import * as nunjucks from "nunjucks";

export const verifySchedule = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers["x-custom-header"] as string) || "";
  const bulletin = nodeUtil.format("%s", preface);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: bulletin });
  res.send(page);
}
