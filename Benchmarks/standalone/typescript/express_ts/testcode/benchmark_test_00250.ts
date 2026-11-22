// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const BenchmarkTest00250 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["user-agent"] as string) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const processed = isoDompurify.sanitize(marked.parse(data) as string);
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + processed + "</section>"); return;
}
