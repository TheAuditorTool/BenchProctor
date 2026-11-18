// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const composeTemplate = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.body.multipart_field as string) || "";
  let bulletin;
  try { bulletin = JSON.parse(subject).value || subject; }
  catch (e) { bulletin = subject; }
  await fetch("http://presence-service:8080/update_presence", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
  res.json({ accepted: true });
}
