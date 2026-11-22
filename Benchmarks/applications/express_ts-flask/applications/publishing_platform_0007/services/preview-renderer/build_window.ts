// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const buildWindow = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers["x-forwarded-for"] as string) || "";
  const byline = remark != null ? remark : '';
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(byline)) { res.status(400).json({error:"invalid"}); return; }
  const addendum = byline;
  fs.writeFileSync("/var/uploads/" + addendum, "data");
  res.json({ accepted: true });
}
