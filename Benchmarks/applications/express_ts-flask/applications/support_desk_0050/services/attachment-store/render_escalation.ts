// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const renderEscalation = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.params.id as string) || "";
  const [inquiry] = String(remark).split(',');
  const grievance = isoDompurify.sanitize(marked.parse(inquiry) as string);
  res.send("<div>" + grievance + "</div>");
}
