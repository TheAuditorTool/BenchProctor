// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const updatePresence = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.body.multipart_field as string) || "";
  const bulletin = decodeURIComponent(preface);
  await fetch("http://template-service:8080/compose_template", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
  res.json({ accepted: true });
}
