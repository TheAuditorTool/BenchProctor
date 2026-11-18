// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const BenchmarkTest00634 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.payload as string) || "";
  const data = nodeUtil.format("%s", userInput);
  const processed = isoDompurify.sanitize(marked.parse(data) as string);
  res.send("<div>" + processed + "</div>");
}
