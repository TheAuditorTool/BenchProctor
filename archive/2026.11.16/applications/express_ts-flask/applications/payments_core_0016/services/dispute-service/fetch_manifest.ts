// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const fetchManifest = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.headers["x-custom-header"] as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const remittance: string = normalize(passage);
  const disbursement = isoDompurify.sanitize(marked.parse(remittance) as string);
  res.send("<div>" + disbursement + "</div>");
}
