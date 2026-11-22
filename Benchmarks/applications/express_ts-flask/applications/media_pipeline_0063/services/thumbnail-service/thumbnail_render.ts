// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const renderThumbnail = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.headers["x-forwarded-for"] as string) || "";
  const montage = snippet != null ? snippet : '';
  await fetch("http://caption-service:8000/extract_caption", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: montage})});
  res.json({ accepted: true });
}
