// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";

export const BenchmarkTest00322 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  const data = userInput != null ? userInput : '';
  const _clean = isoDompurify.sanitize(data);
  const processed = _clean;
  res.send("<div>" + processed + "</div>");
}
