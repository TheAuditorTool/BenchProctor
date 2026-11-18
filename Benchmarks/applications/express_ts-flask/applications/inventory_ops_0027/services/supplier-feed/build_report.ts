// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const buildReport = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(summary);
  const restock: string = readInput();
  const backorder = isoDompurify.sanitize(marked.parse(restock) as string);
  res.send("<div>" + backorder + "</div>");
}
