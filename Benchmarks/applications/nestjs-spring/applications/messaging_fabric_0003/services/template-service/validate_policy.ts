// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("template-service")
export class ValidatePolicy {
  @Post("validatePolicy")
  async validatePolicy(@Req() req: Request): Promise<unknown> {
    const subject = (req.body as string) || "";
    const transform = (v: string): string => v.trim();
    const bulletin: string = transform(subject);
    await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [bulletin] });
    return { created: true };
  }
}
