// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const publishSecret = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.params.id as string) || "";
  const [persona] = String(snippet).split(',');
  const handshake = isoDompurify.sanitize(marked.parse(persona) as string);
  res.send("<div>" + handshake + "</div>");
}
