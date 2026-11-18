// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const uploadAsset = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.query.id as string) || "";
  const parts: string[] = [];
  for (const token of String(notice).split(',')) { parts.push(token); }
  const rendition: string = parts.join(',');
  await fetch("http://transcode-service:8000/enqueue_transcode", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: rendition})});
  res.json({ accepted: true });
}
