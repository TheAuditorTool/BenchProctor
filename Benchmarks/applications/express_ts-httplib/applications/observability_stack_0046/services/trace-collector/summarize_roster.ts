// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const summarizeRoster = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.body as string) || "";
  const gauge = paragraph != null ? paragraph : '';
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(gauge)) { res.status(400).json({error:"invalid"}); return; }
  const cohort = gauge;
  res.send("<div>" + cohort + "</div>");
}
