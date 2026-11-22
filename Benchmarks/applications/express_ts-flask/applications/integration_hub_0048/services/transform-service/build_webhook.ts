// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const buildWebhook = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.params.id as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const handshake: string = normalize(citation);
  const heading = isoDompurify.sanitize(marked.parse(handshake) as string);
  res.send("<div>" + heading + "</div>");
}
