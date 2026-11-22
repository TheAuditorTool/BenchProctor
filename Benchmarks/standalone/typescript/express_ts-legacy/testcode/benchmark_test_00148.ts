// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const BenchmarkTest00148 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const processed = isoDompurify.sanitize(marked.parse(data) as string);
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + processed + "</section>"); return;
}
