// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const formatRevision = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body as string) || "";
  const byline = remark != null ? remark : '';
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(byline)) { res.status(400).json({error:"invalid"}); return; }
  const addendum = byline;
  res.send("<div>" + addendum + "</div>");
}
