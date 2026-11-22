// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const resolveManifest = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.cookies?.session_token as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(transcript);
  const addendum: string = readInput();
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + addendum + "</section>"); return;
}
