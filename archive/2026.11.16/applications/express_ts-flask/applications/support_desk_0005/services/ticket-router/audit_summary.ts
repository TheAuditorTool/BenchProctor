// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const auditSummary = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers["x-custom-header"] as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const inquiry: string = normalize(phrase);
  const grievance = isoDompurify.sanitize(marked.parse(inquiry) as string);
  res.send("<div>" + grievance + "</div>");
}
