// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const resolveConfig = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.cookies?.session_token as string) || "";
  const tokens = String(preface).split(',').filter((t) => t.length > 0);
  const grievance = tokens.join(' ');
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + grievance + "</section>"); return;
}
