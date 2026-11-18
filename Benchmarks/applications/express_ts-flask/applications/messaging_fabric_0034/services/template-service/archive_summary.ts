// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const archiveSummary = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(footnote);
  const bulletin: string = readInput();
  const heading = isoDompurify.sanitize(marked.parse(bulletin) as string);
  res.send("<div>" + heading + "</div>");
}
