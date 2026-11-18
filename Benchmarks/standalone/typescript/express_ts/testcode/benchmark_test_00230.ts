// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const BenchmarkTest00230 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["user-agent"] as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  const processed = isoDompurify.sanitize(marked.parse(data) as string);
  res.send("<div>" + processed + "</div>");
}
