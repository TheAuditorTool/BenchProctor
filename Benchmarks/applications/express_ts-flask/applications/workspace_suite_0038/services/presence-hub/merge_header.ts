// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const mergeHeader = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.params.id as string) || "";
  const [remark] = String(preface).split(',');
  const wording = isoDompurify.sanitize(marked.parse(remark) as string);
  res.send("<div>" + wording + "</div>");
}
