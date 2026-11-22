// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const renderProfile = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.params.id as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const bulletin: string = normalize(footnote);
  const snippet = isoDompurify.sanitize(marked.parse(bulletin) as string);
  res.send("<div>" + snippet + "</div>");
}
