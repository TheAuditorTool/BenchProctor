// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const compactBatch = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.params.id as string) || "";
  const [bulletin] = String(paragraph).split(',');
  const synopsis = isoDompurify.sanitize(marked.parse(bulletin) as string);
  res.send("<div>" + synopsis + "</div>");
}
