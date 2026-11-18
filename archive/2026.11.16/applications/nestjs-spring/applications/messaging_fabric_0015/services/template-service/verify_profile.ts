// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import { escapeIdentifier } from "pg";

@Controller("template-service")
export class VerifyProfile {
  @Post("verifyProfile")
  async verifyProfile(@Req() req: Request): Promise<unknown> {
    const heading = (req.body as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(heading);
    const bulletin: string = readInput();
    await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(bulletin)));
    return { created: true };
  }
}
