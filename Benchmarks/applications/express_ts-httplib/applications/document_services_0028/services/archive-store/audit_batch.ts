// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const auditBatch = async (req: Request, res: Response): Promise<void> => {
  const note = (req.body.field as string) || "";
  const transform = (v: string): string => v.trim();
  const addendum: string = transform(note);
  const dossier = addendum.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.send("<div>" + dossier + "</div>");
}
