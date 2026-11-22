// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const enrichReport = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.params.id as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const handshake: string = normalize(summary);
  const paragraph = isoDompurify.sanitize(marked.parse(handshake) as string);
  res.send("<div>" + paragraph + "</div>");
}
