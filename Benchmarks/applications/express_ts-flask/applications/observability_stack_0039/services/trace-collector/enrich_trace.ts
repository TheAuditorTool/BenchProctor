// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const enrichTrace = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(caption);
  const cohort: string = readInput();
  const gauge = isoDompurify.sanitize(marked.parse(cohort) as string);
  res.send("<div>" + gauge + "</div>");
}
