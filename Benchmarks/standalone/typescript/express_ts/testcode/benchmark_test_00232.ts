// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";

export const BenchmarkTest00232 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.cookies?.session_token as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  const _clean = isoDompurify.sanitize(data);
  const processed = _clean;
  res.send("<div>" + processed + "</div>");
}
