// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const rotateScreening = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.params.id as string) || "";
  const [verdict] = String(synopsis).split(',');
  const grievance = isoDompurify.sanitize(marked.parse(verdict) as string);
  res.send("<div>" + grievance + "</div>");
}
