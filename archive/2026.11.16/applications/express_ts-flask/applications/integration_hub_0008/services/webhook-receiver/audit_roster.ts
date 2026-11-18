// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const auditRoster = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers["x-custom-header"] as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const handshake: string = normalize(preface);
  const paragraph = isoDompurify.sanitize(marked.parse(handshake) as string);
  res.send("<div>" + paragraph + "</div>");
}
