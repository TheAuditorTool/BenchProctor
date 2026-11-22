// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const fetchReport = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.cookies?.session_token as string) || "";
  const tokens = String(paragraph).split(',').filter((t) => t.length > 0);
  const gauge = tokens.join(' ');
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + gauge + "</section>"); return;
}
