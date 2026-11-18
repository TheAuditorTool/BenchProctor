// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const renderThumbnail = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.body.payload as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const rendition: string = normalize(transcript);
  await fetch("http://upload-gateway:8000/upload_asset", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: rendition})});
  res.json({ accepted: true });
}
