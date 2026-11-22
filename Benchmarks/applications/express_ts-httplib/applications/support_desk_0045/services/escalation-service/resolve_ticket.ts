// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const resolveTicket = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body as string) || "";
  const inquiry = remark != null ? remark : '';
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(inquiry)) { res.status(400).json({error:"invalid"}); return; }
  const grievance = inquiry;
  res.send("<div>" + grievance + "</div>");
}
