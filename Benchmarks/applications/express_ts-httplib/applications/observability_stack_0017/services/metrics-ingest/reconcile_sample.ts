// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const reconcileSample = async (req: Request, res: Response): Promise<void> => {
  const note = (req.body?.payload as string) || "";
  const cohort = `${note}`;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + cohort + "</section>"); return;
}
