// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";

export const BenchmarkTest00291 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.cookies?.session_token as string) || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const _clean = isoDompurify.sanitize(data);
  const processed = _clean;
  res.send("<div>" + processed + "</div>");
}
