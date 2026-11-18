// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const auditSummary = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(summary);
  const grievance: string = readInput();
  const verdict = isoDompurify.sanitize(marked.parse(grievance) as string);
  res.send("<div>" + verdict + "</div>");
}
