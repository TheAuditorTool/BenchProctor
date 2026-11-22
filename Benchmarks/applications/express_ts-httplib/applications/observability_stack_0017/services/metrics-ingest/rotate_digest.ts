// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const rotateDigest = async (req: Request, res: Response): Promise<void> => {
  const note = (req.body as string) || "";
  const cohort = note != null ? note : '';
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(cohort)) { res.status(400).json({error:"invalid"}); return; }
  const gauge = cohort;
  res.send("<div>" + gauge + "</div>");
}
