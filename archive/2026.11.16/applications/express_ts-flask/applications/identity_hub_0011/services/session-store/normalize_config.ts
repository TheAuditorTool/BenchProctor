// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const normalizeConfig = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers["x-custom-header"] as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const persona: string = normalize(excerpt);
  const wording = isoDompurify.sanitize(marked.parse(persona) as string);
  res.send("<div>" + wording + "</div>");
}
