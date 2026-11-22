// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const reconcileThreshold = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.params.id as string) || "";
  const transform = (v: string): string => v.trim();
  const gauge: string = transform(remark);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(gauge)) { res.status(400).json({error:"invalid"}); return; }
  const cohort = gauge;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: cohort });
  res.send(page);
}
