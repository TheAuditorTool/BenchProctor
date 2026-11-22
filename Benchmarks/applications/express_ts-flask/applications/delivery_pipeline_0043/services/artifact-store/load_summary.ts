// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const loadSummary = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body.payload as string) || "";
  const tokens = String(remark).split(',').filter((t) => t.length > 0);
  const note = tokens.join(' ');
  res.send("<div>" + note + "</div>");
}
