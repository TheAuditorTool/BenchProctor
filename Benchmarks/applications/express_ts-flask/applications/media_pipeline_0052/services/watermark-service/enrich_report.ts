// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const enrichReport = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(tagline);
  const rendition: string = readInput();
  const montage = isoDompurify.sanitize(marked.parse(rendition) as string);
  res.send("<div>" + montage + "</div>");
}
