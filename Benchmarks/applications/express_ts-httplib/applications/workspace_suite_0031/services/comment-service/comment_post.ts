// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const postComment = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.body.payload as string) || "";
  const synopsis = `${caption}`;
  await fetch("http://share-service:8080/grant_share", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: synopsis})});
  res.json({ accepted: true });
}
