// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const buildManifest = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.body?.field as string) || "";
  const pending: string[] = String(synopsis).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const rendition: string = collected.join(',');
  await fetch("http://upload-gateway:8000/upload_asset", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: rendition})});
  res.json({ accepted: true });
}
