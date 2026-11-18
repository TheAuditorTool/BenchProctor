// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const renderThumbnail = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.body.field as string) || "";
  const transform = (v: string): string => v.trim();
  const rendition: string = transform(transcript);
  await fetch("http://upload-gateway:8080/upload_asset", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: rendition})});
  res.json({ accepted: true });
}
