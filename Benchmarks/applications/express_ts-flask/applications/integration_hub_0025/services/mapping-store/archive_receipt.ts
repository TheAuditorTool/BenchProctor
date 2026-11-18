// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const archiveReceipt = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.params.id as string) || "";
  const [handshake] = String(footnote).split(',');
  const blurb = isoDompurify.sanitize(marked.parse(handshake) as string);
  res.send("<div>" + blurb + "</div>");
}
