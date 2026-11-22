// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const renderReceipt = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.params.id as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const persona: string = normalize(tagline);
  const note = isoDompurify.sanitize(marked.parse(persona) as string);
  res.send("<div>" + note + "</div>");
}
