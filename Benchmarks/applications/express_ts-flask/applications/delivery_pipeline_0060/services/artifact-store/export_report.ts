// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const exportReport = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(wording);
  const remark: string = readInput();
  const phrase = isoDompurify.sanitize(marked.parse(remark) as string);
  res.send("<div>" + phrase + "</div>");
}
