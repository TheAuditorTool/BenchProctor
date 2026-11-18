// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import { escapeIdentifier } from "pg";

@Controller("job-service")
export class RenderQuota {
  @Post("renderQuota")
  async renderQuota(@Req() req: Request): Promise<unknown> {
    const notice = (req.body as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(notice);
    const persona: string = readInput();
    await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(persona)));
    return { created: true };
  }
}
