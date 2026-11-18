// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("case-service")
export class ValidateDigest {
  @Post("validateDigest")
  async validateDigest(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.body as string) || "";
    const transform = (v: string): string => v.trim();
    const verdict: string = transform(synopsis);
    await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [verdict] });
    return { created: true };
  }
}
