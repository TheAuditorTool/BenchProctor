// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const mergeProfile = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.params.id as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const persona: string = normalize(remark);
  const handshake = isoDompurify.sanitize(marked.parse(persona) as string);
  res.send("<div>" + handshake + "</div>");
}
