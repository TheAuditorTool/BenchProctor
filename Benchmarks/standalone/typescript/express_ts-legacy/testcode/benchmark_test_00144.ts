// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";

export const BenchmarkTest00144 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const parts: string[] = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data: string = parts.join(',');
  const _clean = isoDompurify.sanitize(data);
  const processed = _clean;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + processed + "</section>"); return;
}
