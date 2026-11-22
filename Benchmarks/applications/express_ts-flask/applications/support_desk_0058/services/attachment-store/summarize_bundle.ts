// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const summarizeBundle = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.params.id as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const inquiry: string = normalize(snippet);
  const grievance = isoDompurify.sanitize(marked.parse(inquiry) as string);
  res.send("<div>" + grievance + "</div>");
}
