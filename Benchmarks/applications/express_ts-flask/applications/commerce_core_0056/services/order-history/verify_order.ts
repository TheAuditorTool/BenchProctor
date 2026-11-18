// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const verifyOrder = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(citation);
  const backorder: string = readInput();
  const voucher = isoDompurify.sanitize(marked.parse(backorder) as string);
  res.send("<div>" + voucher + "</div>");
}
