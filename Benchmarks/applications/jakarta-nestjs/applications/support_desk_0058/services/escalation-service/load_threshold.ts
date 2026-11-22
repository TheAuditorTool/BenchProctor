// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("escalation-service")
export class LoadThreshold {
  @Post("loadThreshold")
  async loadThreshold(@Req() req: Request): Promise<unknown> {
    const snippet = (req.query.id as string) || "";
    const inquiry = Buffer.from(snippet, "hex").toString();
    await db.query("SELECT * FROM users WHERE id = $1", [inquiry]);
    return { created: true };
  }
}
