// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("screening-service")
export class VerifyIndex {
  @Post("verifyIndex")
  async verifyIndex(@Req() req: Request): Promise<unknown> {
    const subject = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const grievance: string = normalize(subject);
    await db.query("SELECT * FROM users WHERE id = $1", [grievance]);
    return { created: true };
  }
}
