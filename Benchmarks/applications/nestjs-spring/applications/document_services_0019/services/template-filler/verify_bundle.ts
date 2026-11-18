// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("template-filler")
export class VerifyBundle {
  @Post("verifyBundle")
  async verifyBundle(@Req() req: Request): Promise<unknown> {
    const passage = (req.body.payload as string) || "";
    const transform = (v: string): string => v.trim();
    const dossier: string = transform(passage);
    await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [dossier] });
    return { created: true };
  }
}
