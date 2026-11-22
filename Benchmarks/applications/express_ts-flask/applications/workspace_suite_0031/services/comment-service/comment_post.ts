// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const postComment = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.body?.multipart_field as string) || "";
  const formData = Object.freeze({ payload: caption });
  const synopsis = formData.payload;
  await fetch("http://share-service:8000/grant_share", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: synopsis})});
  res.json({ accepted: true });
}
