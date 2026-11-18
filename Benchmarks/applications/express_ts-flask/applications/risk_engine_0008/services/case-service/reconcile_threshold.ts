// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const reconcileThreshold = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(synopsis);
  const verdict: string = readInput();
  const grievance = isoDompurify.sanitize(marked.parse(verdict) as string);
  res.send("<div>" + grievance + "</div>");
}
