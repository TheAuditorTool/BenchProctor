// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const annotateProfile = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers["x-custom-header"] as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const dossier: string = normalize(excerpt);
  const addendum = isoDompurify.sanitize(marked.parse(dossier) as string);
  res.send("<div>" + addendum + "</div>");
}
