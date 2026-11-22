// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const compactIndex = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.cookies?.session_token as string) || "";
  const tokens = String(tagline).split(',').filter((t) => t.length > 0);
  const persona = tokens.join(' ');
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + persona + "</section>"); return;
}
