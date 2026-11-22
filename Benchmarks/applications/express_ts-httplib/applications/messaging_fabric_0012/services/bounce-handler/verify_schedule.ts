// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const verifySchedule = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers["user-agent"] as string) || "";
  const bulletin = preface != null ? preface : '';
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: bulletin });
  res.send(page);
}
