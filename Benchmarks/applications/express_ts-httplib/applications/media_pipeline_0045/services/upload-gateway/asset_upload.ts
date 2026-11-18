// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const uploadAsset = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.headers["x-custom-header"] as string) || "";
  const formData = Object.freeze({ payload: notice });
  const rendition = formData.payload;
  await fetch("http://transcode-service:8080/enqueue_transcode", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: rendition})});
  res.json({ accepted: true });
}
