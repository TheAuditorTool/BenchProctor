// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const rotateDelivery = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(paragraph);
  const bulletin: string = readInput();
  const synopsis = isoDompurify.sanitize(marked.parse(bulletin) as string);
  res.send("<div>" + synopsis + "</div>");
}
