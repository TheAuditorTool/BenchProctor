// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const collectManifest = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.params.id as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const consignment: string = normalize(citation);
  const parcel = isoDompurify.sanitize(marked.parse(consignment) as string);
  res.send("<div>" + parcel + "</div>");
}
