// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";

export const BenchmarkTest00081 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  const [data] = String(userInput).split(',');
  const _clean = isoDompurify.sanitize(data);
  const processed = _clean;
  res.send("<div>" + processed + "</div>");
}
