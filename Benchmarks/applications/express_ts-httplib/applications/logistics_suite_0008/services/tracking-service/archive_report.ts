// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const archiveReport = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.cookies?.session_token as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(caption);
  const consignment: string = readInput();
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + consignment + "</section>"); return;
}
