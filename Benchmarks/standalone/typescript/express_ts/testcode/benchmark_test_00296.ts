// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const BenchmarkTest00296 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.cookies?.session_token as string) || "";
  const data = decodeURIComponent(userInput);
  const processed = isoDompurify.sanitize(marked.parse(data) as string);
  res.send("<div>" + processed + "</div>");
}
