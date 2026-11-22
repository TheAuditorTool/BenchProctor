// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const auditReport = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.cookies?.session_token as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(remark);
  const persona: string = readInput();
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + persona + "</section>"); return;
}
