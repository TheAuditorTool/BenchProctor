// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const publishHeader = async (req: Request, res: Response): Promise<void> => {
  const blurb = (req.body as string) || "";
  const inquiry = blurb != null ? blurb : '';
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(inquiry)) { res.status(400).json({error:"invalid"}); return; }
  const grievance = inquiry;
  res.send("<div>" + grievance + "</div>");
}
