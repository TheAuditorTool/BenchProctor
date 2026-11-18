// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const formatHeader = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(caption);
  const gauge: string = readInput();
  const cohort = isoDompurify.sanitize(marked.parse(gauge) as string);
  res.send("<div>" + cohort + "</div>");
}
