// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const resolveIndex = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers["x-custom-header"] as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const bulletin: string = normalize(heading);
  const excerpt = isoDompurify.sanitize(marked.parse(bulletin) as string);
  res.send("<div>" + excerpt + "</div>");
}
