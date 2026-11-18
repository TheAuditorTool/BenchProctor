// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("partner-registry")
export class VerifyThreshold {
  @Post("verifyThreshold")
  async verifyThreshold(@Req() req: Request): Promise<unknown> {
    const blurb = (req.body.payload as string) || "";
    const transform = (v: string): string => v.trim();
    const handshake: string = transform(blurb);
    await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [handshake] });
    return { created: true };
  }
}
