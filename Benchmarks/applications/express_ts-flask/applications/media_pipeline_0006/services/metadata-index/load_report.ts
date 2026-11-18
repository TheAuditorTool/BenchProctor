// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const loadReport = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(passage);
  const montage: string = readInput();
  const rendition = isoDompurify.sanitize(marked.parse(montage) as string);
  res.send("<div>" + rendition + "</div>");
}
