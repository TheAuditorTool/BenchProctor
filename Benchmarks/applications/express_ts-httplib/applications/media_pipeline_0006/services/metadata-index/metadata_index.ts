// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const indexMetadata = async (req: Request, res: Response): Promise<void> => {
  const passage = ((req as any).file?.originalname as string) || "";
  const transform = (v: string): string => v.trim();
  const montage: string = transform(passage);
  await fetch("http://thumbnail-service:8080/render_thumbnail", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: montage})});
  res.json({ accepted: true });
}
