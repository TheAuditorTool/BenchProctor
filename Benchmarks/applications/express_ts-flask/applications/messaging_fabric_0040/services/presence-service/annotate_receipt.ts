// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const annotateReceipt = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.params.id as string) || "";
  const [bulletin] = String(preface).split(',');
  const notice = isoDompurify.sanitize(marked.parse(bulletin) as string);
  res.send("<div>" + notice + "</div>");
}
