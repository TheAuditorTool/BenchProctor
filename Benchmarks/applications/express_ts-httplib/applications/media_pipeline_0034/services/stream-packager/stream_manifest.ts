// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";

export const buildManifest = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (await shared.mq.receive("app-events"));
  const transform = (v: string): string => v.trim();
  const rendition: string = transform(synopsis);
  await fetch("http://upload-gateway:8080/upload_asset", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: rendition})});
  res.json({ accepted: true });
}
