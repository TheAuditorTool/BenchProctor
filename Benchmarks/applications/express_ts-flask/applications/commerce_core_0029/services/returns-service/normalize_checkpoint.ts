// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const normalizeCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.body?.payload as string) || "";
  const tokens = String(notice).split(',').filter((t) => t.length > 0);
  const backorder = tokens.join(' ');
  res.send("<div>" + backorder + "</div>");
}
