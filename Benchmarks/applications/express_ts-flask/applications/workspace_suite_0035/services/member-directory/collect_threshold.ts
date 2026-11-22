// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const collectThreshold = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.params.id as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const wording: string = normalize(paragraph);
  const transcript = isoDompurify.sanitize(marked.parse(wording) as string);
  res.send("<div>" + transcript + "</div>");
}
