// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const resolveProfile = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.params.id as string) || "";
  const [dossier] = String(passage).split(',');
  const addendum = isoDompurify.sanitize(marked.parse(dossier) as string);
  res.send("<div>" + addendum + "</div>");
}
