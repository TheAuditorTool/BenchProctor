// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const renderThumbnail = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers["x-forwarded-for"] as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(citation);
  const rendition: string = readInput();
  await fetch("http://metadata-index:8000/index_metadata", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: rendition})});
  res.json({ accepted: true });
}
